import xml.etree.ElementTree as ET

def xml_to_github_markdown(xml_path, md_path):
    # Define DDI namespace (must match the XML structure)
    ns = {"ddi": "ddi:codebook:2_5"}
    
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Error loading XML: {e}")
        return

    # Extract all variable tags (<var>)
    variables = root.findall(".//ddi:dataDscr/ddi:var", ns)
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("#IPUMS CPS Data Codebook\n\n")
        f.write("This document provides a summary of the extracted data variables.\n\n")

        # 1. Variable Summary Table (Top Section)
        f.write("## 1. Variable List\n")
        f.write("| Variable | Label | Description | Universe |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        
        # List to store categorical variables for detailed output later
        cat_variables = [] 

        for var in variables:
            name = var.get("name", "N/A")
            
            # Find specific tags (with None-check for safety)
            labl = var.find("ddi:labl", ns)
            txt = var.find("ddi:txt", ns)
            univ = var.find("ddi:universe", ns)
            
            l_text = labl.text.strip() if labl is not None and labl.text else "-"
            t_text = txt.text.strip() if txt is not None and txt.text else "-"
            u_text = univ.text.strip() if univ is not None and univ.text else "-"
            
            # Append a row to the summary table
            f.write(f"| **{name}** | {l_text} | {t_text} | {u_text} |\n")
            
            # Collect variables that have category values (<catgry>)
            categories = var.findall("ddi:catgry", ns)
            if categories:
                cat_variables.append((name, l_text, categories))

        # 2. Detailed Value Labels (Bottom Section)
        if cat_variables:
            f.write("\n---\n\n## 2. Value Labels\n")
            for name, label, cats in cat_variables:
                f.write(f"\n### {name} : {label}\n")
                f.write("| Code | Label |\n")
                f.write("| :--- | :--- |\n")
                for cat in cats:
                    v = cat.find("ddi:catValu", ns)
                    l = cat.find("ddi:labl", ns)
                    v_txt = v.text.strip() if v is not None and v.text else "?"
                    l_txt = l.text.strip() if l is not None and l.text else "?"
                    f.write(f"| {v_txt} | {l_txt} |\n")

    print(f"Conversion complete! Markdown saved to: '{md_path}'")

# Usage Example
xml_to_github_markdown("data/codebook/cps_00002.xml", "data/codebook/codebook.md")