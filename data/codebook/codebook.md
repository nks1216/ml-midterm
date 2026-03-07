#IPUMS CPS Data Codebook

This document provides a summary of the extracted data variables.

## 1. Variable List
| Variable | Label | Description | Universe |
| :--- | :--- | :--- | :--- |
| **YEAR** | Survey year | YEAR reports the year in which the survey was conducted.  YEARP is repeated on person records. | - |
| **SERIAL** | Household serial number | SERIAL is an identifying number unique to each household in a given survey month and year.  All person records are assigned the same serial number as the household record they follow.  A combination of YEAR, MONTH, and SERIAL provides a within-sample unique identifier for every household in IPUMS-CPS; YEAR, MONTH, SERIAL, and PERNUM uniquely identify every person within a single sample.

SERIAL is a new value generated for IPUMS-CPS and should not be confused with the household serial number created by the Census Bureau and included in the original CPS data. | - |
| **MONTH** | Month | MONTH indicates the calendar month of the CPS interview. | - |
| **CPSID** | CPSID, household record | CPSID is an IPUMS-CPS defined variable that uniquely identifies households across CPS samples. The first six digits of CPSID index the four-digit year and two-digit month that the household was first in the CPS. CPSID allows users to link a household record across samples, based on the 4-8-4 rotation pattern, by assigning a unique CPSID value based on a combination of household identifiers. CPSID will only ever appear for a maximum of 8 times, which is the number of times a household may be observed in the CPS survey (as indexed by MISH). In some cases, a household will appear fewer than 8 times due to migration, mortality, non-response, and recording errors. CPSID Extensive documentation about the creation of CPSID is available elsewhere.

CPSID may also be used to link ASEC households that appear in the March Basic Monthly file to other months of CPS data. This linking is made possible by IPUMS through the creation of MARBASECIDH. For further information about the relationship between the March Basic and the ASEC, please see our additional documentation.

Households that are part of the ASEC oversample (as indicated by ASECOVERH) may also be linked across ASEC samples, but not to the March or any other Basic Monthly sample. Note that MISH is not a reliable indicator of rotation pattern status for ASEC oversample records and should not be used to validate matches. For further information on linking records across ASEC samples, please see our additional documentation.

Users may also want to see CPSIDP and CPSIDV for more information about linking individuals across time using a person-specific version of CPSID. | - |
| **ASECFLAG** | Flag for ASEC | ASECFLAG indicates whether the respondent is part of the ASEC or the March Basic. This variable is useful for users who wish to distinguish ASEC and March Basic files in their extracts. See further information about the ASEC versus the March Basic Monthly Files. | - |
| **ASECWTH** | Annual Social and Economic Supplement Household weight | ASECWTH is a household-level weight that should be used to generate statistics about households in March Annual Social and Economic (ASEC) Supplement data. The CPS uses a complex stratified sampling scheme, and ASECWTH must be used to produce unbiased household-level statistics from the IPUMS-CPS ASEC data. For analyses of non-ASEC data, researchers should use HWTFINL. For individual-level analyses, researchers should use WTFINL, ASECWT, or EARNWT. 

ASECWTH generally has the same value as WTSUPP for the household head or reference person. Vacant housing units and households that could not be interviewed due to residents' absence or refusal to participate have a value of zero in HWTSUPP; such sampled units were included in the public use CPS data beginning in 1988. 

Estimates on the entire population are prepared by projecting forward the resident population from the last available census. These projections are derived by updating the demographic census data from a number of other data sources that account for death, births and net migration. About 3 years after every census (i.e. 2003 for the 2000 Census and 2013 for the 2010 Census), the Census Bureau updates its independent population control and provides a new weight for the relevant years.

Two important points should be noted here. First, the lag between when the Census is conducted and when the CPS weights are updated is about 3 years. While the Census data are being processed, the CPS files are made available using the weighting scheme from the US Census prior to the latest Census. Second, once the files are updated, the old weights become obsolete and are replaced in the IPUMS data extract system. Published estimates from the lag years that use the old weights are not always updated. For example, 2010 poverty estimates were released in ASEC using the 2000 population controls. Once the 2010 population controls were made available, IPUMS-CPS replaced the ASEC 2010, 2011, and 2012 weights that are based on the 2000 population control with weights that are based on the 2010 population controls.

IPUMS-CPS makes available only the most up-to-date weights. The old values are available here: Old SPM and Weights Values. | - |
| **NUMPREC** | Number of person records following | NUMPREC reports the number of person records following the household record.  These person records all have the same serial number (SERIAL) as the household record. | - |
| **HHINTYPE** | Type of household | HHINTYPE is a household-level variable indicating whether members of the household were interviewed and, if not, why no interview took place.  Type A nonresponse households represent housing units suitable for inclusion in the survey whose residents were not interviewed for reasons such as refusal to participate and temporary absence.  Type B nonresponse households were vacant or were occupied by persons ineligible for interview (e.g., institutionalized persons).  Type C nonresponse households were housing units that were demolished, converted to storage or business use, or included in the sample by mistake.

Sampling for the CPS is based on housing units (addresses) rather than persons.  For this reason, interviewers necessarily initially visit some unoccupied or uninhabitable dwellings.  Participation in the survey is voluntary, rather than required by law, and institutionalized persons are intentionally excluded. | - |
| **REGION** | Region and division | REGION identifies the region and division where the housing unit was located. Unless otherwise noted in the comparability discussion, states are recoded into the following 1990 regional and divisional classification system: 

1. Northeast Region
New England Division: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont

Middle Atlantic Division: New Jersey, New York, Pennsylvania
2. Midwest (formerly North Central) Region
East North Central Division: Illinois, Indiana, Michigan, Ohio, Wisconsin

West North Central Division: Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota
3. South Region
South Atlantic Division: Delaware, District of Columbia, Florida, Georgia, Maryland, North Carolina, South Carolina, Virginia, West Virginia

East South Central Division: Alabama, Kentucky, Mississippi, Tennessee

West South Central Division: Arkansas, Louisiana , Oklahoma, Texas
4. West Region
Mountain Division: Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, Wyoming

Pacific Division: Alaska, California, Hawaii, Oregon, Washington | - |
| **STATEFIP** | State (FIPS code) | STATEFIP identifies the household's state of residence, using the Federal Information Processing Standards (FIPS) coding scheme, which orders the states alphabetically.

In 1973-1975 ASEC samples, all households in the Anaheim-Santa Ana-Garden Grove, CA METAREA are coded as Michigan-Wisconsin for STATEFIP in the original data. As there is insufficient geographic information in the public use data to determine which variable is in error, this mistake has been left un-recoded. | - |
| **STATECENSUS** | State (Census code) | STATECENSUS identifies the household's state of residence using Census state codes. | - |
| **METFIPS** | Metropolitan area (FIPS code) | METFIPS gives the original (unrecoded) CPS codes for the respondent's metropolitan area of residence. A metropolitan area, or metro area, is a region consisting of a large urban core together with surrounding communities that have a high degree of economic and social integration with the urban core. Metro areas are defined by the Office of Management and Budget (OMB), which occasionally makes significant changes to its protocols and regularly revises the delineations of metro areas to reflect current population distributions and commuting flows. Metro areas can cross state lines, and they are county-based except in New England. (Prior to the institution of the 2003 OMB protocols, metro areas in New England were based on towns and cities. Now all official metro areas are county-based, but the CPS continues to use special town-based definitions for New England, which the OMB calls New England City and Town Areas, or NECTAs.)

See also (METRO), which identifies whether a household resided in a metro area and specifically whether it resided in a central/principal city of a metro area. For 1962-2022 samples, IPUMS CPS includes a separate variable, METAREA, which aimed to apply a consistent coding scheme across all samples based on the FIPS codes in use with the 1990 census. As explained in that variable's description, it is not altogether possible to maintain both consistency and comparability, and the complications of maintaining that approach have led both IPUMS USA and CPS to discontinue updates to their METAREA variables.

METFIPS information was added to the ASEC CPS data by the Census Bureau, not collected from respondents.

Not all metropolitan areas are identified: see under "Codes" for more information. Note also that some component counties are not included in the CPS sample of households in certain metropolitan areas. See the "Specific Metropolitan Identifiers" Appendix of the appropriate month's technical documentation for more information on whether a specific metropolitan area sample has excluded components. For more information on the definitions and components of metropolitan areas over time, see the Census Bureau website; for the current metropolitan area definitions, see here.

Note that the Census Bureau warns: "One set of estimates that can be produced from CPS microdata files should be treated with caution. These are estimates for individual metropolitan areas. Although estimates for the larger areas such as New York, Los Angeles, and so forth, should be fairly accurate and valid for a multitude of uses, estimates for the smaller metropolitan areas (those with populations under 500,000) should be used with caution because of the relatively large sampling variability associated with these estimates." | - |
| **METRO** | Metropolitan and central/principal city status | METRO indicates whether a household resided in a metropolitan area. For households within metropolitan areas, METRO also indicates whether the housing unit was inside or outside of a central/principal city. The Census Bureau adds this information itself and does not collect it directly from respondents. | - |
| **CBSASZ** | Core-based (metro/micro) statistical area size | CBSASZ identifies the population size of the core based statistical area (CBSA) in which the household is located. CBSA's are classified as either metropolitan or micropolitan statistical areas, but micropolitan areas are too small to be identified in the CPS public use microdata, so CBSASZ provides sizes of metropolitan areas only.

Users should note that official definitions of metropolitan areas have changed over time. Please see the comparability tab for more details. 

The Census Bureau publishes records of re-categorized or newly introduced metropolitan areas on its Historical Statistical Area Delineations page. | - |
| **INDIVIDCC** | Individual central/principal city | For households that reside in a central/principal city of a metropolitan area, INDIVIDCC identifies the individual city of residence. In the official metropolitan area definitions produced by the Office of Management and Budget (OMB), every metropolitan area contains one or more "central cities" (in pre-2003 definitions) or "principal cities" (in definitions since 2003). The central/principal cities include the largest city in each metropolitan area by population along with certain other large cities that meet requirements stipulated by the OMB protocols in use at the time. Not all central/principal cities are identified. INDIVIDCC must be used along with METFIPS and (sometimes) COUNTY or STATEFIP to uniquely identify cities. (More information is under the "Codes" tab).

Note that for many cities, sample sizes will be too small to provide reliable city-level statistics. | - |
| **PLACEFIPS** | FIPS code for central/principal city of residence | For households that reside in a central/principal city of a metropolitan area, PLACEFIPS gives the FIPS (Federal Information Processing Series) code for the central/principal city of residence. In the official metropolitan area definitions produced by the Office of Management and Budget (OMB), every metropolitan area contains one or more "central cities" (in pre-2003 definitions) or "principal cities" (in definitions since 2003). The central/principal cities include the largest city in each metropolitan area by population along with certain other large cities that meet requirements stipulated by the OMB protocols in use at the time. Not all central/principal cities are identified.

While INDIVIDCC also identifies the central/principal city of residence, PLACEFIPS adds a FIPS coding scheme to support linking central/principal city-level data to CPS respondents. FIPS codes were developed by the National Institute of Standards and Technology (NIST) in the 1980s and have been used by the Census Bureau for decennial censuses since 1990 and in many other datasets published by the United States government (e.g., American Community Survey). FIPS codes are assigned to each place in alphabetical order within a state.  

PLACEFIPS codes are state-dependent; they must be combined with state codes (see STATEFIP and STATECENSUS) to uniquely identify cities located in different states. To determine which metropolitan area the PLACEFIPS unit is located within, users should inspect the METAREA code associated with a specific PLACEFIPS code. 

PLACEFIPS codes are available for the CPS samples from September 1995 to the present. For samples from October 1985 - May 1995, the PLACECENSUS variable should be used. From June - August 1995, no METAREA or INDIVIDCC codes were reported in the CPS samples. | - |
| **OWNERSHP** | Ownership of dwelling | OWNERSHP indicates whether the household rented or owned its housing unit. Households that acquired their unit with a mortgage or other lending arrangement were understood to "own" their unit even if they had not yet completed repayment. 

Two types of renters were identified: those who paid cash rent and those who paid no cash rent.  The latter category included occupants who paid only for their utilities. | - |
| **HHINCOME** | Total household income | HHINCOME reports the total money income during the previous calendar year of all adult household members.  The amount should equal the sum of all household members' individual incomes as recorded in the IPUMS-CPS variable INCTOT.  The persons included were those present in the household at the time of the survey.  People who lived in the household during the previous year but were not still living there at the time of the survey are not included; household members who lived elsewhere during the previous year but had joined the household at the time of the survey are included. | - |
| **PUBHOUS** | Living in public housing | PUBHOUS indicates whether the house, apartment, or mobile home is part of a government housing project for people with low incomes, commonly known as a "public housing project."

Participation in public housing is determined by two factors: program eligibility and the availability of housing. Income standards for initial and continuing occupancy vary across local housing authorities, although Federal guidelines set broad limits. Rental charges define net benefits and cannot exceed 30 percent of the family's or the individual's net monthly income. A public housing unit can be occupied by a family of two or more related persons or an individual who is handicapped, elderly, or displaced by urban renewal or natural disaster. 

An alternative form of housing assistance is rent subsidy, in which the rent for a housing unit is reduced because the Federal, state, or local government is paying part of the cost.  See (RENTSUB).
 
Households coded as "Yes" in PUBHOUS or RENTSUB were receiving housing assistance at the time of the ASEC survey.  The reference period for some other non-cash benefits is the preceding calendar year (for Food Stamps) or the previous six months (for heat subsidy). 

For some variables relating to means-tested government assistance, including PUBHOUS, information was collected only from households whose estimated income fell below a given threshold.  During the first month that a household entered the survey, and one year later, the CPS interviewer asked the respondent to estimate the family's total income in the past twelve months, by choosing one of fourteen broad categories.  Only households in which the household members' combined income fell below a given level (e.g., under 30,000 dollars in the 1980s) were questioned about means-tested program benefits.  Households with estimated incomes above the threshold were presumed to not qualify for or receive such benefits, and were not asked these questions, to limit the length of interviews.  Households that were not questioned were coded as "no" for several variables relating to the receipt of means-tested benefits, including PUBHOUS. | - |
| **RENTSUB** | Paying lower rent due to government subsidy | RENTSUB indicates whether the rent on the house, apartment or mobile home is reduced because a Federal, state or local government is paying part of the cost. With rent subsidies, the difference between the "fair market" rent and the rent charged to the tenant in private sector housing is paid to the owner by a government agency, using federal, state, or local funds.  See also (PUBHOUS) for information on public housing, an alternative form of housing assistance to low-income families and individuals. 

For some variables relating to means-tested government assistance, including RENTSUB, information was collected only from households whose estimated income fell below a given threshold.  During the first month that a household entered the survey, and one year later, the CPS interviewer asked the respondent to estimate the family's total income in the past twelve months, by choosing one of fourteen broad categories.  Only households in which the household members' combined income fell below a given level (e.g., under 30,000 dollars in the 1980s) were questioned about means-tested program benefits.  Households with estimated incomes above the threshold were presumed to not qualify for or receive such benefits, and were not asked these questions, to limit the length of interviews.  Households that were not questioned were coded as "no" for several variables relating to the receipt of means-tested benefits, including RENTSUB. | - |
| **HEATSUB** | Received energy subsidy | HEATSUB indicates whether the household had been enrolled in or had received benefits from the Federal home heating and cooling assistance program at any time since the beginning of October of the previous year. 

The Low-Income Home Energy Assistance Program provides financial assistance to qualified households to help them pay heating costs. The program is funded by the Federal government and administered by the States under broad guidelines. In some states a household may automatically be eligible for this program if the members receive: (1) Aid to Families with Dependent Children (AFDC); (2) Food Stamps; (3) Supplemental Security Income (SSI); or (4) certain Veterans' benefits. 

(HEATVAL) gives the total value of energy assistance received in the past six months.  (HEATPAY) specifies the form of payment for heat subsidy recipients.  (NOHEAT) identifies households that reported being without heat for one or more days in the past six months, due to inability to pay the utility or fuel bill.  (FUELHEAT) specifies the type of heating fuel used, for households receiving energy assistance.

For some variables relating to means-tested government assistance, including HEATSUB, information was collected only from households whose estimated income fell below a given threshold.  During the first month that a household entered the survey, and one year later, the CPS interviewer asked the respondent to estimate the family's total income in the past twelve months, by choosing one of fourteen broad categories.  Only households in which the members' combined income fell below a given level (e.g., under 30,000 dollars in the 1980s) were questioned about means-tested program benefits.  Households with estimated incomes above the threshold were presumed to not qualify for or receive such benefits, and were not asked these questions, to limit the length of interviews.  Households that were not questioned were coded as "no" for several variables relating to the receipt of means-tested benefits, including HEATSUB.

In the 1982-1987 samples, there are some interview households which were incorrectly been coded as NIU in the original data for this variable. | - |
| **HEATVAL** | Value of energy subsidy | HEATVAL specifies the total value of energy assistance the household received since October 1 of the previous year.  To identify households receiving energy assistance, see (HEATSUB).  For information about the form of payment for energy assistance, see (HEATPAY). | - |
| **FOODSTMP** | Food stamp recipiency | FOODSTMP indicates whether one or more members of the household received benefits from the Supplement Nutrition Assistance Program (SNAP) during the prior year. This program is formerly known as the Food Stamps program.

Once such a household was identified, three follow-up questions were asked.  The first question determined the number of current household members covered by Food Stamps during the previous calendar year (STAMPNO).  The second question determined the number of months that Food Stamps were received during the previous year (STAMPMO).  Finally, a last question determined the total face value of Food Stamps received during that period (STAMPVAL).

The Food Stamp Act of 1977 was enacted to increase the food purchasing power of eligible households through the use of coupons to purchase food. The Food and Nutrition Service of the U.S. Department of Agriculture (USDA) administers the Food Stamp Program through State and local welfare offices. The Food Stamp Program is the major national income support program which provides benefits to all low-income and low-resource households, regardless of the person's characteristics (e.g., sex, age, disability, etc.). The Food Stamps program was renamed SNAP as part of the Farm Bill of 2008.

For some variables relating to means-tested government assistance, including FOODSTMP, information was collected only from households whose estimated income fell below a given threshold.  During the first month that a household entered the survey, and one year later, the CPS interviewer asked the respondent to estimate the family's total income in the past twelve months, by choosing one of fourteen broad categories.  Only households in which the household members' combined income fell below a given level (e.g., under 30,000 dollars in the 1980s) were questioned about means-tested program benefits.  Households with estimated incomes above the threshold were presumed to neither qualify for nor receive such benefits, and were not asked these questions, to limit the length of interviews.  Households that were not questioned were coded as "no" for several variables relating to the receipt of means-tested benefits, including FOODSTMP. | - |
| **STAMPNO** | Number of persons covered by food stamps | STAMPNO specifies the number of current household members covered by Food Stamps during the previous calendar year. See also (FOODSTMP). | - |
| **STAMPMO** | Number of months received food stamps | STAMPMO specifies the number of months the household received Food Stamps during the previous calendar year. For information about the Food Stamp program, see (FOODSTMP). | - |
| **STAMPVAL** | Total value of food stamps | STAMPVAL gives the total value of Food Stamps received by the household during the previous calendar year. For discussion of the Food Stamp program and related variables, see (FOODSTMP). 

Inflation-adjusted versions of this variable created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **FAMINC** | Family income of householder | FAMINC reports annual family income, in categories, of all persons related to the head of household/householder. For individuals who are not part of the householder's family, FAMINC reports the value for the householder's family. 

This measure includes the income of all members of the household who are 15 years of age or older.  Income includes money from jobs; net income from business, farm or rent; pensions; dividends; interest; Social Security payments; and any other monetary income received by family members.

Family income is collected as part of the basic monthly survey. At the end of the monthly labor force survey, respondents are asked to choose the category that represents the total combined income during the past 12 months for all members of the householder's family. The questionnaire says that "This includes money from jobs, net income from business, farm or rent, pensions, dividends, interest, social security payments and any other money income received" by members of the householder's family who are 15 years of age or older. Available categories change over time. | - |
| **UNITSSTR** | Units in structure | UNITSSTR reports the number of housing units (both occupied and vacant) in the structure that contained the household.  The survey form included five possible responses: 1, 2, 3-4, 5-9, and 10+.  To increase consistency with the IPUMS-USA variable UNITSSTR, IPUMS-CPS also integrates other information into the UNITSSTR variable.  Housing units described as "mobile home or trailer with no permanent room added" and "tent/trailer site" elsewhere in the original data were coded as "mobile home or trailer" (code 01) and "boat, tent, van, other" (code 02) in the UNITSSTR variable.  These are one-unit structures.  All other one-unit structures are in code 11, "One unit, unspecified type (CPS)." | - |
| **HRHHID** | Household ID, part 1 | HRHHID is part 1 of the CPS household ID on the original files. When combined with HRHHID2, HRHHID can uniquely identify households within basic monthly samples. | - |
| **HRHHID2** | Household ID, part 2 | HRHHID2 is part 2 of the CPS household ID on the original files for all basic monthly samples from May 2004 forward. For January 1994- May 2004, IPUMS created HRHHID2 based on HRSAMPLE, HRSERSUF, and HUHHNUM. | - |
| **PERNUM** | Person number in sample unit | PERNUM numbers all persons within each household consecutively (starting with "1") in the order in which they are listed in the original CPS data.  When combined with YEAR , MONTH, and SERIAL, PERNUM uniquely identifies each person within IPUMS-CPS samples, though not across IPUMS-CPS samples. | - |
| **CPSIDP** | CPSID, person record | CPSIDP is an IPUMS CPS defined variable that uniquely identifies individuals across CPS samples. The first six digits of CPSIDP index the four-digit year and two-digit month that the household was first in the CPS. CPSIDP allows users to link a respondent appearing with a designated household roster line number (LINENO) across samples, based on the 4-8-4 rotation pattern, by assigning a unique CPSIDP value to this line number. CPSIDP will only ever appear for a maximum of 8 times, which is the number of times a household may be observed in the CPS survey (as indexed by MISH). In some cases, individuals will appear fewer than 8 times due to migration, mortality, non-response, and recording errors. Extensive documentation about the creation of CPSIDP is available elsewhere.

To get started using CPSIDP, users may want to sort their data file by CPSIDP and MISH to create a person-time file.

Users should note that it is important to verify CPSIDP linkages with AGE, SEX, and RACE. In some cases CPSIDP will result in erroneous links, which are due to errors in the source data. Cases with the same CPSIDP value may also have inconsistent responses across samples due to errors on the part of the respondent or in recording the response. Ultimately, it is up to the individual researcher to determine the acceptability of the linkages made using CPSIDP. IPUMS CPS also offers CPSIDV which creates linkages across months that have been validated based on demographic characteristics.

CPSIDP may also be used to link ASEC respondents who are in the March Basic Monthly file to other months of CPS data. This linking is made possible by IPUMS through the creation of MARBASECIDP. For further information about the relationship between the March Basic and the ASEC, please see our additional documentation.

Respondents who are part of the ASEC oversample (as indicated by ASECOVERP) may also be linked across ASEC samples, but not to the March or any other Basic Monthly sample. Note also that MISH is not a reliable indicator of rotation pattern status for ASEC oversample records and should not be used to validate matches. For further information on linking records across ASEC samples, please see our additional documentation. | - |
| **CPSIDV** | Validated Longitudinal Identifier | CPSIDV is an IPUMS CPS-created variable that uniquely identifies individuals across CPS samples. In addition to linking records across the CPS 4-8-4 rotation pattern, CPSIDV only makes links between those records whose SEX and RACE values do not change and whose AGE values change in expected ways over time. 

CPSIDV is based on CPSIDP and so there are some structural similarities between them. The first six digits of CPSIDV are identical to CPSIDP - the four-digit year and two-digit month that the household was first in the CPS. Like CPSIDP, CPSIDV allows users to link a respondent appearing with a designated household roster line number (LINENO) across samples, based on the 4-8-4 rotation pattern. 

Only records that link using CPSIDP that also have consistent race and sex values and age values that increase at least one but not more than two years over the course of the 16-month CPS rotation are linkable using CPSIDV. As a result, linkage rates using CPSIDV are slightly lower than those achieved using CPSIDP. However, linkages created with CPSIDV do not require the recommended post-linking verification steps recommended for use with CPSIDP links. Users should note that original, unharmonized values of age, sex, and race are used in the creation of CPSIDV. The procedure and validation criteria for creating CPSIDV are described in detail in A Holistic Approach to Validating Current Population Survey Panel Data. 

To get started using CPSIDV, users may want to sort their data file by CPSIDV and MISH to create a person-time file. 

CPSIDV may also be used to link ASEC respondents across years. This linking is made possible, in part, by IPUMS through the creation of MARBASECIDP. For further information about the relationship between the March Basic and the ASEC, please see our additional documentation. In addition, persons in the ASEC oversample (as indicated by ASECOVERP) can be linked across ASEC samples using CPSIDV. Note however, that ASEC oversample individuals cannot be linked to the March Basic or any other Basic Monthly survey using CPSIDV. Note also that MISH is not a reliable indicator of rotation pattern status for ASEC oversample records and should not be used to validate matches. For further information on linking ASEC oversamples using CPSIDV, please refer to our additional documentation.

Users should take care when including the March Basic or ASEC as part of their linking. Respondents who are part of the ASEC oversample (as indicated by ASECOVERP) have a CPSIDV value of 0. | - |
| **ASECWT** | Annual Social and Economic Supplement Weight | ASECWT is a person-level weight that should be used in analyses of individual-level CPS supplement data. Since the CPS relies on a complex stratified sampling scheme, it is essential to use one of the provided weighting variables.

Researchers should use WTFINL rather than ASECWT when they wish to conduct person-level analyses of non-ASEC data. EARNWT should be used for any analysis including a small number of person-level variables (EARNWEEK, HOURWAGE, PAIDHOUR, and UNION). Researchers should use ASECWTH for household-level analyses. ASECWTCVD is available for the 2020 ASEC to adjust for nonrandom nonresponse resulting from the COVID-19 pandemic.

User Caution: For analyses that include the 2014 ASEC sample, please see the comparability tab.

The ASEC CPS files include two groups of people who are not included in the production of published labor force statistics: (1) members of the armed services, and (2) members of the Hispanic oversample who were interviewed in months other than March. WTFINL and EARNWT assign these groups a value of 0. Both groups are assigned non-zero values in ASECWT.

ASECWT is based on the inverse probability of selection into the sample and adjustments for the following factors: failure to obtain an interview; sampling within large sample units; the known distribution of the entire population according to age, sex, and race; over-sampling Hispanic persons; to give husbands and wives the same weight; and an additional step to provide consistency with labor force estimates from the basic survey. 

Estimates on the entire population are prepared by projecting forward the resident population from the last available census. These projections are derived by updating the demographic census data from a number of other data sources that account for death, births and net migration. About 3 years after every census (i.e. 2003 for the 2000 Census and 2013 for the 2010 Census), the Census Bureau updates its independent population control and provides a new weight for the relevant years.

Two important points should be noted here. First, the lag between when the Census is conducted and when the CPS weights are updated is about 3 years. While the Census data are being processed, the CPS files are made available using the weighting scheme from the US Census prior to the latest Census. Second, once the files are updated, the old weights become obsolete and are replaced in the IPUMS data extract system. Published estimates from the lag years that use the old weights are not always updated. For example, 2010 poverty estimates were released in ASEC using the 2000 population controls. Once the 2010 population controls were made available, IPUMS-CPS replaced the ASEC 2010, 2011, and 2012 weights that are based on the 2000 population control with weights that are based on the 2010 population controls. IPUMS-CPS makes available only the most up-to-date weights. | - |
| **RELATE** | Relationship to household head | RELATE reports an individual's relationship to the head of household or householder.

CPS interviewers collected detailed information about the precise relationships of all persons in the household in their initial listing of household members.  Unfortunately, they then simplified the detailed data (e.g., daughter-in-law, lodger's brother) by coding it into a few broad categories (e.g., "other relative of head," "nonrelative of head with own relatives in household") specified on the interview form.  Only the broad categories are preserved in the data.  The 4-digit codes for RELATE are consistent with the coding scheme used in IPUMS-USA census data. | - |
| **AGE** | Age | Age gives each person's age at last birthday. | - |
| **SEX** | Sex | SEX gives each person's sex. | - |
| **RACE** | Race | Racial categories in the CPS have been more consistent than racial categories in the census.  Up through 2002, the number of race categories ranged from 3 (white, negro, and other) to 5 (white, black, American Indian/Eskimo/Aleut, Asian or Pacific Islander, and other).   Beginning in 2003, respondents could report more than one race, and the number of codes rose to 21, and then up to 26 codes in 2013. | - |
| **MARST** | Marital status | MARST gives each person's current marital status, including whether the spouse was currently living in the same household. | - |
| **POPSTAT** | Adult civilian, armed forces, or child | POPSTAT reports the person's status in the population -- whether the person is an adult civilian, member of the U. S. armed forces, or a child.

The CPS is, in large part, a labor market survey, and is used to measure unemployment among the civilian labor force.  (The U.S. unemployment rate reported by the Bureau of Labor Statistics excludes members of the armed forces.)   Children (for ASEC samples under age 14 through 1979 and under age 15 beginning in 1980; for non-ASEC samples under 14 through February, 1989 and under 15 beginning March 1989) were not asked questions pertaining to economic activity.  Members of the armed forces were asked only a small number of questions relating to demographic facts, migration, and income during the previous calendar year.  POPSTAT provides a useful "filter" variable for excluding persons who had no responses for many of the survey questions.  If children and/or members of the armed forces were excluded from the universe of a particular question, they appear only in the "not in universe" category of a variable. | - |
| **ASIAN** | Asian subgroup | In 2013, the Census Bureau introduced a question about Asian subgroups of national origin within Asia for respondents who responded as Asian Only for RACE. Those that are multiple Asian races are identified as Other Asian. | - |
| **VETSTAT** | Veteran status | VETSTAT is a dichotomous variable identifying veterans, that is, persons who served in the military forces of the United States (Army, Navy, Air Force, Marine Corps, or Coast Guard) in time of war or peace, but who were not in the armed forces at the time of the survey.  

Information on the most recent period of service for veterans is given in the VETLAST variable.  Data are not available for 1966.  Beginning in 2006, veterans could report up to four periods of service.  While the most recent period of service is included in VETLAST variable (comparable over time), the four variables: VET1, VET2, VET3, and VET4 are also available for the four period of service for veterans. | - |
| **OCCLY** | Occupation last year | OCCLY reports the person's primary occupation during the previous calendar year.  A respondent who held more than one job during the preceding year was to report the job that lasted longest. The reference period for OCCLY, the preceding calendar year, is the same as the reference period for income variables in IPUMS-CPS.

The CPS interviewer collected information by asking what kind of work the person was doing during the preceding calendar year, and Census Bureau staff coded the information into the CPS or census occupational classification. Researchers who wish to work with a consistent occupational coding scheme for 1968 forward should use the OCC50LY variable.  

The occupation of persons employed at the time of the survey is reported in OCC.  OCC also provides information about the most recent job for persons not in the labor force at the time of the survey.  For general discussion of employment concepts, including the definition of those not in the labor force, see the documentation on EMPSTAT.    

The 1962 sample is unavailable due to a shared code (0) between ' medical and other health workers' and 'not in universe'. However, the unharmonized variable (OCCLYR) is provided for users who wish to analyze the data independently. | - |
| **OCC50LY** | Occupation last year, 1950 basis | OCC50LY recodes information contained in the variable OCCLY into the 1950 Census Bureau occupational classification system.  OCC50LY provides consistent occupational codes for the jobs respondents reported working during the previous calendar year, for 1968 forward.  Information on occupation during the previous year is given as it appeared in the original survey data in OCCLY.  For both OCCLY and OCC50LY, respondents were to report the jobs they held for the longest time during the previous year.  

The occupations of persons employed at the time of the survey is reported in OCC, and this information is recoded into the consistent 1950 occupational classification system in OCC1950.  OCC and OCC1950 also provide information about the most recent jobs of persons not employed at the time of the survey. | - |
| **INDLY** | Industry last year | INDLY reports the industry in which the respondent worked during the previous calendar year.  A respondent who held more than one job during the preceding year was to report the job that lasted longest.   The reference period for INDLY, the preceding calendar year, is the same as the reference period for income variables in IPUMS-CPS.

The CPS interviewer collected information by asking what kind of work the person was doing last year, and Census Bureau staff coded the information into the CPS or census industrial classification.  Researchers who wish to work with a consistent occupational coding scheme for 1968-2002 should use the IND50LY variable.  

The industry of persons employed at the time of the survey is reported in IND.  IND also provides information about the most recent job for persons not in the labor force at the time of the survey.  For general discussion of employment concepts, including the definition of those not in the labor force, see the documentation on EMPSTAT.    

The 1962 sample is unavailable due to a shared code (0) between 'agriculture' and 'not in universe'. However, the unharmonized variable (INDLYR) is provided for users who wish to analyze the data independently. | - |
| **IND50LY** | Industry last year, 1950 basis | IND50LY recodes information contained in the variable INDLY into the 1950 Census Bureau industrial classification system.  IND50LY provides consistent occupational codes for the jobs respondents reported working during the previous calendar year, for 1968 on.  Information on industry during the previous year is given as it appeared in the original survey data in INDLY.  For both INDLY and IND50LY, respondents were to report the jobs they held for the longest time during the previous year.  

The industry of persons employed at the time of the survey is reported in IND, and this information is recoded into the consistent 1950 industrial classification system in IND1950.  IND and IND1950 also provide information about the most recent jobs of persons not employed at the time of the survey. | - |
| **OCC90LY** | Occupation last year, 1990 basis | OCC90LY recodes information contained in the variable OCCLY into the 1990 Census Bureau occupational classification system.  OCC90LY provides consistent occupational codes for the jobs respondents reported working during the previous calendar year, for 1968 forward.  Information on occupation during the previous year is given as it appeared in the original survey data in OCCLY.  For both OCCLY and OCC90LY, respondents were to report the jobs they held for the longest time during the previous year.  

The occupations of persons employed at the time of the survey is reported in OCC, and this information is recoded into the consistent 1990 occupational classification system in OCC1990.  OCC and OCC1990 also provide information about the most recent jobs of persons not employed at the time of the survey. | - |
| **IND90LY** | Industry last year, 1990 basis | IND90LY recodes information contained in the variable INDLY into the 1990 Census Bureau industrial classification system.  IND90LY provides consistent occupational codes for the jobs respondents reported working during the previous calendar year, for 1968 on.  Information on industry during the previous year is given as it appeared in the original survey data in INDLY.  For both INDLY and IND90LY, respondents were to report the jobs they held for the longest time during the previous year.  

The industry of persons employed at the time of the survey is reported in IND, and this information is recoded into the consistent 1990 industrial classification system in IND1990.  IND and IND1990 also provide information about the most recent jobs of persons not employed at the time of the survey. | - |
| **OCC10LY** | Occupation last year, 2010 basis | OCC10LY recodes information contained in the variable OCCLY into the 2010 Census Bureau occupational classification system.  OCC10LY provides consistent occupational codes for the jobs respondents reported working during the previous calendar year, for 1968 forward.  Information on occupation during the previous year is given as it appeared in the original survey data in OCCLY.  For both OCCLY and OCC10LY, respondents were to report the jobs they held for the longest time during the previous year.  

The occupations of persons employed at the time of the survey is reported in OCC, and this information is recoded into the consistent 2010 occupational classification system in OCC2010.  OCC and OCC2010 also provide information about the most recent jobs of persons not employed at the time of the survey. | - |
| **CLASSWLY** | Class of worker last year | CLASSWLY specifies whether a person who worked during the previous calendar year was self-employed, an employee in private industry or the public sector, in the armed forces, or worked without pay in a family business or farm.  Respondents were classified by the job that they held for the longest time during the previous year.  More specific information about an individual's job during this period is given in OCCLY, OCC50LY, INDLY, and IND50LY.  

CLASSWKR relates to the respondent's job during the previous week, rather than the previous year.  CLASSWKR also reports the most recent job for respondents who were not employed in the week prior to the survey. | - |
| **WORKLY** | Worked last year | WORKLY indicates whether or not the respondent worked any time in the calendar year previous to the survey year.  For example, if the respondent is interviewed in March of 2015, they are reporting whether they had worked any time in 2014. | - |
| **WKSWORK1** | Weeks worked last year | WKSWORK1 reports the number of weeks, in single weeks, that the respondent worked for profit, pay, or as an unpaid family worker during the preceding calendar year.  Respondents were prompted to count weeks in which they worked for even a few hours and to include paid vacation and sick leave as work.  Information on weeks worked during the preceding year is available in the form of intervals for 1962 forward in the WKSWORK2 variable. | - |
| **WKSWORK2** | Weeks worked last year, intervalled | WKSWORK2, like WKSWORK1, reports the number of weeks that the respondent worked for profit, pay, or as an unpaid family worker during the preceding calendar year.  It differs from WKSWORK1 in that responses are given in intervals: 1-13 weeks; 14-26 weeks; 27-39 weeks; 40-47 weeks; 48-49 weeks; and 50-52 weeks.  Respondents were prompted to include weeks in which they worked for even a few hours and to include paid vacation and sick leave as work. | - |
| **UHRSWORKLY** | Usual hours worked per week (last yr) | UHRSWORKLY reports the number of hours per week that respondents usually worked if they worked during the previous calendar year.  Individuals were asked this question if: 1) they reported working at a job or business at any time during the previous year or 2) they acknowledged doing "any temporary, part-time, or seasonal work even for a few days" during the previous year.  

See the Hours Worked Variables Notes for an overview of the different actual and usual hours worked variables available. | - |
| **WKSUNEM1** | Weeks unemployed last year | WKSUNEM1 gives the number of weeks, in single weeks, that the respondent looked for work or was on layoff during the preceding calendar year. | - |
| **WKSUNEM2** | Weeks unemployed last year, intervalled | WKSUNEM2 gives the number of weeks, in intervals, during which the respondent looked for during the preceding calendar year. In years after 1976, those on layoff are also included in this variable.  Information on weeks of unemployment during the preceding year is available in single weeks, beginning in 1976, in the variable WKSUNEM1. | - |
| **FULLPART** | Worked full or part time last year | FULLPART indicates whether respondents who were employed during the previous calendar year worked full-time or part-time.  Full-time work is defined as thirty-five hours a week or more.   Beginning in 1976, more detailed information on hours worked during the previous year is available in UHRSWORKLY. | - |
| **WKXPNS** | Work expenses | WKXPNS reports the annual expenses associated with going to work and earning a wage. This variable is imputed by the Census Bureau with data from the Survey of Income and Program Participation (SIPP) which collects information on work expenses. Specifically, the Census Bureau uses 85 percent of the median weekly expenses for anyone over 18 in the SIPP and multiplies this fixed dollar amount by the number of weeks respondents reported working in the year in the CPS (WKSWORK1).

Additionally, WKXPNS is capped at a person's total yearly earnings. For example, if a person reported working 52 weeks in the past year and earned less than the maximum value of WKXPNS, their value of WKXPNS will be equal to their total yearly earnings. 

Additional information about work-related expenses and the calculation of median work expenses from the SIPP can be found in this paper.

Amounts are expressed as they were calculated in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **NWLOOKWK** | Weeks looked for work last year (didn't work) | For civilian adults who did not work during the preceding calendar year, NWLOOK reports the number of weeks such persons spent looking for work or on layoff. 

After ascertaining that the individual did not work, even for a few days, during the previous calendar year, the interviewer asked, "Even though you did not work in [year], did you spend any time trying to find a job or on layoff?"  If the answer was yes, the interviewer asked, "How many different weeks were you looking for work or on layoff?"   Responses to this second question are recorded in NWLOOKWK.  A code of "00" indicates that the individual did not work during the preceding calendar year and spent no weeks looking for work or on layoff during this period. | - |
| **PENSION** | Pension plan at work | PENSION indicates whether the respondent's union or employer for his or her longest job during the preceding calendar year had a pension or other retirement plan for any of the employees, and, if so, whether the respondent was included in that plan.  The question specifically excluded retirement support from Social Security. | - |
| **FIRMSIZE** | Number of employees | FIRMSIZE indicates the total number of persons who worked for the respondent's employer during the preceding calendar year, counting all locations where the employer operated.  If the individual was self-employed in a business or farm, the response to FIRMSIZE indicates how many employees worked for the respondent.   Responses were grouped into broad categories, such as "under 25 employees," "25 to 99 employees," "100 to 499 employees," "500 to 999 employees," and "1000+ employees." | - |
| **WANTJOB** | Want regular job now | WANTJOB reports whether respondents not in the labor force (neither working, nor temporarily absent from a job, nor actively looking for work) wanted a job, either full- or part-time. | - |
| **WHYPTLY** | Reason for working part-time last year | WHYPTLY reports the reason why respondents worked part-time (less than 35 hours) for at least one week during the previous calendar year.   Some of these individuals normally worked a part-time job; others usually worked full-time but worked less than 35 hours for some weeks (e.g., because of slack work or a shortage of materials).   Paid time off due to vacations, holidays, or sick leave did not count. | - |
| **USFTPTLW** | Usually work full time (part time last week) | USFTPTLW reports whether persons who worked part-time (less than 35 hours) during the preceding week usually worked full-time (35 hours or more). | - |
| **PAYIFABS** | Paid if absent from work last week | PAYIFABS reports whether respondents received wages or salary for the time that they were absent from work during the preceding week. | - |
| **NUMEMPS** | Number of employers last year | NUMEMPS reports whether respondents had one, two, or three or more employers during the previous calendar year.  If individuals worked more for more than one employer simultaneously, they were to count this as only one employer.  NUMEMPS is thus an indicator of job changes across employers over one year, rather than of multiple jobholding at one point in time. | - |
| **WNLWNILF** | When last worked for pay (NILF last week) | For individuals not currently in the labor force (neither working nor temporarily absent from a job nor actively looking for work), WNLWNILF reports the amount of time that had passed since such persons last worked at a job or business. | - |
| **STRECHLK** | Stretches of looking for work last year | STRCHLK reports whether the weeks that part-year workers spent looking for work or on layoff during the previous calendar year were "all in one stretch" or "in more than one stretch" (for 1962-1967) or occurred in one stretch, two stretches, or three or more stretches (for 1968 onward). | - |
| **WHYNWLY** | Reason not working last year | WHYNWLY reports the main reason given for not working at all during the previous calendar year. | - |
| **ACTNLFLY** | Activity when not in labor force last year (part-year workers) | For the period prior to 1976, ACTNLFLY reports respondents' main activity when they were not working during the previous calendar year.  For 1976 on, ACTNLFLY reports respondents' main activity when they were not in the labor force (neither working nor looking for work nor on layoff from a job) during the previous calendar year.  Only persons who were working part of the year (from 1-49 weeks) were asked this question about what they were doing during most of the remaining weeks. | - |
| **PTWEEKS** | Weeks working part time last year | PTWEEKS reports the number of weeks that respondents worked part-time (less than 35 hours) during the preceding calendar year.   It includes both employed persons whose usual number of working hours per week was less than 35 hours and those who usually worked full-time but who acknowledged working less than 35 hours during at least one week.  Work weeks that were shortened due to time off with pay because of holidays, vacation days, or sickness were not to be counted. | - |
| **FTOTVAL** | Total family income | FTOTVAL reports the total income for the respondent's family. Amounts are expressed as they were reported to the interviewer (i.e., in the survey year's dollar amounts). Users may want to adjust for inflation using Consumer Price Index adjustment factors. (FTOTVAL relies on Census-defined families. For more on Census families see FTYPE and FAMREL. This is a different definition from IPUMS-derived families as in FAMUNIT). | - |
| **INCTOT** | Total personal income | INCTOT indicates each respondent's total pre-tax personal income or losses from all sources for the previous calendar year.  Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. | - |
| **INCWAGE** | Wage and salary income | INCWAGE indicates each respondent's total pre-tax wage and salary income--that is, money received as an employee--for the previous calendar year.  

For ASEC samples 1988-onward, INCWAGE is derived from a Census recode variable.  The topcoded components of INCWAGE are OINCWAGE and INCLONGJ.  OINCWAGE  is always a component of INCWAGE.  When SRCEARN indicates that INCLONGJ is earned from wage and salary, INCLONGJ is an additional component of INCWAGE.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCBUS** | Non-farm business income | INCBUS indicates each respondent's net pre-income-tax non-farm business and/or professional practice income for the previous calendar year.  INCBUS is reported for self-employed persons; employees' earnings are given in INCWAGE.   

For ASEC samples 1988-onward, INCBUS is derived from a Census recode variable.  The topcoded components of INCBUS are OINCBUS and INCLONGJ.  OINCBUS  is always a component of INCBUS.  When SRCEARN indicates that INCLONGJ is earned from self-employment, INCLONGJ is an additional component of INCBUS.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCFARM** | Farm income | INCFARM indicates each respondent's net pre-income-tax earnings as a tenant farmer, sharecropper, or operator of his or her own farm during the previous calendar year.  INCFARM collects income information for self-employed persons who had their own farms.  Income earned as an employee on a farm is contained in the variable INCWAGE.  

For ASEC samples 1988-onward, INCFARM is derived from a Census recode variable.  The topcoded components of INCFARM are OINCFARM and INCLONGJ.  OINCFARM  is always a component of INCFARM.  When SRCEARN indicates that INCLONGJ is earned from farm self-employment, INCLONGJ is an additional component of INCFARM.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCSS** | Social Security income | INCSS indicates how much pre-tax income (if any) the respondent received from Social Security or U.S. government Railroad Retirement insurance payments (for 1968-1979) or from Social Security payments exclusively (1980 forward).  

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. | - |
| **INCWELFR** | Welfare (public assistance) income | INCWELFR indicates how much pre-tax income (if any) the respondent received during the previous calendar year from various public assistance programs commonly referred to as "welfare."

Totals are given as they were reported to CPS interviewers; users must adjust for the effects of inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCRETIR** | Retirement income | INCRETIR indicates how much pre-tax income (if any) the respondent received from all retirement income sources during the past year. Pension or retirement income from a previous employer or union, or from other retirement income (excluding Social Security and Veterans' Administration payments) are included as sources prior to 2019. During this period, the survey questionnaire listed the following types of retirement income: company or union pension, including profit sharing; annuities; U.S. military retirement; federal government employee pensions; state or local government employee pensions; U.S. Railroad Retirement; regular payments from annuities or paid-up insurance policies; and other sources such as IRA or KEOUGH accounts. 

Beginning in 2019, income from retirement accounts, pension plans, and annuities are split into separate variables. INCRETIR includes only income from retirement accounts, and not pension plans or annuities. Retirement account income from 401k, 403b, Roth IRA, regular IRA, KEOGH, and Simplified Employee Pension (SEP) plans are included.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCSSI** | Income from SSI | INCSSI indicates how much pre-tax income (if any) the respondent received from Supplemental Security Income (SSI) during the previous calendar year.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. | - |
| **INCINT** | Income from interest | INCINT indicates how much pre-tax income (if any) the respondent received from  interest on saving accounts, certificates of deposit, money market funds, bonds, treasury notes, IRAs, and/or other investments which paid interest.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCUNEMP** | Income from unemployment benefits | INCUNEMP indicates how much pre-tax income (if any) the respondent received from state or federal unemployment compensation, Supplemental Unemployment Benefits (SUB), or union unemployment or strike benefits during the previous calendar year.  

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCWKCOM** | Income from worker's compensation | INCWKCOM indicates how much pre-tax income (if any) the respondent received from worker's compensation payments or other payments as a result as a job-related injury or illness.  Income from sick pay and disability retirement were not counted as income under INCWKCOM.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. | - |
| **INCVET** | Income from veteran's benefits | INCVET indicates how much pre-tax income (if any) the respondent received from payments from the Veterans' Administration (VA) during the previous calendar year.  Such payments could include service-related disability compensation, survivor benefits, pension, educational allowance, or other veteran payments.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. | - |
| **INCSURV** | Income from survivor's benefits | INCSURV indicates how much pre-tax income (if any) the respondent received from survivors' benefits during the previous calendar year.  Such payments could include the following: company or union survivor pension; federal government civil service pension; U.S. military retirement survivor pension; state or local government survivor pension; worker's compensation survivor pension; black lung survivor pension; regular payments from an estate or trust; and regular payments from annuities or paid-up insurance policies.  Social Security and Veterans' Administration payments were specifically excluded from this category; payments from these sources are given in INCSS and INCVET, respectively.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCDISAB** | Income from disability benefits | INCDISAB indicates how much pre-tax income (if any) the respondent received from disability income during the previous calendar year.   

CPS interviewers asked about income as a result of disability only if at least one member of the household had "a health condition or disability which prevents them from working or which limits the kind or amount of work they can do" or had "ever retired or left a job for health reasons."  If the answer was affirmative, the interviewer asked which household member (or members) had such a health condition and whether this person received income as a result of this health condition, disability, or handicap.

Income due to disability could come from the following sources: worker's compensation; company or union disability; federal government civil service disability; U.S. military retirement disability; state or local government employee disability; U.S. Railroad Retirement disability; accident or disability insurance; black lung miner's disability; or state temporary sickness payments. Income from Social Security and payments from the Veterans' Administration were not included in INCDISAB; such payments were included in INCSS and INCVET, respectively.  

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCDIVID** | Income from dividends | INCDIVID indicates how much pre-tax income (if any) the respondent received from stocks and mutual funds during the previous calendar year.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCRENT** | Income from rent | INCRENT indicates how much pre-tax income (if any) the respondent received from rent (after expenses), from charges to roomers or boarders, and from money paid by estates, trusts, and royalties, during the previous calendar year.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCEDUC** | Income from educational assistance | INCEDUC indicates how much pre-tax income (if any) the respondent received from educational assistance during the previous calendar year.  This variable relates to education beyond the high school level, including college, university, or vocational, business, or trade school.  The financial aid could cover tuition, fees, books, or living expenses while attending school.  

Educational assistance includes Pell Grants or other aid from government sources, non-governmental scholarships and grants, and financial assistance from employers or friends (excluding household members).  Educational benefits from the Veteran's Administration are included in INCVET rather than INCEDUC.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCCHILD** | Income from child support | INCCHILD indicates how much pre-tax income (if any) the respondent received from child support payments during the previous calendar year. 

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCASIST** | Income from assistance | INCASIST indicates how much pre-tax income (if any) the respondent received during the previous calendar year from regular financial assistance from friends or relatives not living in the same household. 

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. | - |
| **INCOTHER** | Income from other Source not specified | INCOTHER is a residual category for pre-tax income for the previous calendar year that was not reported in other, more specific, income variables.  Small amounts of income from hobbies, severance pay, and foster child care payments are included in INCOTHER, as is any income that respondents failed to report earlier in the interview.  

INCOTHER covers income not captured in the variables INCWAGE, INCBUS, INCFARM, INCSS, INCWELFR, INCRETIR, INCSSI, INCINT, INCUNEMP, INCWKCOM, INCVET, INCSURV, INCDISAB, INCRENT, INCDIVID, INCEDUC, INCCHILD, INCALIM, and INCASIST.

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. | - |
| **INCRANN** | Retirement income from annuities | INCRANN reports the amount of retirement income from annuities respondents received during the previous calendar year. 

Prior to 2019, retirement income from annuities was reported in INCRETI1 or INCRETI2 for those who reported annuities as a source of retirement income in SRCRETI1 and SRCRETI2, respectively. | - |
| **INCPENS** | Pension income | INCPENS reports the total amount of pension income the respondent received during the previous calendar year from all sources. These source are identified in SRCPEN1 and SRCPEN2.  Amounts received from these individual sources are found in INCPEN1 and INCPEN2. | - |
| **INCLONGJ** | Earnings from longest job | INCLONGJ reports the net amount (prior to deductions) that the respondent earned from the job held for the longest time during the preceding calendar year.  Whether such income derived from wages or salary or from self-employment in a business or farm is specified in SRCEARN.

Most income variables included in IPUMS-CPS report the total amount earned from a specific source (e.g., wages and salary) during the preceding calendar year.  INCLONGJ, by contrast, does not necessarily include income earned during the entire calendar year.  Imagine that an individual worked at one job for eight months, earning $10,000 in wages, and then worked for four months at two different jobs, earning an additional $5000 in wages.  Wages from the longest-held job (in this case, $10,000) would be reported in INCLONGJ.  Wage and salary income from the two jobs other than the longest-held job (in this case, $5,000) would be reported in OINCWAGE. Total earnings from wages for this person (in this case, $15,000, accrued in three different jobs) would be reported in INCWAGE.  If, however, a wage-earner worked at a single job during the preceding calendar year, the amounts reported in INCLONGJ and INCWAGE would be the same. 

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors. 

Values may be negative. | - |
| **OINCBUS** | Earnings from other work included business self-employment earnings | OINCBUS reports net earnings from self-employment in a non-farm business, if this self-employment did not constitute the respondent's longest-held job during the previous calendar year.  The amount earned (in wages, salary, or earnings from self-employment in a business or farm) from the longest-held job during the preceding calendar year is reported in INCLONGJ.     

Imagine that a self-employed individual worked in one non-farm own business for eight months, netting $10,000 in earnings, and worked in two other non-farm own businesses for the remaining 4 months, netting an additional $12,000 in earnings.  The $12,000 in "other" net self-employment earnings (from work outside the person's primary, or longest-held, job) would be reported in OINCBUS; the $10,000 in net earnings from the individual's longest-held job would be reported in INCLONGJ; and the total amount of net self-employed non-farm business earnings from the previous calendar year ($22,000) would be reported in INCBUS.  

Imagine, instead, that as reported in SRCEARN, an individual worked as an employee earning wages for the primary job, but earned additional income working part of the year in their own non-farm businesses.  In such a case, wage income from the primary job would be reported in INCLONGJ; all self-employed non-farm net business earnings would be reported in OINCBUS; and the value of OINCBUS and INCBUS would be the same.   

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **OINCFARM** | Earnings from other work included farm self-employment earnings | OINCFARM reports net earnings as a tenant farmer, sharecropper, or operator of one's own farm during the previous calendar year, if such work did not constitute the longest-held job during that period.  The amount earned (in wages, salary, or earnings from self-employment in a business or farm) from the longest-held job during the preceding calendar year is reported in INCLONGJ.     

Imagine that an individual considered raising crops on her own land to be her primary job, and considered money earned by harvesting crops on another farmer's land for a few days, using her own equipment, to be a secondary "own farm" job.  In such a case, net earnings from the sale of  her own crops would be reported as income in INCLONGJ; earnings from harvesting crops for another farmer would be reported as "other" self-employed own farm income in OINCFARM; and the sum of earnings from crop sales and farm equipment rental would constitute INCFARM.  If, instead, she grouped together all net earnings from crop sales and income generated from the use of her equipment into a single "own farm" business, all of this net farm income would be reported in both INCLONGJ and INCFARM, and the value of OINCFARM would be zero.  

Imagine, instead, that as reported in SRCEARN, an individual worked as an employee earning wages for the primary job, but earned additional income working part of the year on their own farm.  In such a case, wage income from the primary job would be reported in INCLONGJ; all self-employed farm net business earnings would be reported in OINCFARM; and the value of OINCFARM and INCFARM would be the same.   

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **OINCWAGE** | Earnings from other work included wage and salary earnings | OINCWAGE reports the net amount (prior to deductions) that the respondent earned in wages and salary, other than the amount earned in the primary (longest-held) job, during the preceding calendar year.  The amount earned (in wages, salary, or earnings from self-employment in a business or farm) from the longest held job during the preceding calendar year is reported in INCLONGJ.

Imagine that an individual worked at one job for 8 months, earning $10,000 in wages, and worked at two other jobs for the remaining 4 months, earning $12,000 in wages.  The $12,000 in "other" wage and salary earnings (wages and salary from jobs other than the person's primary, or longest-held, job) would be reported in OINCWAGE; the $10,000 in wages from the individual's longest-held job would be reported in INCLONGJ; and the total amount of wage and salary income from the previous calendar year ($22,000) would be reported in INCWAGE.

Imagine, instead, that as reported in SRCEARN, an individual was self-employed in a business or farm for their primary job, and also worked one or more additional jobs for wages. In such a case, self-employment income from the primary job would be reported in INCLONGJ; all wage and salary earnings would be reported in OINCWAGE, and the value of OINCWAGE and INCWAGE would be the same.  

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **SRCSURV1** | First source of survivor benefits | SRCSURV1 reports the first source of survivor benefits identified by respondents who reported receiving income from survivor benefits (e.g., from widow's pensions, estates, trusts, annuities, or other survivor benefits except Social Security and VA benefits) during the previous calendar year.  If the individual received survivor benefits from more than one source, the second source of survivor benefits is reported in SRCSURV2. | - |
| **SRCSURV2** | Second source of survivor benefits | SRCSURV2 reports the second source of survivor benefits identified by respondents who answered reported receiving income from survivor benefits (e.g., from widow's pensions, estates, trusts, annuities, or other survivor benefits except Social Security and VA benefits) during the previous calendar year.  The first source of survivor benefits is reported in SRCSURV1.  Individuals who received survivor benefits from only one source are coded as Not in Universe (code 00) in SRCSURV2. | - |
| **INCSURV1** | Survivor benefits income from first source | INCSURV1 reports the amount of income from survivor benefits received by a respondent during the previous calendar year, from the source identified in SRCSURV1.  For example, if the source of payments identified in SRCSURV1 were "company or union pension" (code 01), then INCSURV1 would report the amount of income received from survivor benefits from a company or union pension during the previous calendar year.  For persons who reported receiving survivor benefits from a second source in SRCSURV2, INCSURV2 similarly reports the amount of income from survivor benefits received from that second source during the previous calendar year.   

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCSURV2** | Survivor benefits income from second source | INCSURV2 reports the amount of income from survivor benefits received by a respondent during the previous calendar year, from the source identified in SRCSURV2.  For example, if the source of payments identified in SRCSURV2 were "company or union pension" (code 01), then INCSURV2 would report the amount of income received from survivor benefits from a company or union pension during the previous calendar year.  

The first source of survivor benefits reported by an individual is identified in SRCSURV1, and the amount of income from that first source is reported in INCSURV1.  If individuals reported only one source of income from survivor benefits (and received a code of 00 in SRCSURV2), then the INCSURV2 has a value of 99999999 (indicating no income from a second source of survivor benefits).   

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **SRCDISA1** | First source of disability income | SRCDISA1 reports the first source of disability payments identified by respondents who acknowledged receiving income (other than Social Security or VA benefits) during the previous calendar year as a result of a health problem, disability, or handicap.  If the individual received disability income from more than one source, the second source of disability payments is reported in SRCDISA2. | - |
| **SRCDISA2** | Second source of disability income | SRCDISA2 reports the second source of disability payments identified by respondents who acknowledged receiving income (other than Social Security or VA benefits) during the previous calendar year as a result of health problem, disability, or handicap.  The first source of disability payments is reported in SRCDISA1.  Individuals who received disability payments from only one source are coded as Not in Universe (code 00) in SRCDISA2. | - |
| **INCDISA1** | Disability income from first source | INCDISA1 reports the amount of disability income (payments from sources other than Social Security and VA payments and due to health problems) received by respondents during the previous calendar year, from the source identified in SRCDISA1.  For example, if the source of payments identified in SRCDISA1 were "company or union disability" (code 02), then INCDISA1 would report the amount of income received from company or union disability payments during the previous calendar year.  For persons who reported receiving disability payments from a second source in SRCDISA2, INCDISA2 similarly reports the amount of disability income received from that second source during the previous calendar year.   

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCDISA2** | Disability income from second source | INCDISA2 reports the amount of disability income (payments from sources other than Social Security and VA payments and due to health problems) received by respondents during the previous calendar year, from the source identified in SRCDISA2.  For example, if the source of payments identified in SRCDISA2 were "company or union disability" (code 02), then INCDISA2 would report the amount of income received from company or union disability payments during the previous calendar year.  

The first source of disability income reported by an individual is identified in SRCDISA1, and the amount of income from that first source is reported in INCDISA1.  If individuals reported only one source of disability income (and received a code of 00 in SRCDISA2) then the INCDISA2 variable has a value of 99999 (indicating no disability income from a second source).    

Amounts are expressed as they were reported to the interviewer; users must adjust for inflation using Consumer Price Index adjustment factors or the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **SRCRET1** | First source of retirement income | SRCRET1 reports the first source of retirement income identified by respondents who reported having any retirement accounts during the previous year. The second source of retirement income is reported in SRCRET2. | - |
| **SRCRET2** | Second source of retirement income | SRCRET2 reports the second source of retirement income identified by respondents who reported having any retirement accounts during the previous year. The first source of retirement income is reported in SRCRET1. | - |
| **INCRET1** | Retirement income from first source | INCRET1 reports the amount of retirement income received by respondents during the previous calendar year, from the source identified in SRCRET1.  For example, if the source of payments identified in SRCRET1 were "401k account" (code 1), then INCRET1 would report the amount of income received from that 401k account during the previous calendar year.  For those persons who reported receiving retirement income from a second source in SRCRET2, INCRET2 similarly reports the amount of retirement income received from that second source during the previous calendar year.   
Amounts are expressed as they were reported/calculated in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCRET2** | Retirement income from second source | INCRET2 reports the amount of retirement income received by respondents during the previous calendar year, from the source identified in SRCRET2.  For example, if the source of payments identified in SRCRET2 were "401k account" (code 1), then INCRET2 would report the amount of income received from that 401k account during the previous calendar year.  The respondent's first source of retirement income is reported in SRCRET1, INCRET1 similarly reports the amount of retirement income received from that second source during the previous calendar year.   

Amounts are expressed as they were reported/calculated in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **SRCPEN1** | First source of pension income | SRCPEN1 reports the first source of pension income identified by respondents who reported having any retirement accounts during the previous year. The second source of pension income is reported in SRCPEN2. | - |
| **SRCPEN2** | Second source of pension income | SRCPEN2 reports the second source of pension income identified by respondents who reported having any retirement accounts during the previous year. The first source of pension income is reported in SRCPEN1. | - |
| **INCPEN1** | Pension income from first source | INCPEN1 reports the amount of pension income received by respondents during the previous calendar year, from the source identified in SRCPEN1.  For example, if the source of payments identified in SRCPEN1 were "Company pension" (code 1), then INCPEN1 would report the amount of income received from that 401k account during the previous calendar year.  For those persons who reported receiving pension income from a second source in SRCPEN2, INCPEN2 similarly reports the amount of pension income received from that second source during the previous calendar year.   
Amounts are expressed as they were reported/calculated in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCPEN2** | Pension income from second source | INCPEN2 reports the amount of pension income received by respondents during the previous calendar year, from the source identified in SRCPEN2.  For example, if the source of payments identified in SRCPEN2 were "Company pension" (code 1), then INCPEN2 would report the amount of income received from that company pension during the previous calendar year.  The respondent's first source of pension income is reported in SRCPEN1, INCPEN1 similarly reports the amount of pension income received from that second source during the previous calendar year.   
Amounts are expressed as they were reported/calculated in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **RETCONT** | Contribution to a retirement account last year | For respondents who report having a retirement account in the previous year, RETCONT indicates how much money the respondent contributed to this account. Respondents are instructed not to include money that was reinvested from other retirement accounts.
Amounts are expressed as they were reported in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **SRCRINT1** | First source of interest income from a retirement account. | For respondents that earned interest or dividends from a retirement account during the past year, SRCRINT1 reports the type of retirement account that earned that interest. If the respondent reported a second source of interest or dividend retirement income during the past year, SRCRINT2 reports the type of retirement account. | - |
| **SRCRINT2** | Second source of interest income from a retirement account. | SRCRINT2 reports the second type of retirement account that earned that interest during the past year. SRCRINT1 reports the first source of interest or dividend income from a retirement account. | - |
| **INCRINT1** | Interest income from a retirement account from first source | INCRINT1 reports the amount of interest or dividend income earned by the source identified in SRCRINT1.  For example, if the source of payments identified in SRCRINT1 were "401k account" (code 1), then INCRINT1 would report the amount of interest or dividends earned from that 401k account during the previous calendar year.  For those persons who reported interest or dividends from a second source in SRCRINT2, INCRINT2 similarly reports the amount of retirement interest or dividends received from that second source during the previous calendar year.   
Amounts are expressed as they were reported/calculated in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCRINT2** | Interest income from a retirement account from second source | INCRINT2 reports the amount of interest or dividend income earned by the source identified in SRCRINT2. For example, if the source of payments identified in SRCRINT2 were "401k account" (code 1), then INCRINT2 would report the amount of interest or dividends earned from that 401k account during the previous calendar year. SRCRINT1 reports the first source of interest or dividend retirement income. INCRINT1 similarly reports the amount of retirement interest or dividends received from that first source during the previous calendar year.   
Amounts are expressed as they were reported/calculated in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **INCCAPG** | Capital gains received from shares of stocks or mutual funds last year | INCCAPG reports the amount of capital gains the respondent earned from shares of stock or mutual funds for those age 15 and older who received dividend income during the previous year.
Amounts are expressed as they were reported in each year; users must adjust for inflation using Consumer Price Index adjustment factors or use the Adjust Monetary Values tool. Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **SRCEARN** | Source of earnings from longest job | SRCEARN reports the source of income (from wages and salary, self-employment, farm self-employment, or working without pay) for the job that the respondent held for the longest time during the preceding calendar year. | - |
| **SRCEDUC** | Source of educational assistance | For persons who attended school beyond high school and who received educational assistance during the previous calendar year, SRCEDUC reports the source(s) of educational assistance: 1) government assistance (such as a Pell Grant), except for VA educational benefits; 2) scholarships and grants; 3) other assistance (from employers, friends, or family not living in the same household); or 4) some combination of assistance from these sources.  Various types of post-high school training, including attending a college, university, or business, vocational, or trade school, counted in this context.  The educational assistance could cover a variety of costs, including tuition, fees, books, and living expenses while attending school. | - |
| **SRCUNEMP** | Source of unemployment income | For persons who reported receiving federal or state unemployment compensation, SRCUNEMP reports on the receipt of additional unemployment income from supplemental unemployment benefits and/or union unemployment or strike benefits during the previous calendar year.  

The term "supplemental unemployment benefits (SUB)" was not defined in the course of the ASEC CPS interview.  In other contexts, the words "supplemental unemployment benefits" may refer to either: 1) government income transfers extending additional weeks of coverage to persons whose regular unemployment compensation benefits have run out (e.g., under the Emergency Unemployment Compensation Act in place from 1991 to 1994); or 2) to employer-provided payments that are written into private employment contracts and augment the amount (and not necessarily the length) of concurrent government unemployment insurance benefits.  While the use of the acronym SUB suggests the question was intended to refer to the second meaning, some respondents may instead have responded in terms of their receipt of extended unemployment benefits from the state or federal government.   

Respondents were first questioned about whether they had received any state or federal unemployment compensation during the previous year.  Only those who gave an affirmative answer to this question were further queried about whether they had received supplemental unemployment benefits, union unemployment benefits, or strike benefits.  Thus, all persons who reported this additional unemployment income (codes 1, 2, and 3 in SRCUNEMP) had also received state or federal unemployment compensation; however, only a fraction of those receiving state or federal unemployment compensation also received additional unemployment income from the sources covered by the SRCUNEMP variable. | - |
| **SRCWELFR** | Source of welfare income | SRCWELFR reports the type of public assistance that respondents received from the state or local welfare office: 1) AFDC (Aid to Families with Dependent Children) or TANF (Temporary Assistance for Needy Families); 2) other public assistance; or 3) both AFDC/TANF and other public assistance.  Under the Welfare Reform Law of 1996, TANF replaced AFDC beginning July 1, 1997.  "Other types of public assistance" included such programs as General Assistance, Emergency Assistance, Cuban/Haitian Refugee Assistance, and Indian Assistance.  Food Stamps and SSI payments were not to be included. | - |
| **SRCWKCOM** | Source of workmen's compensation | SRCWKCOM reports the source of payments (other than sick pay and disability retirement) respondents received as a result of job-related injury or illness.  The sources identified in the survey were state worker's compensation, employer or employer's insurance, own insurance, and "other."  Though some persons probably received such compensation from more than one source, the variable included in the public use files identifies only one source (presumably that paying the largest amount) for each recipient of such payments. | - |
| **MTHWELFR** | Number of months received welfare income | MTHWELFR reports the number of months during the previous calendar year that respondents received public assistance or welfare payments from the state or local welfare office. | - |
| **VETQA** | Required to fill out annual income questionnaire for veterans' administration | VETQA indicates whether respondents who received veterans' payments during the previous calendar year said that they were required to fill out an annual income questionnaire for the Veterans Administration for VA compensation and pension purposes.

Note:  Many veterans must also supply income information to determine their eligibility for enrollment into the VA health care system.  While many veterans qualify for cost-free health care services based on a compensable service-related condition or other qualifying factor (e.g., former prisoners of war, Purple Heart recipients), most veterans are required to complete an annual financial assessment or means test to determine if they qualify for cost-free services.  Veterans whose household income and net worth exceed the established threshold, as well as those who choose not to complete the financial assessment, must agree to pay required co-payments to become eligible for VA health care services. | - |
| **WHYSS1** | First reason for receiving social security income | WHYSS1 reports the first reason respondents gave for receiving Social Security payments during the previous calendar year.  If persons received Social Security payments for more than one reason (e.g., on the basis of both widowhood and disability), they reported their second reason for receiving Social Security payments in the complementary variable WHYSS2.

Respondents were to report Social Security payments that they themselves received as beneficiaries and Social Security payments that they received on behalf of a child beneficiary.  When interpreting the value labels, users should keep in mind the two meanings of "child" in this context.  Beginning in 1980, the ASEC CPS defined as a "child" anyone under age 15; persons age 15 and older were considered "adults" by the survey and were asked questions about their employment and own income.  (Prior to 1980, persons under age 14 were considered "children" in terms of the survey universe for work and income questions.)  By contrast, government programs such as Social Security generally use the more common definition of "child" to mean persons under age 18 when defining eligibility for benefits.  Thus, the value label "Surviving child" (corresponding to code 5) covers reporting of one's own benefits by persons who qualify for benefits as "children" under Social Security's eligibility rules (i.e., they are unmarried and under age 18 or are unmarried, under age 19, and attending secondary school full-time) but who are "adults" in terms of the CPS definition (i.e., they have passed their 15th birthday).    The value label "On behalf of surviving, dependent, or disabled child(ren)" (corresponding to code 7) covers reporting of benefits on behalf of persons who are under age 15. | - |
| **WHYSS2** | Second reason for receiving social security income | WHYSS2 reports the second reason respondents gave for receiving Social Security payments during the previous calendar year.  The first reason for receipt of such payments is reported in the complementary variable WHYSS1.  

Interviewers asked, "What were the reasons you were getting Social Security?," checked off all applicable answers on the form, and elicited further answers with the probe, "Any other reason?"  Many recipients of Social Security income received such payments for only one reason (reported in WHYSS1), and these individuals are coded as Not in Universe (code 0) in WHYSS2.  For individuals who reported receiving Social Security payments for more than one reason (e.g., on the basis of both disability and widowhood), the second reason given is recorded in WHYSS2.

Respondents were to report Social Security payments that they themselves received as beneficiaries and Social Security payments that they received on behalf of a child beneficiary.  When interpreting the value labels, users should keep in mind the two meanings of "child" in this context.  Beginning in 1980, the ASEC CPS defined as a "child" anyone under age 15; persons age 15 and older were considered "adults" by the survey and were asked questions about their employment and own income.  (Prior to 1980, persons under age 14 were considered "children" in terms of the survey universe for work and income questions.)  By contrast, government programs such as Social Security generally use the more common definition of "child" to mean persons under age 18 when defining eligibility for benefits.  Thus, the value label "Surviving child" (corresponding to code 5) covers reporting of one's own benefits by persons who qualify for benefits as "children" under Social Security's eligibility rules (i.e., they are unmarried and under age 18 or are unmarried, under age 19, and attending secondary school full-time) but who are "adults" in terms of the CPS definition (i.e., they have passed their 15th birthday).    The value label "On behalf of surviving, dependent, or disabled child(ren)" (corresponding to code 7) covers reporting of benefits on behalf of persons who are under age 15. | - |
| **WHYSSI1** | First reason for receiving supplementary security income | WHYSSI1 reports the first reason respondents gave for receiving Supplemental Security Income during the previous calendar year.  If persons received Supplemental Security Income for more than one reason (e.g., on the basis of both blindness and on behalf of a disabled child), they reported their second reason for receiving Supplemental Security Income in the complementary variable WHYSSI2.

Respondents were to report SSI payments that they themselves received as beneficiaries and SSI payments that they received on behalf of a child beneficiary.  When interpreting the value labels, users should keep in mind the two meanings of "child" in this context.  Beginning in 1980, the ASEC CPS defined as a "child" anyone under age 15; persons age 15 and older were considered "adults" by the survey and were asked questions about their employment and own income.  (Prior to 1980, persons under age 14 were considered "children" in terms of the survey universe for work and income questions.)  By contrast, government programs such as SSI generally use the more common definition of "child" to mean persons under age 18 when defining eligibility for benefits.  Thus, the value label "Disabled (adult or child)" (corresponding to code 1) covers reporting of one's own benefits by disabled persons who are legally adults (age 18+) and by disabled persons who are legally children but who are "adults" in terms of the CPS definition (age 15-17).    The value label "On behalf of a disabled child" (corresponding to code 3) covers reporting of benefits on behalf of a disabled child under age 15. | - |
| **WHYSSI2** | Second reason for receiving supplementary security income | WHYSSI2 reports the second reason respondents gave for receiving Supplemental Security Income during the previous calendar year.  The first reason for receipt of such payments is reported in the complementary variable WHYSSI1.  

Interviewers asked, "What were the reasons you were getting Supplemental Security Income?", checked off all applicable answers on the form, and elicited further answers with the probe, "Any other reason?"  Many recipients of Supplemental Security Income received such payments for only one reason (reported in WHYSSI1), and these individuals are coded as Not in Universe (code 0) in WHYSSI2.  For individuals who reported receiving Supplemental Security Income payments for more than one reason (e.g., on the basis of blindness and on behalf of a disabled child), the second reason given is recorded in WHYSSI2.

Respondents were to report SSI payments that they themselves received as beneficiaries and SSI payments that they received on behalf of a child beneficiary.  When interpreting the value labels, users should keep in mind the two meanings of "child" in this context.  Beginning in 1980, the ASEC CPS defined as a "child" anyone under age 15; persons age 15 and older were considered "adults" by the survey and were asked questions about their employment and own income.  (Prior to 1980, persons under age 14 were considered "children" in terms of the survey universe for work and income questions.)  By contrast, government programs such as SSI generally use the more common definition of "child" to mean persons under age 18 when defining eligibility for benefits.  Thus, the value label "Disabled (adult or child)" (corresponding to code 1) covers reporting of one's own benefits by disabled persons who are legally adults (age 18+) and by disabled persons who are legally children but who are "adults" in terms of the CPS definition (age 15-17).    The value label "On behalf of a disabled child" (corresponding to code 3) covers reporting of benefits on behalf of a disabled child under age 15. | - |
| **GOTVDISA** | Received veterans' disability compensation | GOTVDISA indicates whether respondents who received veterans' payments during the previous calendar year received VA Disability Compensation.  VA Disability Compensation is a monetary benefit paid to a veteran who was disabled by injury or disease incurred or aggravated in the line of duty during active military service. | - |
| **GOTVEDUC** | Received veterans' education assistance | GOTVEDUC indicates whether respondents who received veterans' payments during the previous calendar year received veterans' educational assistance.  The specific educational assistance programs administered by the Veterans Administration have varied over time; programs include the Veterans' Educational Assistance Program, the Montgomery G.I. Bill, and the Survivors' and Dependents' Educational Assistance Program. | - |
| **GOTVOTHE** | Received other veterans' payments | GOTVOTHE indicates whether respondents who received veterans' payments during the previous calendar year received some form of compensation from the Veterans Administration other than educational assistance, survivor benefits, disability compensation, or a VA pension.   Most income transfers from the VA fall within one of these four specific categories, not in a residual "other" category. | - |
| **GOTVPENS** | Received veterans' pension | GOTVPENS indicates whether a respondent who received veterans' payments during the previous calendar year received a veteran's pension.   The Veterans Administration provides pensions to some veterans with low incomes whose active service occurred, at least in part, during a period of war.  Military retirement pensions paid to veterans after twenty years of active military service are not included in this category. | - |
| **GOTVSURV** | Received veterans' survivor benefits | GOTVSURV indicates whether respondents who received veterans' payments during the previous calendar year received veterans' survivor benefits.  Dependency and indemnity compensation and/or a death pension may be paid to the spouse of a deceased veteran (if the spouse has not remarried), to the children of a deceased veteran (if the children are unmarried and are either under age 18 or are between the ages of 18 and 23 and are attending school), or to the parents of a deceased veteran (if their income falls below a specific cut-off).  For survivors to be eligible the deceased veteran must have died from disease or injury incurred or aggravated while on active duty or during military training, or from a disability compensated by the Veterans Administration. | - |
| **CTCCRD** | Child Tax Credit | CTCCRD indicates the dollar amount the respondent received from the Child Tax Credit. This tax credit may be worth as much as $1,000 per qualifying child depending upon your income. A child qualifies for this credit if they meet the relevant criteria of six test: age, relationship, support, dependent, citizenship and residence. See the IRS Tax Tip 2011-29, February 10, 2011 for more information.

CTCCRD, like other tax-related variables included in the ASEC CPS (ADJGINC, ACTCCRD, CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FEDTAX, FICA, FILESTAT, MARGTAX, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-186RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

Amounts for CTCCRD are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation. Users can adjust for inflation using Consumer Price Index adjustment factors. 

The 2021 expanded child credits were imputed for the 2022 CPS ASEC sample. The 2022 CPS ASEC sample added two new tax variables (UH_CDCCRD_A1 and UH_ADVCTC_A1) and updated the definitions for FEDTAXAC, CTCCRD, and ACTCCRD. For more information, please view this working paper. | - |
| **ACTCCRD** | Additional Child Tax Credit | ACTCCRD indicates the dollar amount the respondent received in Additional Child Tax Credit. An individual can claim the Additional Child Tax Credit in addition to the Child Tax Credit if the amount of the Child Tax Credit is greater than the amount of income tax owed by an individual. See the IRS Tax Tip 2011-29, February 10, 2011 for more information.

ACTCCRD, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, CTCCRD, EITCRED, FEDRETIR, FEDTAX, FICA, FILESTAT, MARGTAX, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-186RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

Amounts for ACTCCRD are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation. Users can adjust for inflation using Consumer Price Index adjustment factors. 

The 2021 expanded child credits were imputed for the 2022 CPS ASEC sample. The 2022 CPS ASEC sample added two new tax variables (UH_CDCCRD_A1 and UH_ADVCTC_A1) and updated the definitions for FEDTAXAC, CTCCRD, and ACTCCRD. For more information, please view this working paper. | - |
| **ADJGINC** | Adjusted gross income | For income tax purposes, ADJGINC (Adjusted Gross Income) consists of an individual's total gross (pre-tax) income from taxable sources minus certain items, such as individual retirement plan contributions (payments to a Keogh plan or a deductible Individual Retirement Account), alimony paid, medical savings accounts, and non-reimbursed employee business expenses.  ADJGINC minus deductions and personal exemptions equals the individual's taxable income (TAXINC).

ADJGINC, like other tax-related variables included in the ASEC CPS (CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FEDTAX, FICA, FILESTAT, MARGTAX, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-18RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

Amounts for ADJGINC are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. | - |
| **EITCRED** | Earned income tax credit | EITCRED represents the value of the Earned Income Tax Credit for an individual or couple filing a federal income tax return. The federal Earned Income Tax Credit (EITC) is a refundable tax credit that reduces or eliminates the amount of income tax that low-to moderate-income working people are required to pay, and it frequently operates as a wage subsidy for low-income workers.  If the amount of the credit exceeds the amount owed in federal income taxes, the difference is received as a cash payment. The value of the EITC depends on the amount of earned income and family size (e.g., whether a single-parent or two-parent family and number of dependent children).

EITCRED, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, FEDRETIR, FEDTAX, FICA, FILESTAT, MARGTAX, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-186RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

Amounts for EITCRED are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. | - |
| **FEDTAX** | Federal income tax liability, before credits | FEDTAX reports the federal income tax liability for an individual or for a couple filing a joint tax return.  The federal income tax on personal income provides for national programs such as defense, foreign affairs, law enforcement, and interest on the national debt.  "Federal income tax liability" means the amount of federal income tax, excluding any federal minimum alternative tax, taxpayers are required to pay.  A value of "00000" for this variable indicates no federal income tax liability.

Beginning in 2005, FEDTAXAC is added to the data, which indicates the amount of federal tax liability, after tax credits are deducted.  On the other hand, FEDTAX indicates the amount of federal tax liability, before tax credits are deducted.  The credits include the additional child tax credit and the earned income tax credit.

FEDTAX, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FICA, FILESTAT, MARGTAX, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-18RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

Amounts for FEDTAX are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. | - |
| **FEDTAXAC** | Federal income tax liability, after all credits | FEDTAXAC indicates the amount of federal tax liability, after tax credits are deducted.  The credits include the additional child tax credit and the earned income tax credit.  For more information about these credits, see the Internal Revenue Service website.  FEDTAX  indicates the amount of federal tax liability, before tax credits are deducted.  Amounts are reported in dollars.

Amounts for FEDTAXAC are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. 

In 2021 and 2022, the economic impact payments were imputed and affected this variable. For more information, please view this working paper. Additionally, the 2021 expanded child credits were imputed for the 2022 CPS ASEC sample. The 2022 CPS ASEC sample added two new tax variables (UH_CDCCRD_A1 and UH_ADVCTC_A1) and updated the definitions for FEDTAXAC, CTCCRD, and ACTCCRD. For more information, please view this working paper. | - |
| **FICA** | Social security retirement payroll deduction | FICA reports the total Social Security retirement payroll deductions for an individual or for a couple filing a joint tax return.  Social Security payroll taxes are collected under authority of the Federal Insurance Contributions Act (FICA).  Under this law, employers are required to withhold a share of employee wages and pay them to the government trust fund which provides benefits via Social Security.   FICA payroll taxes are thus both taxes and contributions to the social insurance system of Social Security, which funds retirement benefits, disability insurance, and survivor benefits.

FICA, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FEDTAX, FILESTAT, MARGTAX, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-18RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

Amounts for FICA are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. | - |
| **FILESTAT** | Tax filer status | FILESTAT reports the federal income tax filing status (single, married filing jointly, head of household, and non-filer) for individuals.  For joint filers, the response categories are further determined by age (over 65 years of age, or younger than 65, for one or both of the filers).  

Under IRS rules, an individual's tax filing status is partly determined by marital status on the last day of the year.  Unmarried persons and those who are legally separated or divorced, and who do not qualify for another filing status, must file as single.  With a few exceptions (i.e., those who were still married but who lived apart from their spouse for at least half the year), head of household filing status is reserved for persons who were not married and who paid for over half the cost of maintaining a home that also housed a dependent unmarried child, grandchild, or dependent parent.  Users should note that the "head of household" value for FILESTAT is not synonymous with identification as the household reference person in the RELATE (Relationship to head of household) variable.

FILESTAT, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FEDTAX, FICA, MARGTAX, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-18RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

To understand more about the census tax model and the construction and assumption of tax variables, please see this paper | - |
| **DEPSTAT** | Dependency status pointer | DEPSTAT is a dependency status pointer, which indicates a person line number of person who claimed the respondent as his/her dependent. Person line number values are available in the LINENO variable.  

Data checking has revealed dramatic shifts across time in the proportion of persons who are dependent, which may indicate inaccuracies in the data.  Researchers should exercise caution in using DEPSTAT until the cause of these problems can be determined. | - |
| **MARGTAX** | Federal income marginal tax rate | MARGTAX reports the Federal Income Marginal Tax Rate for an individual or for a couple filing a joint tax return.  The Marginal Tax Rate is the rate of tax imposed on an additional dollar of taxable income, or on the last dollar of taxable income.  If a person's marginal tax rate is 43 percent, they will net $0.57 for every dollar (after taxes, 100 percent less 43 percent).  Values for MARGTAX are 2-digits with an implicit decimal point before the first digit.  

MARGTAX, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FEDTAX, FICA, FILESTAT, STATETAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-18RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS. | - |
| **STATETAX** | State income tax liability, before credits | STATETAX reports the numerical state income tax liability of an individual or of a couple filing a joint tax return.  Tax provisions vary by state of residence.  Some states do not levy income taxes, while others allow individual cities to impose an additional income tax.  State tax provisions incorporated in the Census Bureau's tax model were based on the State Tax Handbook.

Beginning in 2005, STATAXAC was added to the data, which indicates the amount of state tax liability, after tax credits are deducted.  On the other hand, STATETAX indicates the amount of state tax liability, before tax credits are deducted.  The credits include the additional child tax credit and the earned income tax credit.

STATETAX, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FEDTAX, FICA, FILESTAT, MARGTAX, TAXINC, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-18RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

In 2004, STATETAX started reporting negative dollar values.

Amounts for STATETAX are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. | - |
| **STATAXAC** | State income tax liability, after all credits | STATAXAC indicates the amount of state tax liability, after tax credits are deducted.  The credits include the additional child tax credit and the earned income tax credit.  For more information about these credits, see the  Internal Revenue Service website. STATETAX  indicates the amount of state tax liability, before tax credits are deducted.  Amounts are reported in dollars. 

Amounts for STATAXAC are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. | - |
| **TAXINC** | Taxable income amount | For income tax purposes, TAXINC, or taxable income, consists of adjusted gross income (ADJGINC) minus allowable itemized deductions (or a standard allowance amount) and exemptions for the taxpayer and his or her dependents.  Taxable income is the amount used in the calculation of an individual's income tax liability.

TAXINC, like other tax-related variables included in the ASEC CPS (ADJGINC, CAPGAIN, CAPLOSS, EITCRED, FEDRETIR, FEDTAX, FICA, FILESTAT, MARGTAX, STATETAX, and household level variable PROPTAX) was not determined by direct questioning of respondents.  Rather, values for these variables come from the Census Bureau's tax model, which simulates individual tax returns to produce estimates of federal, state, and payroll taxes.  The model incorporates information from non-CPS sources, such as the Internal Revenue Service's Statistics of Income series, the American Housing Survey, and the State Tax Handbook.  For more information about the model, see Current Population Reports, Series P60-18RD.  The IPUMS-CPS staff welcomes further information from users about the interpretation of this variable or other tax-related variables in the ASEC CPS.

Amounts are expressed in dollars of the given year, rather than in constant dollars adjusted for inflation.  Users can adjust for inflation using Consumer Price Index adjustment factors. | - |
| **MIGSTA1** | State of residence 1 year ago | MIGSTA1 reports the U.S. state of previous residence for respondents who were living in a different house a year ago.   Interviewers asked whether respondents were living in the same house or apartment on March 1 of the previous year.  Movers (those who answered, "No") then supplied information about the city, county, and state or foreign country where they lived a year ago.  

The MIGRATE1 variable identifies nonmovers and classifies movers according to whether their change of residence crossed county lines, state lines, or international boundaries.  COUNTRY identifies the country of previous residence for movers who were living abroad a year ago. | - |
| **WHYMOVE** | Reason for moving | WHYMOVE reports the primary reason for moving, for people who lived in a different residence a year ago.  While data were collected for all movers age 1 and older, the responses for minors doubtless reflect the rationales given by adults in the household.  The codes relate to family, work, housing, education, climate, and health.    

Movers across various geographic boundaries--county, state, and country--are identified in the MIGRATE1 variable.  State and foreign country of previous residence are specified in the MIGSTA1 and COUNTRY variables, respectively. | - |
| **MIGRATE1** | Migration status, 1 year | MIGRATE1 indicates whether the respondent had changed residence in the past year.   Those who were living in the same house as one year ago were considered non-movers and were asked no further questions about migration over the past year.   Movers were asked about the city, county and state and/or the U.S. territory or foreign country where they resided one year ago.

The category "Same house" includes both persons who did not move since the reference date (March 1 of the preceding year) and those who had moved and then returned to their earlier residence. Movers are subdivided into the following categories: those who had moved within the same county; those who had crossed county lines but stayed in the same state; those who those who had resided in a different state; and those who had migrated from abroad.

Information about the state where movers were living one year ago is available in the MIGSTA1 variable.  COUNTRY specifies the foreign country or U.S. territory of previous residence for those who migrated from abroad during the past year. 

In the 2002 ASEC sample, 54 children between the ages of 1 and 3 are coded as NIU in the original data and have been left unrecoded despite not being in line with the universe statement in the original documentation.

User Caution: Frequencies in the 1995 ASEC original CPS data are highly suspect and differ greatly from surrounding years. | - |
| **PAIDGH** | Employer paid for group health plan | PAIDGH indicates whether an employer or union paid for all, part, or none of the cost of premiums for an employment-based group health insurance plan that the respondent was included in (i.e., was the policyholder for), during the previous calendar year.  For discussion of changes in the question wording about inclusion in employment-based health insurance, see INCLUGH. | - |
| **HIMCAIDLY** | Covered by Medicaid last year | HIMCAIDLY indicates whether the respondent was covered by Medicaid during the previous calendar year. The data in HIMCAID were edited by the Census Bureau and assign Medicaid coverage to some persons who did not report such health insurance during questioning. For general discussion of Medicaid funding and eligibility, see CAIDLY.

For 1980-1987, information on health insurance coverage was collected only for persons age 15 and above. The CPS interviewer asked, "At any time during [the previous year], was anyone in this household covered by Medicaid, the public assistance program that pays for health care? Who was that?" The Census Bureau edited the data to allot coverage (a "yes" response in HIMCAIDLY) to some children, as well as to some categories of adults who did not provide an affirmative response to the Medicaid question. All children under age 21 in families were assumed to be covered by Medicaid if either the householder or spouse reported being covered by Medicaid. All adult AFDC recipients and their children, and SSI recipients living in states which legally required Medicaid coverage for persons receiving Supplemental Security Income, were also coded as "yes" in HIMCAIDLY.

Beginning in 1988, the question wording remained the same, but CPS interviewers directly collected information on Medicaid coverage for all household members, of all ages. With the introduction of computer-assisted interviewing technology (CATI) in 1994, the interviewer also asked about Medicaid coverage by referring to the state-specific names of Medicaid programs in the state where the household was located.

After 1987, the Census Bureau continued to edit the data in HIMCAIDLY, assigning Medicaid coverage to some persons who did not mention Medicaid during questioning. For example, in 1996 and 1997, HIMCAIDLY was coded as "Yes" if the individual reported coverage from Indian Health Service, or reported having "other government health care" or "other insurance" in a final, follow-up question about health insurance not previously acknowledged. | - |
| **HIMCARELY** | Covered by Medicare last year | HIMCARELY indicates whether the respondent was covered by Medicare during the previous calendar year. The data in HIMCARELY were edited by the Census Bureau and assign Medicare coverage to some persons who did not report such health insurance during questioning.

For 1980-1987, information on health insurance coverage was collected only for persons age 15 and above. The CPS interviewer asked, "At any time during [the previous year], was anyone in this household covered by Medicare, the health insurance for persons 65 years old and over or persons with disabilities?" The Census Bureau edited the data to allot coverage (a "Yes" response in HIMCARELY) to all persons age 65 and older who reported income from Social Security. After 1988, the universe for Medicare recipients was still treated as persons age 15 and older, even though the survey generally focused on insurance coverage for all age groups.

Beginning in 1988, the question wording remained the same, but CPS interviewers directly collected information on insurance coverage for all household members, of all ages. Because the universe for Medicare coverage was treated as persons age 15 and older, this basic change in the phrasing of insurance-related questions had less effect on HIMCARELY than on other insurance-related variables. | - |
| **HIMCAIDNW** | Current Medicaid, CHIP, or other means-tested coverage | HIMCAIDNW identifies persons who reported having Medicaid, CHIP, or other means-tested coverage at the time of their interview. Interviewers defined Medicaid as "the government assistance that pays for health care," and they mentioned both federal Medicaid programs and the Medicaid programs specific to the state where the household was located when collecting this information. CHIP provides insurance to eligible children through Medicaid and other programs administered by the states. The original CPS documentation gives no indication of what is included under "other means-tested coverage."

Medicaid pays for medical assistance to low-income families with dependent children and to aged, blind, or permanently and totally disabled individuals with incomes insufficient to meet the costs of medical services. The program became law in 1965.  Medicaid is administered by state agencies and is jointly funded by the federal, state, and, sometimes, local governments. Eligibility requirements for this means-tested program vary across states.  All recipients of Aid to Families with Dependent Children (AFDC) and most recipients of Supplemental Security Income (SSI) are eligible for Medicaid coverage.  In some states, other persons qualify, such as needy unemployed persons who have children and who are not receiving cash assistance, and medically needy persons whose income and assets are too low to cover their medical costs. Many Medicaid recipients are inmates of medical institutions, such as low-income elderly persons in nursing homes. Such institutionalized persons are not included in the CPS sample. | - |
| **HIMCARENW** | Current Medicare coverage | HIMCAIDNW identifies persons who reported having Medicare coverage at the time of their interview. | - |
| **HICHAMP** | Covered by military health insurance last year | HICHAMP indicates whether the respondent was covered by CHAMPUS, VA, or other military health care during the previous calendar year.
 
For 1980-1987, information on military health insurance coverage was collected only on persons age 15 and above.  The CPS interviewer asked, "At any time during [the previous year], was anyone in this household covered by CHAMPUS, VA, or military health care?  Who was that?"   Editing by the Census Bureau allotted coverage (a "yes" response in HICHAMP) to the child and adult dependents (e.g., children, spouse) covered by the policy of the household member enrolled in CHAMPUS or other military health care.      

For 1988-1993, the question wording remained the same, but CPS interviewers directly collected information on military health insurance coverage for all household members, of all ages. With the introduction of computer-assisted interviewing technology (CATI) in 1994, information was collected through a series of questions, after the interviewer had asked about employment-based and privately-purchased insurance, Medicaid, and Medicare.  Specifically, the interviewer asked, "At any time during [the previous calendar year], was anyone in the household covered by any other kind of health insurance, including CHAMPUS, CHAMPVA, VA or military health care, or the Indian Health Service?  Who was that?  What plan were you covered by?"  Those who reported coverage by CHAMPUS, CHAMPVA, or VA health care were coded as "yes" in HICHAMP. | - |
| **PHINSUR** | Reported covered by private health insurance last year | PHINSUR indicates whether the respondent reported being covered by a private (i.e., employment-based or privately-purchased, not government) insurance plan during the preceding calendar year.  

The term "covered by private insurance" in the direct question posed to respondents is ambiguous; coverage might mean either being a private insurance policyholder or having coverage as a dependent via someone else's private insurance policy.  Because some respondents interpreted the question in the former, narrower sense, the identification of persons covered by private insurance (either as policyholders or as dependents) via the Bureau's allocation program in COVERPI is more complete than the private health insurance coverage reported in PHINSUR. | - |
| **PHIOWN** | Private health insurance in own name last year | PHIOWN indicates whether a respondent covered by a private (i.e., employment-based or privately-purchased, not governmental) insurance plan during the previous calendar year held such a plan in his or her own name (i.e., was the policyholder for such a plan). | - |
| **CAIDLY** | Covered by Medicaid last year | CAIDLY identifies persons who reported Medicaid coverage during the previous calendar year. Interviewers defined Medicaid as "the government assistance that pays for health care," and they mentioned both federal Medicaid programs and the Medicaid programs specific to the state where the household was located when collecting this information.  

Medicaid pays for medical assistance to low-income families with dependent children and to aged, blind, or permanently and totally disabled individuals with incomes insufficient to meet the costs of medical services. The program became law in 1965.  Medicaid is administered by state agencies and is jointly funded by the federal, state, and, sometimes, local governments. Eligibility requirements for this means-tested program vary across states.  All recipients of Aid to Families with Dependent Children (AFDC) and most recipients of Supplemental Security Income (SSI) are eligible for Medicaid coverage.  In some states, other persons qualify, such as needy unemployed persons who have children and who are not receiving cash assistance, and medically needy persons whose income and assets are too low to cover their medical costs. Many Medicaid recipients are inmates of medical institutions, such as low-income elderly persons in nursing homes. Such institutionalized persons are not included in the CPS sample.

Through programming in IPUMS CPS, other cases were added to the pool of positive responses for the CAIDLY variable in the original public use data in 1996-2018.  If the respondent mentioned Medicaid coverage when answering a catchall summary question on "other" health insurance plans, after hearing questions about many specific types of insurance coverage (including Medicaid), then that person was given a positive response for CAIDLY in IPUMS CPS. | - |
| **CAIDNW** | Current Medicaid coverage | CAIDNW identifies persons who reported having Medicaid coverage at the time of their interview. Interviewers defined Medicaid as "the government assistance that pays for health care," and they mentioned both federal Medicaid programs and the Medicaid programs specific to the state where the household was located when collecting this information.  

Medicaid pays for medical assistance to low-income families with dependent children and to aged, blind, or permanently and totally disabled individuals with incomes insufficient to meet the costs of medical services. The program became law in 1965.  Medicaid is administered by state agencies and is jointly funded by the federal, state, and, sometimes, local governments. Eligibility requirements for this means-tested program vary across states.  All recipients of Aid to Families with Dependent Children (AFDC) and most recipients of Supplemental Security Income (SSI) are eligible for Medicaid coverage.  In some states, other persons qualify, such as needy unemployed persons who have children and who are not receiving cash assistance, and medically needy persons whose income and assets are too low to cover their medical costs. Many Medicaid recipients are inmates of medical institutions, such as low-income elderly persons in nursing homes. Such institutionalized persons are not included in the CPS sample. | - |
| **CAIDPART** | Medicaid coverage for all or part of last year | CAIDPART reports whether the respondent had Medicaid coverage during the entire previous year or only part of it. Infants born after the calendar year are not included. | - |
| **MOOP** | Total family (primary family including related subfamilies) medical out of pocket payments (in dollars) | MOOP reports the total dollar amount a Census family, including related subfamilies, spent on medical expenditures out of pocket in the last 12 months.  There are no implied decimals. (For more on Census families see FTYPE and FAMREL; this is a different definition from IPUMS-derived families as in FAMUNIT).

Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **HIPVAL** | Total family (primary family including related subfamilies) payments (in dollars) for health insurance premiums | HIPVAL reports the total dollar amount a Census family, including related subfamilies, spent on health insurance premiums in the last 12 months.  There are no implied decimals. (For more on Census families see FTYPE and FAMREL; this is a different definition from IPUMS-derived families as in FAMUNIT).

Inflation-adjusted versions created with the Adjust Monetary Values tool will use the default reference year for the sample (i.e., survey year [YEAR] for basic monthly and previous year [YEAR-1] for ASEC). | - |
| **ANYCOVLY** | Any health insurance coverage last year | ANYCOVLY reports whether the respondent had any health insurance coverage during the previous year. Infants born after the calendar year are not in universe. | - |
| **ANYCOVNW** | Covered by health insurance at time of interview | ANYCOVNW indicates whether the respondent was covered by any type of health insurance at the time of the interview.  ANYCOVNW is a Census recode of current coverage of private health insurance, Medicare, Medicaid, CHIP, other government coverage, or military coverage (TRICARE, VA Care, CHAMPVA). | - |
| **PUBCOVLY** | Any government health insurance coverage last year | PUBCOVLY reports whether the respondent had any government health insurance coverage during the previous year. Infants born after the calendar year are not included. | - |
| **PUBCOVNW** | Any current government health insurance coverage | PUBCOVNW reports whether the respondent currently has any government health insurance coverage. | - |
| **ANYPART** | Any insurance coverage for all or part of last year | ANYPART reports whether the respondent had any health insurance coverage during the entire previous year or only part of it. Infants born after the calendar year are not included. | - |
| **PUBPART** | Government insurance coverage for all or part of last year | PUBPART reports whether the respondent had government-provided health insurance coverage during the entire previous year or only part of it. Infants born after the calendar year are not included. | - |
| **PRVTPART** | Private insurance coverage for all or part of last year | PRVTPART reports whether the respondent had private health insurance coverage during the entire previous year or only part of it. Infants born after the calendar year are not included.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. PHINSUR, reported covered by private insurance last year, adheres to the pre-2019 definition of private insurance. | - |
| **PRVTCOVLY** | Any private coverage last year (2019 definition) | PRVTCOVLY reports whether the respondent had any private health insurance coverage during the previous year. Infants born after the calendar year are not included.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. PHINSUR, reported covered by private insurance last year, adheres to the pre-2019 definition of private insurance. | - |
| **PRVTDEPLY** | Private insurance through a household member last year (2019 definition) | PRVTDEPLY indicates whether the respondent had private health insurance coverage through a household member during the last year.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. | - |
| **PRVTOWNLY** | Policyholder for private insurance last year | PRVTOWNLY reports whether the respondent was the policy holder for their private insurance coverage last year.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. PHINSUR, reported covered by private insurance last year, adheres to the pre-2019 definition of private insurance. | - |
| **PRVTCOUTLY** | Private insurance coverage through someone outside the household last year | PRVTCOUTLY reports whether the respondent was covered by the private health insurance policy of someone outside the household during the previous year.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. | - |
| **PRVTCOVNW** | Currently covered by private insurance | PRVTCOVNW indicates whether the respondent is currently covered by private health insurance.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. | - |
| **PRVTDEPNW** | Currently have private health insurance through a household member | PRVTDEPNW indicates whether the respondent currently has private health insurance coverage through a household member.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. | - |
| **PRVTOWNNW** | Policyholder for current private insurance | PRVTOWNNW reports whether the respondent is the policy holder for their current private insurance coverage.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. PHINSUR, reported covered by private insurance last year, adheres to the pre-2019 definition of private insurance. | - |
| **PRVTCOUTNW** | Current private coverage provided by person outside the household | PRVTCOUTNW indicates whether the respondent's current private health insurance coverage is provided by someone living outside the household.

In this variable, "private" includes employment-based, directly purchased, marketplace, non-marketplace, and TRICARE coverage. This definition of private insurance begins with the 2019 ASEC. Prior to 2019, "private" insurance included only employment-based and directly purchased insurance. | - |
| **GRPCOVLY** | Covered by employment-based group health last year | GRPCOVLY indicates whether the respondent was covered, either as a policyholder or as a dependent of another household member, by employment-based group health insurance during the previous calendar year. | - |
| **GRPDEPLY** | Dependent covered by employment-based insurance last year | GRPDEPLY indicates whether, during the previous calendar year, the respondent had coverage, as a dependent, on employment-based health insurance. The interviewer asked whether, at any time during the previous calendar year, anyone in the household was covered by a health plan provided through a current or former employer or union (excluding military health insurance), and distinguished between policyholders and dependents covered by the plan through follow-up questions.     

Persons who were policyholders for such insurance are identified in the GRPOWNLY variable. Up to two household members who were policyholders for employment-based group health insurance are identified in the GRPWHO1 and GRPWHO2 variables. Using the GRPWHO1, GRPWHO2, and LINENO variables, researchers can identify the policyholder(s) whose employment-based insurance provided coverage for someone coded as "Yes" in GRPDEPLY.  

Through programming in IPUMS-CPS, other cases were added to the pool of positive responses for GRPDEPLY in 1996-2018.  If the respondent mentioned dependent coverage on employment-based insurance in response to a catchall summary question on "other" health insurance plans (after hearing questions about many specific types of insurance coverage, including employment-based insurance), then that person was given a positive response for GRPDEPLY in IPUMS CPS. | - |
| **GRPOWNLY** | Policyholder for employment-based insurance last year | GRPOWNLY indicates whether, during the previous calendar year, the respondent was the policyholder for group health insurance that was related to current or past employment.  The interviewer asked whether, at any time during the previous calendar year, anyone in the household was covered by a health plan provided through a current or former employer or union (excluding military health insurance).  Follow-up questions identified the policyholder(s) and other persons covered by such insurance, including persons living outside the household.  

Through programming in IPUMS CPS in 1996-2018, other cases were added to the pool of positive responses for GRPOWNLY.  Such additions were made when the respondent mentioned being the policyholder for such insurance, when answering a catchall summary question on "other" health insurance plans that followed questions about many specific types of insurance coverage.    

Persons who had insurance coverage as dependents of a policyholder are identified in the GRPDEPLY variable.  Up to two household members who were policyholders for employment-based group health insurance are identified in the GRPWHO1 and GRPWHO2 variables.  GRPTYPLY indicates whether the policyholder's employment-based health insurance covered the respondent only or also covered family members, and GRPOUTLY reports whether the policyholder's coverage extended to persons outside the household. | - |
| **GRPOUTLY** | Employment-based insurance covered non-household member | GRPOUTLY indicates whether, during the previous calendar year, the respondent's own policy for employment-based health insurance provided coverage for someone outside the household.  The interviewer asked whether, at any time during the previous calendar year, anyone in the household was covered by employment-based health insurance, and distinguished between policyholders and dependents covered by the plan through follow-up questions.  One such question, the basis for GRPOUTLY, inquired whether the respondent's employment-based policy covered anyone outside the household.     

Persons who were policyholders for such insurance are identified in the GRPOWNLY variable.  GRPDEPLY identifies household members covered as dependents by the employment-based insurance policy of someone in the household.  Up to two household members who were policyholders for employment-based health insurance are identified in the GRPWHO1 and GRPWHO2 variables.  GRPTYPLY indicates whether the policyholder's employment-based health insurance covered the respondent only or also covered family members. | - |
| **GRPCOUTLY** | Employment-based insurance coverage through someone outside the household last year | GRPCOUTLY reports whether the respondent was covered by the employment-based health insurance policy of someone outside the household during the previous year. | - |
| **GRPTYPLY** | Type of employment-based coverage last year | GRPTYPLY indicates whether group health insurance acquired through a current or past job or union covered only the policyholder or also covered dependents, during the previous calendar year.  Policyholders of employment-based insurance are identified in the GRPOWNLY variable. Persons who had coverage from such a plan as dependents of a policyholder are identified in the GRPDEPLY variable.  Whether a policyholder's employment-based health insurance provided coverage for someone outside the household is reported in GRPOUTLY. | - |
| **GRPWHO1** | Line number of first policyholder of employment-based insurance | GRPWHO1 indicates the line number of the first member of the household who was the policyholder for employment-based insurance covering the respondent during the previous calendar year.  GRPWHO1 is a pointer value that allows researchers to link a dependent covered by employment-based insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Imagine, for example, that a male householder was the policyholder for employment-based insurance that also covered a co-resident child, and that the value of LINENO for the householder is 01.   Imagine also that the wife of the householder was a policyholder for employment-based insurance that covered the same co-resident child, and that the value of LINENO for the wife is 02. 

If both the householder and his wife declared their spouses as dependents on their employment-based insurance policies, then each would have the other's LINENO as the value for GRPWHO2. 

The value of GRPWHO1 on the child's record would be 01, since the family health care plan of the householder supplied the coverage for that child, as a dependent.  The value of GRPWHO2 on the child's record would be 02, reflecting coverage as a dependent from the employment-based insurance policy of the spouse.   However, the policyholders themselves would be coded as 0 (not in universe) on these variables unless they are covered by someone else.   

If the respondent was also covered by employment-based insurance from the policy of a second household member, that second policyholder is identified in the comparable GRPWHO2 variable.

Whether an individual was the policyholder for employment-based insurance is indicated by the GRPOWNLY variable. Persons who had insurance coverage as dependents of a policyholder are identified in the GRPDEPLY variable.  GRPTYPLY indicates whether the policyholder's employment-based health insurance covered the respondent only or also covered family members, and GRPOUTLY reports whether the policyholder's coverage extended to persons outside the household. | - |
| **GRPCOVNW** | Currently covered by employment-based insurance | GRPCOVNW indicates whether the respondent is currently covered by employment-based health insurance. | - |
| **GRPDEPNW** | Dependent currently covered by employment-based insurance | GRPDEPNW indicates whether the respondent currently has employment-based health insurance coverage through a household member. | - |
| **GRPOWNNW** | Policyholder for current employment-based insurance | GRPOWNNW reports whether the respondent is the policy holder for their current employment-based insurance coverage. | - |
| **GRPOUTNW** | Current employment-based coverage covers non-household member | GRPOUTNW indicates whether the respondent's current employment-based insurance covers non-household members. | - |
| **GRPCOUTNW** | Current employment-based coverage provided by person outside the household | GRPCOUTNW indicates whether the respondent's current employment-based health insurance coverage is provided by someone living outside the household. | - |
| **GRPTYPNW** | Type of current employment-based plan | GRPTYPNW indicates whether the respondent's current employment-based health insurance policy covers a family, the policyholder and one other person, or the policyholder only. | - |
| **GRPWHONW** | Policyholder line number for current employment-based coverage | GRPWHONW indicates the line number of the policyholder of the respondent's current employment-based coverage for those who have employment-based insurance through a household member.

GRPWHONW is a pointer value that allows researchers to link a dependent covered by employment-based insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable. | - |
| **DPCOVLY** | Direct-purchase insurance coverage last year | DPCOVLY indicates whether the respondent was covered by directly purchased private health insurance during the past year. Both private plans acquired through the Affordable Care Act insurance marketplaces (MRKCOVLY) and outside of those marketplaces (NMCOVLY) are included in the definition of direct-purchase. | - |
| **DPDEPLY** | Dependent for direct-purchase insurance, previous year | DPDEPLY indicates whether the respondent had directly-purchased private health insurance coverage as a dependent during the previous year. The interviewer asked whether, at any time during the previous calendar year, anyone in the household was covered by such direct-purchase private insurance, and distinguished between policyholders and dependents covered by the plan through follow-up questions.     

Persons who were policyholders for such insurance are identified in the DPOWNLY variable.  Up to two household members who were policyholders for privately-purchased health insurance are identified in the DPWHO1 and DPWHO2 variables.  Using the DPWHO1, DPWHO2, and LINENO variables, researchers can identify the policyholder(s) whose privately-purchased insurance provided coverage for someone coded as "Yes" in DPDEPLY.  

Through programming in IPUMS CPS, other cases were added to the pool of positive responses for DPDEPLY in the 1996-2018 ASEC.  If the respondent mentioned dependent coverage on privately-purchased insurance in response to a catchall summary question on "other" health insurance plans (after hearing questions about many specific types of insurance coverage, including privately-purchased insurance), then that person was given a positive response for DPDEPLY in IPUMS CPS. | - |
| **DPOWNLY** | Policyholder for direct-purchase insurance, previous year | DPOWNLY indicates whether, during the previous calendar year, the respondent was the policyholder for health insurance that was purchased directly and that was not related to current or past employment.  The interviewer asked whether, at any time during the previous calendar year, anyone in the household was covered by direct-purchased private health insurance.  Follow-up questions identified the policyholder(s) and other persons covered by such insurance, including persons living outside the household.  

Through programming in IPUMS CPS, other cases were added to the pool of positive responses for DPOWNLY.  Such additions were made when the respondent mentioned being the policyholder for such insurance, when answering a catchall summary question on "other" health insurance plans, following questions about many specific types of insurance coverage.    

Persons who had direct-purchased private insurance coverage as dependents of a policyholder are identified in the DPDEPLY variable.  Up to two household members who were policyholders for direct-purchased private health insurance are identified in the DPWHO1 and DPWHO2 variables.  DPTYPLY indicates whether the policyholder's direct-purchased private health insurance covered the respondent only or also covered family members, and DPOUTLY reports whether the policyholder's coverage extended to persons outside the household. | - |
| **DPOUTLY** | Direct-purchase private coverage for non-hh member last year | DPOUTLY indicates the respondent's own policy for direct-purchase private health insurance provided coverage for someone outside the household last year. The interviewer asked whether, at any time during the previous calendar year, anyone in the household was covered by such direct-purchase private health insurance, and distinguished between policyholders and dependents covered by the plan through follow-up questions.  One such question, the basis for DPOUTLY, inquired whether the respondent's privately-purchased policy covered anyone outside the household.     

Persons who were policyholders for such insurance are identified in the DPOWNLY variable. DPDEPLY identifies household members covered as dependents by the privately-purchased insurance policy of someone in the household.  Up to two household members who were policyholders for privately-purchased health insurance are identified in the DPWHO1 and DPWHO2 variables. DPTYPLY indicates whether the policyholder's privately-purchased health insurance covered the respondent only or also covered family members. | - |
| **DPCOUTLY** | Direct-purchase insurance coverage through someone outside the household last year | DPCOUTLY reports whether the respondent was covered by the direct-purchase health insurance policy of someone outside the household during the previous year. | - |
| **DPTYPLY** | Type of direct-purchase insurance plan, previous year | DPTYPLY indicates whether a direct-purchase private insurance plan covered only the policyholder or also covered dependents, during the previous calendar year.  Policyholders of direct-purchased insurance are identified in the DPOWNLY variable. Persons who had coverage from such a plan as dependents of a policyholder last year are identified in the DPDEPLY variable. Whether the policyholder's direct-purchase insurance covered someone living in another household is reported in DPOUTLY. | - |
| **DPWHO1** | Line number of first policyholder of direct-purchase insurance, previous year | DPWHO1 and DPWHO2 indicate the line numbers of the first and second members of the household who were the policyholders for direct-purchased private insurance covering the respondent during the previous calendar year. DPWHO1 and DPWHO2 are pointer variables that allow researchers to link a dependent covered by direct-purchase insurance to the household members who were the policyholders of that insurance, using information in the LINENO variable.

Imagine, for example, that a male householder was the policyholder for direct-purchase insurance that also covered a co-resident child, and that the value of LINENO for the householder is 01. Imagine also that the wife of the householder was a policyholder for direct-purchase private insurance that covered the same co-resident child, and that the value of LINENO for the wife is 02. 

The value of DPWHO1 on the child's record would be 01, since the direct-purchase private family health care plan of the householder supplied the coverage for that child, as a dependent.  The value of DPWHO2 on the child's record would be 02, reflecting coverage as a dependent from the direct-purchase insurance policy of the spouse.  However, the policyholders themselves would be coded as 0 (not in universe) on these variables. 

Whether an individual was the policyholder for direct-purchase insurance last year is indicated by the DPOWNLY variable. Persons who had insurance coverage as dependents of a policyholder are identified in the DPDEPLY variable.  DPTYPLY indicates whether the policyholder's direct-purchase health insurance covered the respondent only or also covered family members last year, and DPOUTLY reports whether the policyholder's coverage extended to persons outside the household. | - |
| **DPCOVNW** | Currently covered by direct-purchase insurance | DPCOVNW indicates whether the respondent is currently covered by direct-purchase health insurance. Both private plans acquired through the Affordable Care Act insurance marketplaces (MRKCOVNW) and outside of those marketplaces (NMCOVNW) are included in the definition of direct-purchase. | - |
| **DPDEPNW** | Dependent currently covered by direct-purchase insurance | DPDEPNW indicates whether the respondent currently has direct-purchase health insurance coverage through a household member. | - |
| **DPOWNNW** | Policyholder for current direct-purchase insurance | DPOWNNW reports whether the respondent is the policy holder for their current direct-purchase insurance coverage. | - |
| **DPOUTNW** | Current direct-purchase coverage covers non-household member | DPOUTNW indicates whether the respondent's current direct-purchase insurance covers non-household members. | - |
| **DPCOUTNW** | Current direct-purchase coverage provided by person outside the household | DPCOUTNW indicates whether the respondent's current direct-purchase health insurance coverage is provided by someone living outside the household. | - |
| **DPTYPNW** | Type of current direct-purchase plan | DPTYPNW indicates whether the respondent's current direct-purchase health insurance policy covers a family, the policyholder and one other person, or the policyholder only. | - |
| **DPWHONW** | Policyholder line number for current direct-purchase coverage | DPWHONW indicates the line number of the policyholder of the respondent's current direct-purchase coverage for those who have direct-purchase insurance through a household member.

DPWHONW is a pointer value that allows researchers to link a dependent covered by direct-purchase insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable. | - |
| **MRKCOVLY** | Any Marketplace coverage last year | MRKCOVLY reports whether the respondent had any marketplace health insurance coverage during the previous year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces. Infants born after the calendar year are not included.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Individuals whose marketplace coverage was subsidized last year are reported in MRKSCOVLY, and those with unsubsidized coverage in MRKUCOVLY. | - |
| **MRKDEPLY** | Dependent covered by marketplace insurance last year | MRKDEPLY indicates whether the respondent had marketplace health insurance coverage through a household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Dependents whose marketplace coverage was subsidized last year are reported in MRKSDEPLY, and those with unsubsidized coverage in MRKUDEPLY. | - |
| **MRKOWNLY** | Policyholder for marketplace insurance last year | MRKOWNLY indicates whether the respondent was the policy holder for their marketplace insurance coverage last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholders whose marketplace coverage was subsidized last year are reported in MRKSOWNLY, and those with unsubsidized coverage in MRKUOWNLY. | - |
| **MRKOUTLY** | Marketplace insurance covered non-household member last year | MRKOUTLY indicates whether the respondent's marketplace insurance covered a non-household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Subsidized marketplace coverage for persons outside the household last year is reported in MRKSOUTLY, and those with unsubsidized coverage in MRKUOUTLY. | - |
| **MRKCOUTLY** | Marketplace insurance coverage through someone outside the household last year | MRKCOUTLY reports whether the respondent was covered by the marketplace health insurance policy of someone outside the household during the previous year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Individuals with subsidized marketplace coverage from someone outside the house are reported in MRKSCOUTLY, and those with unsubsidized coverage in MRKUCOUTLY. | - |
| **MRKTYPLY** | Type of marketplace coverage last year | MRKTYPLY indicates whether the respondent's marketplace health insurance policy covered a family, the policyholder and one other person, or the policyholder only last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. For individuals whose marketplace coverage was subsidized last year, the type of plan is reported in MRKSTYPLY, and plan types for those with unsubsidized coverage in MRKUTYPLY. | - |
| **MRKWHO1** | Line number of policy holder of marketplace insurance | MRKWHO1 indicates the line number of the policyholder of the respondent's marketplace coverage for those who had marketplace insurance through a household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

MRKWHO1 is a pointer value that allows researchers to link a dependent covered by marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Line numbers of policyholders whose marketplace coverage was subsidized last year are reported in MRKSWHO1, and those with unsubsidized coverage in MRKUWHO1. | - |
| **MRKCOVNW** | Currently covered by marketplace insurance | MRKCOVNW indicates whether the respondent is currently covered by marketplace health insurance. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Individuals whose marketplace coverage is subsidized are reported in MRKSCOVNW, and those with unsubsidized coverage in MRKUCOVNW. | - |
| **MRKDEPNW** | Dependent currently covered by marketplace insurance | MRKDEPNW indicates whether the respondent currently has marketplace health insurance coverage through a household member. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Dependents whose marketplace coverage is subsidized are reported in MRKSDEPNW, and those with unsubsidized coverage in MRKUDEPNW. | - |
| **MRKOWNNW** | Policyholder for current marketplace insurance | MRKOWNNW reports whether the respondent is the policy holder for their current marketplace insurance coverage. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholders whose current marketplace coverage is subsidized are reported in MRKSOWNNW, and those with unsubsidized coverage in MRKUOWNNW. | - |
| **MRKOUTNW** | Current marketplace coverage covers non-household member. | MRKOUTNW indicates whether the respondent's current marketplace insurance covers non-household members. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Current subsidized marketplace coverage for persons outside the household is reported in MRKSOUTNW, and those with unsubsidized coverage in MRKUOUTNW. | - |
| **MRKCOUTNW** | Current marketplace coverage provided by person outside the household. | MRKCOUTNW indicates whether the respondent's current marketplace health insurance coverage is provided by someone living outside the household. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Individuals with current subsidized marketplace coverage from someone outside the house are reported in MRKSCOUTNW, and those with unsubsidized coverage in MRKUCOUTNW. | - |
| **MRKTYPNW** | Type of current marketplace plan | MRKTYPNW indicates whether the respondent's current marketplace health insurance policy covers a family, the policyholder and one other person, or the policyholder only. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. For individuals whose marketplace coverage is subsidized last, the type of plan is reported in MRKSTYPNW, and plan types for those with unsubsidized coverage in MRKUTYPNW. | - |
| **MRKWHONW** | Policyholder line number for current marketplace coverage | MRKWHONW indicates the line number of the policyholder of the respondent's current marketplace coverage for those who have marketplace insurance through a household member. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

MRKWHONW is a pointer value that allows researchers to link a dependent covered by marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Line numbers of policyholders whose current marketplace coverage is subsidized are reported in MRKSWHONW, and those with unsubsidized coverage in MRKUWHONW. | - |
| **MRKSCOVLY** | Any subsidized marketplace coverage last year | MRKSCOVLY reports whether the respondent had any subsidized marketplace health insurance coverage during the previous year. Infants born after the calendar year are not included. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Individuals with unsubsidized marketplace insurance coverage last year are reported in MRKUCOVLY. | - |
| **MRKSDEPLY** | Dependent covered by subsidized marketplace insurance last year | MRKSDEPLY indicates whether the respondent had subsidized marketplace health insurance coverage through a household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Dependents with unsubsidized marketplace insurance coverage last year are reported in MRKUDEPLY. | - |
| **MRKSOWNLY** | Policyholder for subsidized marketplace insurance last year | MRKSOWNLY indicates whether the respondent was the policy holder for their subsidized marketplace insurance coverage last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholders of unsubsidized marketplace insurance plans last year are reported in MRKUOWNLY. | - |
| **MRKSOUTLY** | Subsidized marketplace insurance covered non-household member last year | MRKSOUTLY indicates whether the respondent's subsidized marketplace insurance covered a non-household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Unsubsidized coverage for non-household members last year is reported in MRKUOUTLY. | - |
| **MRKSCOUTLY** | Subsidized marketplace insurance coverage through someone outside the household last year | MRKSCOUTLY reports whether the respondent was covered by the subsidized marketplace health insurance policy of someone outside the household during the previous year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Unsubsidized coverage from someone outside the household last year is reported in MRKUCOUTLY. | - |
| **MRKSTYPLY** | Type of subsidized marketplace coverage last year | MRKSTYPLY indicates whether the respondent's subsidized marketplace health insurance policy covered a family, the policyholder and one other person, or the policyholder only last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. For individuals with unsubsidized marketplace insurance coverage last year, the plan type is reported in MRKUTYPLY. | - |
| **MRKSWHO1** | Line number of policy holder of subsidized marketplace insurance | MRKSWHO1 indicates the line number of the policyholder of the respondent's subsidized marketplace coverage for those who had subsidized marketplace insurance through a household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

MRKSWHO1 is a pointer value that allows researchers to link a dependent covered by subsidized marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholder line number for unsubsidized coverage last year is found in MRKUWHO1. | - |
| **MRKSCOVNW** | Currently covered by subsidized marketplace insurance | MRKSCOVNW indicates whether the respondent is currently covered by subsidized marketplace health insurance. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Individuals with current unsubsidized marketplace insurance coverage are reported in MRKUCOVNW. | - |
| **MRKSDEPNW** | Dependent currently covered by subsidized marketplace insurance | MRKSDEPNW indicates whether the respondent currently has subsidized marketplace health insurance coverage through a household member. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Dependents with current unsubsidized marketplace insurance coverage are reported in MRKUDEPNW. | - |
| **MRKSOWNNW** | Policyholder for current subsidized marketplace insurance | MRKSOWNNW reports whether the respondent is the policy holder for their current subsidized marketplace insurance coverage. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Current policyholders of unsubsidized marketplace insurance plans are reported in MRKUOWNNW. | - |
| **MRKSOUTNW** | Current subsidized marketplace coverage covers non-household member. | MRKSOUTNW indicates whether the respondent's current subsidized marketplace insurance covers non-household members. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Current unsubsidized coverage for non-household members is reported in MRKUOUTNW. | - |
| **MRKSCOUTNW** | Current subsidized marketplace coverage provided by person outside the household. | MRKSCOUTNW indicates whether the respondent's current subsidized marketplace health insurance coverage is provided by someone living outside the household. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Current unsubsidized coverage from someone outside the household is reported in MRKUCOUTNW. | - |
| **MRKSTYPNW** | Type of current subsidized marketplace plan | MRKSTYPNW indicates whether the respondent's current subsidized marketplace health insurance policy covers a family, the policyholder and one other person, or the policyholder only. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. For individuals with current unsubsidized marketplace insurance coverage, the pal type is reported in MRKUTYPNW. | - |
| **MRKSWHONW** | Policyholder line number for current subsidized marketplace coverage | MRKSWHONW indicates the line number of the policyholder of the respondent's current subsidized marketplace coverage for those who have subsidized marketplace insurance through a household member. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

MRKSWHONW is a pointer value that allows researchers to link a dependent covered by subsidized marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholder line number for current unsubsidized coverage is found in MRKUWHONW. | - |
| **MRKUCOVLY** | Any unsubsidized marketplace coverage last year | MRKUCOVLY reports whether the respondent had any unsubsidized marketplace health insurance coverage during the previous year. Infants born after the calendar year are not included. | - |
| **MRKUDEPLY** | Dependent covered by unsubsidized marketplace insurance last year | MRKUDEPLY indicates whether the respondent had unsubsidized marketplace health insurance coverage through a household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Dependents with subsidized marketplace insurance coverage last year are reported in MRKSDEPLY. | - |
| **MRKUOWNLY** | Policyholder for unsubsidized marketplace insurance last year | MRKUOWNLY indicates whether the respondent was the policy holder for their unsubsidized marketplace insurance coverage last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholders of subsidized marketplace insurance plans last year are reported in MRKSOWNLY. | - |
| **MRKUOUTLY** | Unsubsidized marketplace insurance covered non-household member last year | MRKUOUTLY indicates whether the respondent's unsubsidized marketplace insurance covered a non-household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Subsidized coverage for non-household members last year is reported in MRKSOUTLY. | - |
| **MRKUCOUTLY** | Unsubsidized marketplace insurance coverage through someone outside the household last year | MRKUCOUTLY reports whether the respondent was covered by the unsubsidized marketplace health insurance policy of someone outside the household during the previous year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Subsidized coverage from someone outside the household last year is reported in MRKSCOUTLY. | - |
| **MRKUTYPLY** | Type of unsubsidized marketplace coverage last year | MRKUTYPLY indicates whether the respondent's unsubsidized marketplace health insurance policy covered a family, the policyholder and one other person, or the policyholder only last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. For individuals with subsidized marketplace insurance coverage last year, the plan type is reported in MRKSTYPLY. | - |
| **MRKUWHO1** | Line number of policy holder of unsubsidized marketplace insurance | MRKUWHO1 indicates the line number of the policyholder of the respondent's unsubsidized marketplace coverage for those who had unsubsidized marketplace insurance through a household member last year. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

MRKUWHO1 is a pointer value that allows researchers to link a dependent covered by unsubsidized marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholder line number for subsidized coverage last year is found in MRKSWHO1. | - |
| **MRKUCOVNW** | Currently covered by unsubsidized marketplace insurance | MRKUCOVNW indicates whether the respondent is currently covered by unsubsidized marketplace health insurance. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Individuals with current subsidized marketplace insurance coverage are reported in MRKSCOVNW. | - |
| **MRKUDEPNW** | Dependent currently covered by unsubsidized marketplace insurance | MRKUDEPNW indicates whether the respondent currently has unsubsidized marketplace health insurance coverage through a household member. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Dependents with current subsidized marketplace insurance coverage are reported in MRKSDEPNW. | - |
| **MRKUOWNNW** | Policyholder for current unsubsidized marketplace insurance | MRKUOWNNW reports whether the respondent is the policy holder for their current unsubsidized marketplace insurance coverage. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Current policyholders of subsidized marketplace insurance plans are reported in MRKSOWNNW. | - |
| **MRKUOUTNW** | Current unsubsidized marketplace coverage covers non-household member. | MRKUOUTNW indicates whether the respondent's current unsubsidized marketplace insurance covers non-household members. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Current subsidized coverage for non-household members is reported in MRKSOUTNW. | - |
| **MRKUCOUTNW** | Current unsubsidized marketplace coverage provided by person outside the household. | MRKUCOUTNW indicates whether the respondent's current unsubsidized marketplace health insurance coverage is provided by someone living outside the household. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Current subsidized coverage from someone outside the household is reported in MRKSCOUTNW. | - |
| **MRKUTYPNW** | Type of current unsubsidized marketplace plan | MRKUTYPNW indicates whether the respondent's current unsubsidized marketplace health insurance policy covers a family, the policyholder and one other person, or the policyholder only. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. For individuals with current subsidized marketplace insurance coverage, the pal type is reported in MRKSTYPNW. | - |
| **MRKUWHONW** | Policyholder line number for current unsubsidized marketplace coverage | MRKUWHONW indicates the line number of the policyholder of the respondent's current unsubsidized marketplace coverage for those who have unsubsidized marketplace insurance through a household member. Marketplace health insurance plans are obtained through healthcare.gov or through equivalent state-run online marketplaces.

MRKUWHONW is a pointer value that allows researchers to link a dependent covered by unsubsidized marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Health insurance exchanges, or online marketplaces where one can purchase private health insurance, were established in all U.S. states by the 2010 Patient Protection and Affordable Care Act (commonly referred to as the ACA). For those without coverage available through an employer, a family member's coverage, or Medicaid or SCHIP, the ACA provides subsidies on a sliding scale for individuals whose Modified Adjusted Gross Income is between 100% and 400% of the federal poverty line. Policyholder line number for current subsidized coverage is found in MRKSWHONW. | - |
| **NMCOVLY** | Any non-marketplace coverage last year | NMCOVLY reports whether the respondent had any non-marketplace health insurance coverage during the previous year. Infants born after the calendar year are not included. 

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMDEPLY** | Dependent covered by non-marketplace insurance last year | NMDEPLY indicates whether the respondent had non-marketplace health insurance coverage through a household member last year.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMOWNLY** | Policyholder for non-marketplace insurance last year | NMOWNLY indicates whether the respondent was the policy holder for their non-marketplace insurance coverage last year.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMOUTLY** | Non-marketplace insurance covered non-household member last year | NMOUTLY indicates whether the respondent's non-marketplace insurance covered a non-household member last year.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMCOUTLY** | Non-marketplace insurance coverage through someone outside the household last year | NMCOUTLY reports whether the respondent was covered by the non-marketplace health insurance policy of someone outside the household during the previous year.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMTYPLY** | Type of non-marketplace coverage last year | NMTYPLY indicates whether the respondent's non-marketplace health insurance policy covered a family, the policyholder and one other person, or the policyholder only last year.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMWHO1** | Line number of policy holder of non-marketplace insurance | NMWHO1 indicates the line number of the policyholder of the respondent's non-marketplace coverage for those who had non-marketplace insurance through a household member last year.

NMWHO1 is a pointer value that allows researchers to link a dependent covered by non-marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMCOVNW** | Currently covered by non-marketplace insurance | NMCOVNW indicates whether the respondent is currently covered by non-marketplace health insurance.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMDEPNW** | Dependent currently covered by non-marketplace insurance | NMDEPNW indicates whether the respondent currently has non-marketplace health insurance coverage through a household member.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMOWNNW** | Policyholder for current non-marketplace insurance | NMOWNNW reports whether the respondent is the policy holder for their current non-marketplace insurance coverage.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMOUTNW** | Current unsubsidized marketplace coverage covers non-household member. | NMOUTNW indicates whether the respondent's current non-marketplace insurance covers non-household members.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMCOUTNW** | Current non-marketplace coverage provided by person outside the household. | NMCOUTNW indicates whether the respondent's current non-marketplace health insurance coverage is provided by someone living outside the household.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMTYPNW** | Type of current non-marketplace plan | NMTYPNW indicates whether the respondent's current non-marketplace health insurance policy covers a family, the policyholder and one other person, or the policyholder only.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **NMWHONW** | Policyholder line number for current non-marketplace coverage | NMWHONW indicates the line number of the policyholder of the respondent's current non-marketplace coverage for those who have non-marketplace insurance through a household member.

NMWHONW is a pointer value that allows researchers to link a dependent covered by non-marketplace insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

Non-marketplace coverage is private insurance purchased directly by the policyholder outside of the Affordable Care Act insurance exchanges. | - |
| **TRCCOVLY** | Covered by Champus/Tricare last year | TRCCOVLY identifies persons who had TRICARE coverage during the previous calendar year. TRICARE was formerly known as the Civilian Health and Medical Program Uniform Service of the Department of Defense, or CHAMPUS. CHAMPUS was a health care benefits program that provides in-patient and out-patient care from civilian sources and Military Treatment Facilities on a cost sharing basis.  In the late 1990s, a managed care approach was phased in, under the name TRICARE. Retired members of the military are eligible for such coverage, as are the dependents of active-duty, retired, and deceased military.    

Information on TRICARE coverage was collected through an initial question asking about health insurance from several government programs and a follow-up question about the name of the insurance plan for those who reported such coverage.  

Through programming in IPUMS CPS, other cases were added to the pool of positive responses for TRCCOVLY in 1996-2018.  If the respondent mentioned CHAMPUS or TRICARE coverage when answering a catchall summary question on "other" health insurance plans, after hearing questions about many specific types of insurance coverage (including CHAMPUS/TRICARE), then that person was given a positive response for TRCCOVLY in IPUMS CPS. | - |
| **TRCDEPLY** | Dependent covered by TRICARE last year | TRCDEPLY indicates whether the respondent had TRICARE health insurance coverage through a household member last year.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCOWNLY** | Policyholder for TRICARE last year | TRCOWNLY indicates whether the respondent was the policy holder for their TRICARE coverage last year.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCOUTLY** | TRICARE covered non-household member last year | TRCOUTLY indicates whether the respondent's TRICARE insurance covered a non-household member last year.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCCOUTLY** | TRICARE coverage through someone outside the household last year | TRCCOUTLY reports whether the respondent was covered by the TRICARE policy of someone outside the household during the previous year.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCTYPLY** | Type of TRICARE coverage last year | TRCTYPLY indicates whether the respondent's TRICARE health insurance policy covered a family, the policyholder and one other person, or the policyholder only last year.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCWHO1** | Line number of policy holder of TRICARE | TRCWHO1 indicates the line number of the policyholder of the respondent's TRICARE coverage for those who had marketplace insurance through a household member last year.

TRCWHO1 is a pointer value that allows researchers to link a dependent covered by TRICARE insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCCOVNW** | Currently covered by TRICARE | TRCCOVNW indicates whether the respondent is currently covered by marketplace health insurance.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCDEPNW** | Dependent currently covered by TRICARE | TRCDEPNW indicates whether the respondent currently has TRICARE coverage through a household member.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCOWNNW** | Policyholder for current TRICARE insurance | TRCOWNNW reports whether the respondent is the policy holder for their current TRICARE insurance coverage.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCOUTNW** | Current TRICARE coverage covers non-household member. | TRCOUTNW indicates whether the respondent's current TRICARE insurance covers non-household members.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCCOUTNW** | Current TRICARE coverage provided by person outside the household. | TRCCOUTNW indicates whether the respondent's current TRICARE health insurance coverage is provided by someone living outside the household.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCTYPNW** | Type of current TRICARE plan | TRCTYPNW indicates whether the respondent's current TRICARE policy covers a family, the policyholder and one other person, or the policyholder only.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **TRCWHONW** | Policyholder line number for current TRICARE coverage | TRCWHONW indicates the line number of the policyholder of the respondent's current TRICARE coverage for those who have TRICARE insurance through a household member.

TRCWHONW is a pointer value that allows researchers to link a dependent covered by TRICARE insurance to the household member who was the policyholder of that insurance, using information in the LINENO variable.

TRICARE, formerly known as CHAMPUS, provides civilian health benefits for U.S. armed forces personnel, military retirees, and their dependents. Beginning in 2019, TRICARE is considered private coverage. | - |
| **CHAMPVALY** | Covered by CHAMPVA last year | CHAMPVALY identifies persons who had health insurance coverage from the Civilian Health and Medical Program of the Department of Veteran's Affairs during the last year.  CHAMPVA is a health care benefits program for the spouse or widow(er) and for the children of a veteran who met one of the following four conditions: 1) is rated permanently and totally disabled due to a service-related disability; 2) was so rated at the time of death; 3) died of a service-related disability; or 4) died while on active duty.

Information on CHAMPVA coverage was collected through an initial question asking about health insurance from several government programs and a follow-up question about the name of the insurance plan for those who reported such coverage.  

Through programming in IPUMS CPS, other cases were added to the pool of positive responses for CHAMPVALY in 1996-2018.  If the respondent mentioned CHAMPVA coverage when answering a catchall summary question on "other" health insurance plans, after hearing questions about many specific types of insurance coverage (including CHAMPVA), then that person was given a positive response for CHAMPVALY in IPUMS CPS. | - |
| **CHAMPVANW** | Current CHAMPVA coverage | CHAMPVANW indicates whether the respondent is currently covered by CHAMPVA insurance.

For more information on health insurance variables, see [LINK].

For more information on changes in the 2019 ASEC, see [LINK]. | - |
| **INHCOVLY** | Covered by Indian Health Service last year | INHCOVLY identifies persons who had health insurance coverage through the Indian Health Service during the previous year. The Indian Health Service provides medical assistance to eligible American Indians at IHS facilities and helps pay the cost of selected health care services from other facilities. Information on health insurance from the Indian Health Service was collected through an initial question asking about health insurance from several government programs and a follow-up question about the name of the insurance plan for those who reported such coverage. 

Through programming in IPUMS CPS, other cases were added to the pool of positive responses for INHCOVLY in 1996-2018.  If the respondent mentioned coverage from the Indian Health Service when answering a catchall summary question on "other" health insurance plans--after hearing questions about many specific types of insurance--then that person was given a positive response for INHCOVLY in IPUMS CPS.

In its published tabulations on insurance coverage, based on CPS data, the Census Bureau initially grouped coverage from the Indian Health Service with Medicaid coverage.  Based on the advice of health care experts, beginning in 1997, the Census Bureau counted people with no coverage other than access to the Indian Health Service as part of the uninsured population. | - |
| **INHCOVNW** | Respondent currently covered by Indian Health Service | INHCOVNW indicates whether the respondent is currently covered by Indian Health Service. | - |
| **VACOVLY** | VACARE coverage last year | VACOVLY reports whether the respondent had VACARE coverage during the previous year. Infants born after the calendar year are not included. | - |
| **VACOVNW** | Current VACARE coverage | VACOVNW indicates whether the respondent is currently covered by VACARE health insurance. | - |
| **SCHIPLY** | State Children's Health Insurance Program coverage last year | SCHIPLY identifies children age 18 and younger who had health insurance coverage from the State Children's Health Insurance program during the previous calendar year.  Respondents were not questioned about SCHIP coverage (identified in the questionnaire as "the program that helps families get health insurance for children") if a child had Medicaid coverage. The computer-assisted interview program for the survey specified the name(s) for the SCHIP program(s) in the state where the household was located.

The State Children's Health Insurance Program was established under the Balanced Budget Act of 1997 and provides federal funds to states to expand health insurance coverage to uninsured low-income children. States use SCHIP money to develop separate child health programs, expand their Medicaid programs, or both.  Both Medicaid and SCHIP are means-tested government health insurance programs. 

The number of children with SCHIP coverage reported in the CPS is much lower than the figures shown by enrollment data from administrative records. For example, in 2001, the corresponding figures were 2.3 million children according to the survey data, versus 3.3 million children according to administrative records. There are several reasons for this discrepancy.  Some respondents are unclear about the exact source of their government health insurance coverage, and some insurance coverage funded by SCHIP was channeled through Medicaid (see CAIDLY). Thus, many households in which children had SCHIP coverage reported Medicaid or "other" insurance as the source of children's health insurance. Moreover, if a child had Medicaid coverage, the interviewer did not ask about SCHIP coverage. This skip pattern in the questions excludes some SCHIP recipients who had Medicaid coverage for some months and SCHIP coverage for other months during the preceding calendar year.       

A Census Bureau publication states, "Because the SCHIP questions were designed as Medicaid follow-up questions and not to try to capture all SCHIP coverage, we do not recommend using the new question to estimate state SCHIP coverage rates, but rather as an additional component of public health insurance."  The Bureau also recommends examining unweighted results to ascertain whether there are enough cases to support analysis of SCHIP coverage for states or population subgroups.  The Census Bureau does not publish summary measures with a threshold of less than 75,000 weighted cases, or approximately 35 to 40 unweighted sample cases.  Fluctuations over time or differences between states or subgroups in SCHIP coverage should not be given substantive weight unless an adequate number of cases underlie the analysis.  Factors that vary between states--such as whether the SCHIP program has a different name than the state Medicaid program, how long the program has been in place, and how widely publicized the program is--could also produce apparent differences between states in the extent of SCHIP coverage reported in the CPS.     

Finally, researchers should note that the skip patterns described above do not appear to have been followed in all cases.  In 2006 and 2007, for example, almost one quarter of children who were under age 19 and who were receiving Medicaid provided valid responses to the SCHIP item.  In 2008-2010, information on SCHIP recipiency exists for all children, regardless of their Medicaid status.  While this information may be useful to some, researchers who wish to be fully consistent with the guidelines provided by the CPS documentation should ensure that all Medicaid recipients are coded as missing for the SCHIPLY variable. | - |
| **SCHIPNW** | Current State Children's Health Insurance Program coverage | SCHIPNW identifies children age 18 and younger who currently have health insurance coverage from the State Children's Health Insurance program. | - |
| **MULTCOV** | Concurent health insurance coverage last year | MULTCOV indicates whether the respondent had multiple types of health insurance coverage at the same time during the last year. | - |
| **HIELIG** | Person was eligible to purchase employer's health insurance plan if one was offered | HIELIG indicates whether the respondent was eligible to purchase an employer's health insurance plan if one was offered. | - |
| **HINELIG1** | Ineligible for employer health insurance: Don't work enough hours per week or weeks per year | HINELIG1 indicates that the respondent was ineligible for employer-based health insurance if their employer offered it because they didn't work enough hours per week or enough weeks per year for that employer. | - |
| **HINELIG2** | Ineligible for employer health insurance: Contract or temporary employees not allowed in plan | HINELIG2 indicates that the respondent was ineligible for employer-based health insurance if their employer offered it because they were a contract or temporary employee. | - |
| **HINELIG3** | Ineligible for employer health insurance: Haven't worked for employer long enough to be covered | HINELIG3 indicates that the respondent was ineligible for employer-based health insurance if their employer offered it because they hadn't worked for that employer long enough. | - |
| **HINELIG4** | Ineligible for employer health insurance: Have a pre-existing condition | HINELIG4 indicates that the respondent was ineligible for employer-based health insurance if their employer offered it because they have a pre-existing condition. | - |
| **HINELIG5** | Ineligible for employer health insurance: Too expensive | HINELIG5 indicates that the respondent was ineligible for employer-based health insurance if their employer offered it because it is too expensive. | - |
| **HINELIG6** | Ineligible for employer health insurance: Other/specify | HINELIG6 indicates that the respondent was ineligible for employer-based health insurance if their employer offered it for some other reason besides not working enough (HINELIG1), being a contract or temporary employee (HINELIG2), not having worked long enough (HINELIG3), having a pre-existing condition (HINELIG4), or that the insurance is too expensive (HINELIG5). | - |
| **HINTAKE1** | Did not purchase employer health insurance: covered by another plan | HINTAKE1 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it because they were covered by another plan. | - |
| **HINTAKE2** | Did not purchase employer health insurance: Traded health insurance for higher pay | HINTAKE2 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it because they traded health insurance for higher pay. | - |
| **HINTAKE3** | Did not purchase employer health insurance: Too expensive | HINTAKE3 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it because it was too expensive. | - |
| **HINTAKE4** | Did not purchase employer health insurance: Don't need health insurance | HINTAKE4 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it because they didn't need health insurance. | - |
| **HINTAKE5** | Did not purchase employer health insurance: Have pre-existing condition | HINTAKE5 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it because they had a pre-existing condition. | - |
| **HINTAKE6** | Did not purchase employer health insurance: Haven't worked for employer long enough to be covered | HINTAKE6 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it because they haven't worked long enough for this employer to be covered. | - |
| **HINTAKE7** | Did not purchase employer health insurance: Contract or temp employees not allowed in plan | HINTAKE7 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it because they were contract or temp employees and not allowed on the plan. | - |
| **HINTAKE8** | Did not purchase employer health insurance: other/specify | HINTAKE8 indicates that the respondent was eligible for employer-based health insurance, but chose not to purchase it for some reason other than they were covered by another plan (HINTAKE1), they traded insurance for higher pay (HINTAKE2), it was too expensive (HINTAKE3), they didn't need health insurance (HINTAKE4), they had a pre-existing condition (HINTAKE5), they haven't worked for this employer long enough (HINTAKE6), or they were contract or temp employees and not allowed on the plan (HINTAKE7). | - |
| **HIOFFER** | Person's employer offers health insurance to any of its employees | HIOFFER indicates whether the respondent's employer offers a health insurance plan to any of its employees. | - |
| **QHIELIG** | Data quality flag for HIELIG [general version] | Data quality flag for HIELIG. | - |
| **QHIELIGD** | Data quality flag for HIELIG [detailed version] | Data quality flag for HIELIG. | - |
| **QHINELIG1** | Data quality flag for HINELIG1 [general version] | Data quality flag for HINELIG1. | - |
| **QHINELIG1D** | Data quality flag for HINELIG1 [detailed version] | Data quality flag for HINELIG1. | - |
| **QHINELIG2** | Data quality flag for HINELIG2 [general version] | Data quality flag for HINELIG2. | - |
| **QHINELIG2D** | Data quality flag for HINELIG2 [detailed version] | Data quality flag for HINELIG2. | - |
| **QHINELIG3** | Data quality flag for HINELIG3 [general version] | Data quality flag for HINELIG3. | - |
| **QHINELIG3D** | Data quality flag for HINELIG3 [detailed version] | Data quality flag for HINELIG3. | - |
| **QHINELIG4** | Data quality flag for HINELIG4 [general version] | Data quality flag for HINELIG4. | - |
| **QHINELIG4D** | Data quality flag for HINELIG4 [detailed version] | Data quality flag for HINELIG4. | - |
| **QHINELIG5** | Data quality flag for HINELIG5 [general version] | Data quality flag for HINELIG5. | - |
| **QHINELIG5D** | Data quality flag for HINELIG5 [detailed version] | Data quality flag for HINELIG5. | - |
| **QHINELIG6** | Data quality flag for HINELIG6 [general version] | Data quality flag for HINELIG6. | - |
| **QHINELIG6D** | Data quality flag for HINELIG6 [detailed version] | Data quality flag for HINELIG6. | - |
| **QHINTAKE1** | Data quality flag for HINTAKE1 [general version] | Data quality flag for HINTAKE1. | - |
| **QHINTAKE1D** | Data quality flag for HINTAKE1 [detailed version] | Data quality flag for HINTAKE1. | - |
| **QHINTAKE2** | Data quality flag for HINTAKE2 [general version] | Data quality flag for HINTAKE2. | - |
| **QHINTAKE2D** | Data quality flag for HINTAKE2 [detailed version] | Data quality flag for HINTAKE2. | - |
| **QHINTAKE3** | Data quality flag for HINTAKE3 [general version] | Data quality flag for HINTAKE3. | - |
| **QHINTAKE3D** | Data quality flag for HINTAKE3 [detailed version] | Data quality flag for HINTAKE3. | - |
| **QHINTAKE4** | Data quality flag for HINTAKE4 [general version] | Data quality flag for HINTAKE4. | - |
| **QHINTAKE4D** | Data quality flag for HINTAKE4 [detailed version] | Data quality flag for HINTAKE4. | - |
| **QHINTAKE5** | Data quality flag for HINTAKE5 [general version] | Data quality flag for HINTAKE5. | - |
| **QHINTAKE5D** | Data quality flag for HINTAKE5 [detailed version] | Data quality flag for HINTAKE5. | - |
| **QHINTAKE6** | Data quality flag for HINTAKE6 [general version] | Data quality flag for HINTAKE6. | - |
| **QHINTAKE6D** | Data quality flag for HINTAKE6 [detailed version] | Data quality flag for HINTAKE6. | - |
| **QHINTAKE7** | Data quality flag for HINTAKE7 [general version] | Data quality flag for HINTAKE7. | - |
| **QHINTAKE7D** | Data quality flag for HINTAKE7 [detailed version] | Data quality flag for HINTAKE7. | - |
| **QHINTAKE8** | Data quality flag for HINTAKE8 [general version] | Data quality flag for HINTAKE8. | - |
| **QHINTAKE8D** | Data quality flag for HINTAKE8 [detailed version] | Data quality flag for HINTAKE8. | - |
| **QHIOFFER** | Data quality flag for HIOFFER [general version] | Data quality flag for HIOFFER. | - |
| **QHIOFFERD** | Data quality flag for HIOFFER [detailed version] | Data quality flag for HIOFFER. | - |
| **OUT** | Covered by policy of person outside the household | OUT indicates whether, during the previous calendar year, the respondent had health insurance provided by the policy of someone living outside the household.  The interviewer asked whether anyone in the household was covered by the health plan of someone who did not live in that household, and, if "Yes," who had such coverage.

Through programming in IPUMS-CPS, other cases were added to the pool of positive responses for OUT.  Such additions were made when the respondent mentioned having coverage from the policy of someone outside the household, when answering a catchall summary question on "other" health insurance plans that followed questions about many specific types of insurance coverage. | - |

---

## 2. Value Labels

### MONTH : Month
| Code | Label |
| :--- | :--- |
| 01 | January |
| 02 | February |
| 03 | March |
| 04 | April |
| 05 | May |
| 06 | June |
| 07 | July |
| 08 | August |
| 09 | September |
| 10 | October |
| 11 | November |
| 12 | December |

### ASECFLAG : Flag for ASEC
| Code | Label |
| :--- | :--- |
| 1 | ASEC |
| 2 | March Basic |

### HHINTYPE : Type of household
| Code | Label |
| :--- | :--- |
| 1 | Interview |
| 2 | Type A non-interview |
| 3 | Type B/C non-interview |

### REGION : Region and division
| Code | Label |
| :--- | :--- |
| 11 | New England Division |
| 12 | Middle Atlantic Division |
| 21 | East North Central Division |
| 22 | West North Central Division |
| 31 | South Atlantic Division |
| 32 | East South Central Division |
| 33 | West South Central Division |
| 41 | Mountain Division |
| 42 | Pacific Division |
| 97 | State not identified |

### STATEFIP : State (FIPS code)
| Code | Label |
| :--- | :--- |
| 01 | Alabama |
| 02 | Alaska |
| 04 | Arizona |
| 05 | Arkansas |
| 06 | California |
| 08 | Colorado |
| 09 | Connecticut |
| 10 | Delaware |
| 11 | District of Columbia |
| 12 | Florida |
| 13 | Georgia |
| 15 | Hawaii |
| 16 | Idaho |
| 17 | Illinois |
| 18 | Indiana |
| 19 | Iowa |
| 20 | Kansas |
| 21 | Kentucky |
| 22 | Louisiana |
| 23 | Maine |
| 24 | Maryland |
| 25 | Massachusetts |
| 26 | Michigan |
| 27 | Minnesota |
| 28 | Mississippi |
| 29 | Missouri |
| 30 | Montana |
| 31 | Nebraska |
| 32 | Nevada |
| 33 | New Hampshire |
| 34 | New Jersey |
| 35 | New Mexico |
| 36 | New York |
| 37 | North Carolina |
| 38 | North Dakota |
| 39 | Ohio |
| 40 | Oklahoma |
| 41 | Oregon |
| 42 | Pennsylvania |
| 44 | Rhode Island |
| 45 | South Carolina |
| 46 | South Dakota |
| 47 | Tennessee |
| 48 | Texas |
| 49 | Utah |
| 50 | Vermont |
| 51 | Virginia |
| 53 | Washington |
| 54 | West Virginia |
| 55 | Wisconsin |
| 56 | Wyoming |
| 61 | Maine-New Hampshire-Vermont |
| 65 | Montana-Idaho-Wyoming |
| 68 | Alaska-Hawaii |
| 69 | Nebraska-North Dakota-South Dakota |
| 70 | Maine-Massachusetts-New Hampshire-Rhode Island-Vermont |
| 71 | Michigan-Wisconsin |
| 72 | Minnesota-Iowa |
| 73 | Nebraska-North Dakota-South Dakota-Kansas |
| 74 | Delaware-Virginia |
| 75 | North Carolina-South Carolina |
| 76 | Alabama-Mississippi |
| 77 | Arkansas-Oklahoma |
| 78 | Arizona-New Mexico-Colorado |
| 79 | Idaho-Wyoming-Utah-Montana-Nevada |
| 80 | Alaska-Washington-Hawaii |
| 81 | New Hampshire-Maine-Vermont-Rhode Island |
| 83 | South Carolina-Georgia |
| 84 | Kentucky-Tennessee |
| 85 | Arkansas-Louisiana-Oklahoma |
| 87 | Iowa-N Dakota-S Dakota-Nebraska-Kansas-Minnesota-Missouri |
| 88 | Washington-Oregon-Alaska-Hawaii |
| 89 | Montana-Wyoming-Colorado-New Mexico-Utah-Nevada-Arizona |
| 90 | Delaware-Maryland-Virginia-West Virginia |
| 99 | State not identified |

### STATECENSUS : State (Census code)
| Code | Label |
| :--- | :--- |
| 00 | Unknown |
| 11 | Maine |
| 12 | New Hampshire |
| 13 | Vermont |
| 14 | Massachusetts |
| 15 | Rhode Island |
| 16 | Connecticut |
| 19 | Maine, New Hampshire, Vermont, Rhode Island |
| 21 | New York |
| 22 | New Jersey |
| 23 | Pennsylvania |
| 31 | Ohio |
| 32 | Indiana |
| 33 | Illinois |
| 34 | Michigan |
| 35 | Wisconsin |
| 39 | Michigan, Wisconsin |
| 41 | Minnesota |
| 42 | Iowa |
| 43 | Missouri |
| 44 | North Dakota |
| 45 | South Dakota |
| 46 | Nebraska |
| 47 | Kansas |
| 49 | Minnesota, Iowa, Missouri, North Dakota, South Dakota, Nebraska, Kansas |
| 50 | Delaware, Maryland, Virginia, West Virginia |
| 51 | Delaware |
| 52 | Maryland |
| 53 | District of Columbia |
| 54 | Virginia |
| 55 | West Virginia |
| 56 | North Carolina |
| 57 | South Carolina |
| 58 | Georgia |
| 59 | Florida |
| 60 | South Carolina, Georgia |
| 61 | Kentucky |
| 62 | Tennessee |
| 63 | Alabama |
| 64 | Mississippi |
| 67 | Kentucky, Tennessee |
| 69 | Alabama, Mississippi |
| 71 | Arkansas |
| 72 | Louisiana |
| 73 | Oklahoma |
| 74 | Texas |
| 79 | Arkansas, Louisiana, Oklahoma |
| 81 | Montana |
| 82 | Idaho |
| 83 | Wyoming |
| 84 | Colorado |
| 85 | New Mexico |
| 86 | Arizona |
| 87 | Utah |
| 88 | Nevada |
| 89 | Montana, Idaho, Wyoming, Colorado, New Mexico, Arizona, Utah, Nevada |
| 91 | Washington |
| 92 | Oregon |
| 93 | California |
| 94 | Alaska |
| 95 | Hawaii |
| 99 | Washington, Oregon, Alaska, Hawaii |

### METRO : Metropolitan and central/principal city status
| Code | Label |
| :--- | :--- |
| 0 | Not identified |
| 1 | Not in metropolitan area |
| 2 | In central/principal city |
| 3 | Not in central/principal city |
| 4 | Central/principal city status not identified |
| 9 | Missing/unknown |

### CBSASZ : Core-based (metro/micro) statistical area size
| Code | Label |
| :--- | :--- |
| 00 | Not identified or nonmetropolitan |
| 01 | 100,000 - 249,999 |
| 02 | 250,000 - 499,999 |
| 03 | 500,000 - 999,999 |
| 04 | 1,000,000 - 2,499,999 |
| 05 | 2,500,000 - 4,999,999 |
| 06 | 5,000,000 or more |

### OWNERSHP : Ownership of dwelling
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 10 | Owned or being bought |
| 21 | No cash rent |
| 22 | With cash rent |

### PUBHOUS : Living in public housing
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### RENTSUB : Paying lower rent due to government subsidy
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### HEATSUB : Received energy subsidy
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### FOODSTMP : Food stamp recipiency
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### STAMPMO : Number of months received food stamps
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | One |
| 02 | Two |
| 03 | Three |
| 04 | Four |
| 05 | Five |
| 06 | Six |
| 07 | Seven |
| 08 | Eight |
| 09 | Nine |
| 10 | Ten |
| 11 | Eleven |
| 12 | Twelve |

### FAMINC : Family income of householder
| Code | Label |
| :--- | :--- |
| 100 | Under $5,000 |
| 110 | Under $1,000 |
| 111 | Under $500 |
| 112 | $500 - 999 |
| 120 | $1,000 - 1,999 |
| 121 | $1,000 - 1,499 |
| 122 | $1,500-1,999 |
| 130 | $2,000 - 2,999 |
| 131 | $2,000 - 2,499 |
| 132 | $2,500 - 2,999 |
| 140 | $3,000 - 3,999 |
| 141 | $3,000 - 3,499 |
| 142 | $3,500 - 3,999 |
| 150 | $4,000 - 4,999 |
| 200 | $5,000 - 7,999 |
| 210 | $5,000 - 7,499 |
| 220 | $5,000 - 5,999 |
| 230 | $6,000 - 7,999 |
| 231 | $6,000 - 7,499 |
| 232 | $6,000 - 6,999 |
| 233 | $7,000 - 7,499 |
| 234 | $7,000 - 7,999 |
| 300 | $7,500 - 9,999 |
| 310 | $7,500 - 7,999 |
| 320 | $8,000 - 8,499 |
| 330 | $8,500 - 8,999 |
| 340 | $8,000 - 8,999 |
| 350 | $9,000 - 9,999 |
| 400 | $10,000 - 14,999 |
| 410 | $10,000 - 10,999 |
| 420 | $11,000 - 11,999 |
| 430 | $10,000 - 12,499 |
| 440 | $10,000 - 11,999 |
| 450 | $12,000 - 12,999 |
| 460 | $12,000 - 14,999 |
| 470 | $12,500 - 14,999 |
| 480 | $13,000 - 13,999 |
| 490 | $14,000 - 14,999 |
| 500 | $15,000 - 19,999 |
| 510 | $15,000 - 15,999 |
| 520 | $16,000 - 16,999 |
| 530 | $17,000 - 17,999 |
| 540 | $15,000 - 17,499 |
| 550 | $17,500 - 19,999 |
| 560 | $18,000 - 19,999 |
| 600 | $20,000 - 24,999 |
| 700 | $25,000 - 49,999 |
| 710 | $25,000 - 29,999 |
| 720 | $30,000 - 34,999 |
| 730 | $35,000 - 39,999 |
| 740 | $40,000 - 49,999 |
| 800 | $50,000 and over |
| 810 | $50,000 - 74,999 |
| 820 | $50,000 - 59,999 |
| 830 | $60,000 - 74,999 |
| 840 | $75,000 and over |
| 841 | $75,000 - 99,999 |
| 842 | $100,000 - 149,999 |
| 843 | $150,000 and over |
| 995 | Missing |
| 996 | Refused |
| 997 | Don't know |
| 999 | Blank |

### UNITSSTR : Units in structure
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | Mobile home or trailer |
| 05 | 2 family building |
| 06 | 3-4 family building |
| 07 | 5-9 family building |
| 11 | One unit, unspecified type |
| 12 | 10+ units in structure |

### RELATE : Relationship to household head
| Code | Label |
| :--- | :--- |
| 0101 | Head/householder |
| 0201 | Spouse |
| 0202 | Opposite sex spouse |
| 0203 | Same sex spouse |
| 0301 | Child |
| 0303 | Stepchild |
| 0501 | Parent |
| 0701 | Sibling |
| 0901 | Grandchild |
| 1001 | Other relatives, n.s. |
| 1113 | Partner/roommate |
| 1114 | Unmarried partner |
| 1116 | Opposite sex unmarried partner |
| 1117 | Same sex unmarried partner |
| 1115 | Housemate/roomate |
| 1241 | Roomer/boarder/lodger |
| 1242 | Foster children |
| 1260 | Other nonrelatives |
| 9900 | Relationship unknown |
| 9999 | NIU |

### AGE : Age
| Code | Label |
| :--- | :--- |
| 00 | Under 1 year |
| 01 | 1 |
| 02 | 2 |
| 03 | 3 |
| 04 | 4 |
| 05 | 5 |
| 06 | 6 |
| 07 | 7 |
| 08 | 8 |
| 09 | 9 |
| 10 | 10 |
| 11 | 11 |
| 12 | 12 |
| 13 | 13 |
| 14 | 14 |
| 15 | 15 |
| 16 | 16 |
| 17 | 17 |
| 18 | 18 |
| 19 | 19 |
| 20 | 20 |
| 21 | 21 |
| 22 | 22 |
| 23 | 23 |
| 24 | 24 |
| 25 | 25 |
| 26 | 26 |
| 27 | 27 |
| 28 | 28 |
| 29 | 29 |
| 30 | 30 |
| 31 | 31 |
| 32 | 32 |
| 33 | 33 |
| 34 | 34 |
| 35 | 35 |
| 36 | 36 |
| 37 | 37 |
| 38 | 38 |
| 39 | 39 |
| 40 | 40 |
| 41 | 41 |
| 42 | 42 |
| 43 | 43 |
| 44 | 44 |
| 45 | 45 |
| 46 | 46 |
| 47 | 47 |
| 48 | 48 |
| 49 | 49 |
| 50 | 50 |
| 51 | 51 |
| 52 | 52 |
| 53 | 53 |
| 54 | 54 |
| 55 | 55 |
| 56 | 56 |
| 57 | 57 |
| 58 | 58 |
| 59 | 59 |
| 60 | 60 |
| 61 | 61 |
| 62 | 62 |
| 63 | 63 |
| 64 | 64 |
| 65 | 65 |
| 66 | 66 |
| 67 | 67 |
| 68 | 68 |
| 69 | 69 |
| 70 | 70 |
| 71 | 71 |
| 72 | 72 |
| 73 | 73 |
| 74 | 74 |
| 75 | 75 |
| 76 | 76 |
| 77 | 77 |
| 78 | 78 |
| 79 | 79 |
| 80 | 80 |
| 81 | 81 |
| 82 | 82 |
| 83 | 83 |
| 84 | 84 |
| 85 | 85 |
| 86 | 86 |
| 87 | 87 |
| 88 | 88 |
| 89 | 89 |
| 90 | 90 (90+, 1988-2002) |
| 91 | 91 |
| 92 | 92 |
| 93 | 93 |
| 94 | 94 |
| 95 | 95 |
| 96 | 96 |
| 97 | 97 |
| 98 | 98 |
| 99 | 99+ |

### SEX : Sex
| Code | Label |
| :--- | :--- |
| 1 | Male |
| 2 | Female |
| 9 | NIU |

### RACE : Race
| Code | Label |
| :--- | :--- |
| 100 | White |
| 200 | Black |
| 300 | American Indian/Aleut/Eskimo |
| 650 | Asian or Pacific Islander |
| 651 | Asian only |
| 652 | Hawaiian/Pacific Islander only |
| 700 | Other (single) race, n.e.c. |
| 801 | White-Black |
| 802 | White-American Indian |
| 803 | White-Asian |
| 804 | White-Hawaiian/Pacific Islander |
| 805 | Black-American Indian |
| 806 | Black-Asian |
| 807 | Black-Hawaiian/Pacific Islander |
| 808 | American Indian-Asian |
| 809 | Asian-Hawaiian/Pacific Islander |
| 810 | White-Black-American Indian |
| 811 | White-Black-Asian |
| 812 | White-American Indian-Asian |
| 813 | White-Asian-Hawaiian/Pacific Islander |
| 814 | White-Black-American Indian-Asian |
| 815 | American Indian-Hawaiian/Pacific Islander |
| 816 | White-Black--Hawaiian/Pacific Islander |
| 817 | White-American Indian-Hawaiian/Pacific Islander |
| 818 | Black-American Indian-Asian |
| 819 | White-American Indian-Asian-Hawaiian/Pacific Islander |
| 820 | Two or three races, unspecified |
| 830 | Four or five races, unspecified |
| 999 | Blank |

### MARST : Marital status
| Code | Label |
| :--- | :--- |
| 1 | Married, spouse present |
| 2 | Married, spouse absent |
| 3 | Separated |
| 4 | Divorced |
| 5 | Widowed |
| 6 | Never married/single |
| 7 | Widowed or Divorced |
| 9 | NIU |

### POPSTAT : Adult civilian, armed forces, or child
| Code | Label |
| :--- | :--- |
| 1 | Adult civilian |
| 2 | Armed Forces |
| 3 | Child |

### ASIAN : Asian subgroup
| Code | Label |
| :--- | :--- |
| 10 | Asian Indian |
| 20 | Chinese |
| 30 | Filipino |
| 40 | Japanese |
| 50 | Korean |
| 60 | Vietnamese |
| 70 | Other Asian |
| 99 | NIU |

### VETSTAT : Veteran status
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No service |
| 2 | Yes |
| 9 | Unknown |

### OCC50LY : Occupation last year, 1950 basis
| Code | Label |
| :--- | :--- |
| 000 | Accountants and auditors |
| 001 | Actors and actresses |
| 002 | Airplane pilots and navigators |
| 003 | Architects |
| 004 | Artists and art teachers |
| 005 | Athletes |
| 006 | Authors |
| 007 | Chemists |
| 008 | Chiropractors |
| 009 | Clergymen |
| 010 | College presidents and deans |
| 012 | Agricultural sciences |
| 013 | Biological sciences |
| 014 | Chemistry |
| 015 | Economics |
| 016 | Engineering |
| 017 | Geology and geophysics |
| 018 | Mathematics |
| 019 | Medical sciences |
| 023 | Physics |
| 024 | Psychology |
| 025 | Statistics |
| 026 | Natural science (n.e.c.) |
| 027 | Social sciences (n.e.c.) |
| 028 | Nonscientific subjects |
| 029 | Subject not specified |
| 031 | Dancers and dancing teachers |
| 032 | Dentists |
| 033 | Designers |
| 034 | Dieticians and nutritionists |
| 035 | Draftsmen |
| 036 | Editors and reporters |
| 041 | Engineers, aeronautical |
| 042 | Engineers, chemical |
| 043 | Engineers, civil |
| 044 | Engineers, electrical |
| 045 | Engineers, industrial |
| 046 | Engineers, mechanical |
| 047 | Engineers, metallurgical, metallurgists |
| 048 | Engineers, mining |
| 049 | Engineers (n.e.c.) |
| 051 | Entertainers (n.e.c.) |
| 052 | Farm and home management advisors |
| 053 | Foresters and conservationists |
| 054 | Funeral directors and embalmers |
| 055 | Lawyers and judges |
| 056 | Librarians |
| 057 | Musicians and music teachers |
| 058 | Nurses, professional |
| 059 | Nurses, student professional |
| 061 | Agricultural scientists |
| 062 | Biological scientists |
| 063 | Geologists and geophysicists |
| 067 | Mathematicians |
| 068 | Physicists |
| 069 | Miscellaneous natural scientists |
| 070 | Optometrists |
| 071 | Osteopaths |
| 072 | Personnel and labor relations workers |
| 073 | Pharmacists |
| 074 | Photographers |
| 075 | Physicians and surgeons |
| 076 | Radio operators |
| 077 | Recreation and group workers |
| 078 | Religious workers |
| 079 | Social and welfare workers, except group |
| 081 | Economists |
| 082 | Psychologists |
| 083 | Statisticians and actuaries |
| 084 | Miscellaneous social scientists |
| 091 | Sports instructors and officials |
| 092 | Surveyors |
| 093 | Teachers (n.e.c.) |
| 094 | Technicians, medical and dental |
| 095 | Technicians, testing |
| 096 | Technicians (n.e.c.) |
| 097 | Therapists and healers (n.e.c.) |
| 098 | Veterinarians |
| 099 | Professional, technical and kindred workers (n.e.c.) |
| 100 | Farmers (owners and tenants) |
| 123 | Farm managers |
| 200 | Buyers and department heads, store |
| 201 | Buyers and shippers, farm products |
| 203 | Conductors, railroad |
| 204 | Credit men |
| 205 | Floormen and floor managers, store |
| 210 | Inspectors, public administration |
| 230 | Managers and superintendents, building |
| 240 | Officers, pilots, pursers and engineers, ship |
| 250 | Officials and administrators (n.e.c.), public administration |
| 260 | Officials, lodge, society, union, etc. |
| 270 | Postmasters |
| 280 | Purchasing agents and buyers (n.e.c.) |
| 290 | Managers, officials, and proprietors (n.e.c.) |
| 300 | Agents (n.e.c.) |
| 301 | Attendants and assistants, library |
| 302 | Attendants, physicians and dentists office |
| 304 | Baggagemen, transportation |
| 305 | Bank tellers |
| 310 | Bookkeepers |
| 320 | Cashiers |
| 321 | Collectors, bill and account |
| 322 | Dispatchers and starters, vehicle |
| 325 | Express messengers and railway mail clerks |
| 335 | Mail carriers |
| 340 | Messengers and office boys |
| 341 | Office machine operators |
| 342 | Shipping and receiving clerks |
| 350 | Stenographers, typists, and secretaries |
| 360 | Telegraph messengers |
| 365 | Telegraph operators |
| 370 | Telephone operators |
| 380 | Ticket, station, and express agents |
| 390 | Clerical and kindred workers (n.e.c.) |
| 400 | Advertising agents and salesmen |
| 410 | Auctioneers |
| 420 | Demonstrators |
| 430 | Hucksters and peddlers |
| 450 | Insurance agents and brokers |
| 460 | Newsboys |
| 470 | Real estate agents and brokers |
| 480 | Stock and bond salesmen |
| 490 | Salesmen and sales clerks (n.e.c.) |
| 500 | Bakers |
| 501 | Blacksmiths |
| 502 | Bookbinders |
| 503 | Boilermakers |
| 504 | Brickmasons, stonemasons, and tile setters |
| 505 | Cabinetmakers |
| 510 | Carpenters |
| 511 | Cement and concrete finishers |
| 512 | Compositors and typesetters |
| 513 | Cranemen, derrickmen, and hoistmen |
| 514 | Decorators and window dressers |
| 515 | Electricians |
| 520 | Electrotypers and stereotypers |
| 521 | Engravers, except photoengravers |
| 522 | Excavating, grading, and road machinery operators |
| 523 | Foremen (n.e.c.) |
| 524 | Forgemen and hammermen |
| 525 | Furriers |
| 530 | Glaziers |
| 531 | Heat treaters, annealers, temperers |
| 532 | Inspectors, scalers, and graders, log and lumber |
| 533 | Inspectors (n.e.c.) |
| 534 | Jewelers, watchmakers, goldsmiths, and silversmiths |
| 535 | Job setters, metal |
| 540 | Linemen and servicemen, telegraph, telephone, and power |
| 541 | Locomotive engineers |
| 542 | Locomotive firemen |
| 543 | Loom fixers |
| 544 | Machinists |
| 545 | Mechanics and repairmen, airplane |
| 550 | Mechanics and repairmen, automobile |
| 551 | Mechanics and repairmen, office machine |
| 552 | Mechanics and repairmen, radio and television |
| 553 | Mechanics and repairmen, railroad and car shop |
| 554 | Mechanics and repairmen (n.e.c.) |
| 555 | Millers, grain, flour, feed, etc. |
| 560 | Millwrights |
| 561 | Molders, metal |
| 562 | Motion picture projectionists |
| 563 | Opticians and lens grinders and polishers |
| 564 | Painters, construction and maintenance |
| 565 | Paperhangers |
| 570 | Pattern and model makers, except paper |
| 571 | Photoengravers and lithographers |
| 572 | Piano and organ tuners and repairmen |
| 573 | Plasterers |
| 574 | Plumbers and pipe fitters |
| 575 | Pressmen and plate printers, printing |
| 580 | Rollers and roll hands, metal |
| 581 | Roofers and slaters |
| 582 | Shoemakers and repairers, except factory |
| 583 | Stationary engineers |
| 584 | Stone cutters and stone carvers |
| 585 | Structural metal workers |
| 590 | Tailors and tailoresses |
| 591 | Tinsmiths, coppersmiths, and sheet metal workers |
| 592 | Tool makers, and die makers and setters |
| 593 | Upholsterers |
| 594 | Craftsmen and kindred workers (n.e.c.) |
| 595 | Members of the armed services |
| 600 | Apprentice auto mechanics |
| 601 | Apprentice bricklayers and masons |
| 602 | Apprentice carpenters |
| 603 | Apprentice electricians |
| 604 | Apprentice machinists and toolmakers |
| 605 | Apprentice mechanics, except auto |
| 610 | Apprentice plumbers and pipe fitters |
| 611 | Apprentices, building trades (n.e.c.) |
| 612 | Apprentices, metalworking trades (n.e.c.) |
| 613 | Apprentices, printing trades |
| 614 | Apprentices, other specified trades |
| 615 | Apprentices, trade not specified |
| 620 | Asbestos and insulation workers |
| 621 | Attendants, auto service and parking |
| 622 | Blasters and powdermen |
| 623 | Boatmen, canalmen, and lock keepers |
| 624 | Brakemen, railroad |
| 625 | Bus drivers |
| 630 | Chainmen, rodmen, and axmen, surveying |
| 631 | Conductors, bus and street railway |
| 632 | Deliverymen and routemen |
| 633 | Dressmakers and seamstresses, except factory |
| 634 | Dyers |
| 635 | Filers, grinders, and polishers, metal |
| 640 | Fruit, nut, veg graders and packers, except factory |
| 641 | Furnacemen, smeltermen and pourers |
| 642 | Heaters, metal |
| 643 | Laundry and dry cleaning operatives |
| 644 | Meat cutters, except slaughter and packing house |
| 645 | Milliners |
| 650 | Mine operatives and laborers |
| 660 | Motormen, mine, factory, logging camp, etc. |
| 661 | Motormen, street, subway, and elevated railway |
| 662 | Oilers and greaser, except auto |
| 670 | Painters, except construction or maintenance |
| 671 | Photographic process workers |
| 672 | Power station operators |
| 673 | Sailors and deck hands |
| 674 | Sawyers |
| 675 | Spinners, textile |
| 680 | Stationary firemen |
| 681 | Switchmen, railroad |
| 682 | Taxicab drivers and chauffers |
| 683 | Truck and tractor drivers |
| 684 | Weavers, textile |
| 685 | Welders and flame cutters |
| 690 | Operative and kindred workers (n.e.c.) |
| 700 | Housekeepers, private household |
| 710 | Laundressses, private household |
| 720 | Private household workers (n.e.c.) |
| 730 | Attendants, hospital and other institution |
| 731 | Attendants, professional and personal service (n.e.c.) |
| 732 | Attendants, recreation and amusement |
| 740 | Barbers, beauticians, and manicurists |
| 750 | Bartenders |
| 751 | Bootblacks |
| 752 | Boarding and lodging house keepers |
| 753 | Charwomen and cleaners |
| 754 | Cooks, except private household |
| 760 | Counter and fountain workers |
| 761 | Elevator operators |
| 762 | Firemen, fire protection |
| 763 | Guards, watchmen, and doorkeepers |
| 764 | Housekeepers and stewards, except private household |
| 770 | Janitors and sextons |
| 771 | Marshals and constables |
| 772 | Midwives |
| 773 | Policemen and detectives |
| 780 | Porters |
| 781 | Practical nurses |
| 782 | Sheriffs and bailiffs |
| 783 | Ushers, recreation and amusement |
| 784 | Waiters and waitresses |
| 785 | Watchmen (crossing) and bridge tenders |
| 790 | Service workers, except private household (n.e.c.) |
| 810 | Farm foremen |
| 820 | Farm laborers, wage workers |
| 830 | Farm laborers, unpaid family workers |
| 840 | Farm service laborers, self-employed |
| 910 | Fishermen and oystermen |
| 920 | Garage laborers and car washers and greasers |
| 930 | Gardeners, except farm, and groundskeepers |
| 940 | Longshoremen and stevedores |
| 950 | Lumbermen, raftsmen, and woodchoppers |
| 960 | Teamsters |
| 970 | Laborers (n.e.c.) |
| 997 | Unknown |
| 999 | NIU |

### IND50LY : Industry last year, 1950 basis
| Code | Label |
| :--- | :--- |
| 000 | NIU |
| 105 | Agriculture |
| 116 | Forestry |
| 126 | Fisheries |
| 206 | Metal mining |
| 216 | Coal mining |
| 226 | Crude petroleum and natural gas extraction |
| 236 | Nonmetallic mining and quarrying, except fuel |
| 239 | Mining not specified |
| 246 | Construction |
| 306 | Logging |
| 307 | Sawmills, planing mills, and millwork |
| 308 | Misc wood products |
| 309 | Furniture and fixtures |
| 316 | Glass and glass products |
| 317 | Cement, concrete, gypsum and plaster products |
| 318 | Structural clay products |
| 319 | Pottery and related products |
| 326 | Miscellaneous nonmetallic mineral and stone products |
| 336 | Blast furnaces, steel works, and rolling mills |
| 337 | Other primary iron and steel industries |
| 338 | Primary nonferrous industries |
| 346 | Fabricated steel products |
| 347 | Fabricated nonferrous metal products |
| 348 | Not specified metal industries |
| 356 | Agricultural machinery and tractors |
| 357 | Office and store machines and devices |
| 358 | Miscellaneous machinery |
| 367 | Electrical machinery, equipment, and supplies |
| 376 | Motor vehicles and motor vehicle equipment |
| 377 | Aircraft and parts |
| 378 | Ship and boat building and repairing |
| 379 | Railroad and miscellaneous transportation equipment |
| 386 | Professional equipment and supplies |
| 387 | Photographic equipment and supplies |
| 388 | Watches, clocks, and clockwork-operated devices |
| 399 | Miscellaneous manufacturing industries |
| 406 | Meat products |
| 407 | Dairy products |
| 408 | Canning and preserving fruits, vegetables, and seafoods |
| 409 | Grain-mill products |
| 416 | Bakery products |
| 417 | Confectionery and related products |
| 418 | Beverage industries |
| 419 | Miscellaneous food preparations and kindred products |
| 426 | Not specified food industries |
| 429 | Tobacco manufactures |
| 436 | Knitting mills |
| 437 | Dyeing and finishing textiles, except knit goods |
| 438 | Carpets, rugs, and other floor coverings |
| 439 | Yarn, thread, and fabric mills |
| 446 | Miscellaneous textile mill products |
| 448 | Apparel and accessories |
| 449 | Miscellaneous fabricated textile products |
| 456 | Pulp, paper, and paperboard mills |
| 457 | Paperboard containers and boxes |
| 458 | Miscellaneous paper and pulp products |
| 459 | Printing, publishing, and allied industries |
| 466 | Synthetic fibers |
| 467 | Drugs and medicines |
| 468 | Paints, varnishes, and related products |
| 469 | Miscellaneous chemicals and allied products |
| 476 | Petroleum refining |
| 477 | Miscellaneous petroleum and coal products |
| 478 | Rubber products |
| 487 | Leather: tanned, curried, and finished |
| 488 | Footwear, except rubber |
| 489 | Leather products, except footwear |
| 499 | Not specified manufacturing industries |
| 506 | Railroads and railway express service |
| 516 | Street railways and bus lines |
| 526 | Trucking service |
| 527 | Warehousing and storage |
| 536 | Taxicab service |
| 546 | Water transportation |
| 556 | Air transportation |
| 567 | Petroleum and gasoline pipe lines |
| 568 | Services incidental to transportation |
| 578 | Telephone |
| 579 | Telegraph |
| 586 | Electric light and power |
| 587 | Gas and steam supply systems |
| 588 | Electric-gas utilities |
| 596 | Water supply |
| 597 | Sanitary services |
| 598 | Other and not specified utilities |
| 606 | Motor vehicles and equipment |
| 607 | Drugs, chemicals, and allied products |
| 608 | Dry goods apparel |
| 609 | Food and related products |
| 616 | Electrical goods, hardware, and plumbing equipment |
| 617 | Machinery, equipment, and supplies |
| 618 | Petroleum products |
| 619 | Farm products--raw materials |
| 626 | Miscellaneous wholesale trade |
| 627 | Not specified wholesale trade |
| 636 | Food stores, except dairy products |
| 637 | Dairy products stores and milk retailing |
| 646 | General merchandise stores |
| 647 | Five and ten cent stores |
| 656 | Apparel and accessories stores, except shoe |
| 657 | Shoe stores |
| 658 | Furniture and house furnishing stores |
| 659 | Household appliance and radio stores |
| 667 | Motor vehicles and accessories retailing |
| 668 | Gasoline service stations |
| 669 | Drug stores |
| 679 | Eating and drinking places |
| 686 | Hardware and farm implement stores |
| 687 | Lumber and building material retailing |
| 688 | Liquor stores |
| 689 | Retail florists |
| 696 | Jewelry stores |
| 697 | Fuel and ice retailing |
| 698 | Miscellaneous retail stores |
| 699 | Not specified retail trade |
| 716 | Banking and credit agencies |
| 726 | Security and commodity brokerage and investment companies |
| 736 | Insurance |
| 746 | Real estate |
| 806 | Advertising |
| 807 | Accounting, auditing, and bookkeeping services |
| 808 | Miscellaneous business services |
| 816 | Auto repair services and garages |
| 817 | Miscellaneous repair services |
| 826 | Private households |
| 836 | Hotels and lodging places |
| 846 | Laundering, cleaning, and dyeing services |
| 847 | Dressmaking shops |
| 848 | Shoe repair shops |
| 849 | Miscellaneous personal services |
| 856 | Radio broadcasting and television |
| 857 | Theaters and motion pictures |
| 858 | Bowling alleys, and billiard and pool parlors |
| 859 | Miscellaneous entertainment and recreation services |
| 868 | Medical and other health services, except hospitals |
| 869 | Hospitals |
| 879 | Legal services |
| 888 | Educational services |
| 896 | Welfare and religious services |
| 897 | Nonprofit membership organizations |
| 898 | Engineering and architectural services |
| 899 | Miscellaneous professional and related services |
| 906 | Postal service |
| 916 | Federal public administration |
| 926 | State public administration |
| 936 | Local public administration |
| 997 | Nonclassifiable |
| 998 | Industry not reported |

### OCC90LY : Occupation last year, 1990 basis
| Code | Label |
| :--- | :--- |
| 003 | Legislators |
| 004 | Chief executives and public administrators |
| 007 | Financial managers |
| 008 | Human resources and labor relations managers |
| 013 | Managers and specialists in marketing, advertising, and public relations |
| 014 | Managers in education and related fields |
| 015 | Managers of medicine and health occupations |
| 016 | Postmasters and mail superintendents |
| 017 | Managers of food-serving and lodging establishments |
| 018 | Managers of properties and real estate |
| 019 | Funeral directors |
| 021 | Managers of service organizations, n.e.c. |
| 022 | Managers and administrators, n.e.c. |
| 023 | Accountants and auditors |
| 024 | Insurance underwriters |
| 025 | Other financial specialists |
| 026 | Management analysts |
| 027 | Personnel, HR, training, and labor relations specialists |
| 028 | Purchasing agents and buyers, of farm products |
| 029 | Buyers, wholesale and retail trade |
| 033 | Purchasing managers, agents and buyers, n.e.c. |
| 034 | Business and promotion agents |
| 035 | Construction inspectors |
| 036 | Inspectors and compliance officers, outside construction |
| 037 | Management support occupations |
| 043 | Architects |
| 044 | Aerospace engineer |
| 045 | Metallurgical and materials engineers, variously phrased |
| 047 | Petroleum, mining, and geological engineers |
| 048 | Chemical engineers |
| 053 | Civil engineers |
| 055 | Electrical engineer |
| 056 | Industrial engineers |
| 057 | Mechanical engineers |
| 059 | Not-elsewhere-classified engineers |
| 064 | Computer systems analysts and computer scientists |
| 065 | Operations and systems researchers and analysts |
| 066 | Actuaries |
| 067 | Statisticians |
| 068 | Mathematicians and mathematical scientists |
| 069 | Physicists and astronomers |
| 073 | Chemists |
| 074 | Atmospheric and space scientists |
| 075 | Geologists |
| 076 | Physical scientists, n.e.c. |
| 077 | Agricultural and food scientists |
| 078 | Biological scientists |
| 079 | Foresters and conservation scientists |
| 083 | Medical scientists |
| 084 | Physicians |
| 085 | Dentists |
| 086 | Veterinarians |
| 087 | Optometrists |
| 088 | Podiatrists |
| 089 | Other health and therapy |
| 095 | Registered nurses |
| 096 | Pharmacists |
| 097 | Dietitians and nutritionists |
| 098 | Respiratory therapists |
| 099 | Occupational therapists |
| 103 | Physical therapists |
| 104 | Speech therapists |
| 105 | Therapists, n.e.c. |
| 106 | Physicians' assistants |
| 113 | Earth, environmental, and marine science instructors |
| 114 | Biological science instructors |
| 115 | Chemistry instructors |
| 116 | Physics instructors |
| 118 | Psychology instructors |
| 119 | Economics instructors |
| 123 | History instructors |
| 125 | Sociology instructors |
| 127 | Engineering instructors |
| 128 | Math instructors |
| 139 | Education instructors |
| 145 | Law instructors |
| 147 | Theology instructors |
| 149 | Home economics instructors |
| 150 | Humanities profs/instructors, college, nec |
| 154 | Subject instructors (HS/college) |
| 155 | Kindergarten and earlier school teachers |
| 156 | Primary school teachers |
| 157 | Secondary school teachers |
| 158 | Special education teachers |
| 159 | Teachers , n.e.c. |
| 163 | Vocational and educational counselors |
| 164 | Librarians |
| 165 | Archivists and curators |
| 166 | Economists, market researchers, and survey researchers |
| 167 | Psychologists |
| 168 | Sociologists |
| 169 | Social scientists, n.e.c. |
| 173 | Urban and regional planners |
| 174 | Social workers |
| 175 | Recreation workers |
| 176 | Clergy and religious workers |
| 178 | Lawyers |
| 179 | Judges |
| 183 | Writers and authors |
| 184 | Technical writers |
| 185 | Designers |
| 186 | Musician or composer |
| 187 | Actors, directors, producers |
| 188 | Art makers: painters, sculptors, craft-artists, and print-makers |
| 189 | Photographers |
| 193 | Dancers |
| 194 | Art/entertainment performers and related |
| 195 | Editors and reporters |
| 198 | Announcers |
| 199 | Athletes, sports instructors, and officials |
| 200 | Professionals, n.e.c. |
| 203 | Clinical laboratory technologies and technicians |
| 204 | Dental hygenists |
| 205 | Health record tech specialists |
| 206 | Radiologic tech specialists |
| 207 | Licensed practical nurses |
| 208 | Health technologists and technicians, n.e.c. |
| 213 | Electrical and electronic (engineering) technicians |
| 214 | Engineering technicians, n.e.c. |
| 215 | Mechanical engineering technicians |
| 217 | Drafters |
| 218 | Surveyors, cartographers, mapping scientists and technicians |
| 223 | Biological technicians |
| 224 | Chemical technicians |
| 225 | Other science technicians |
| 226 | Airplane pilots and navigators |
| 227 | Air traffic controllers |
| 228 | Broadcast equipment operators |
| 229 | Computer software developers |
| 233 | Programmers of numerically controlled machine tools |
| 234 | Legal assistants, paralegals, legal support, etc |
| 235 | Technicians, n.e.c. |
| 243 | Supervisors and proprietors of sales jobs |
| 253 | Insurance sales occupations |
| 254 | Real estate sales occupations |
| 255 | Financial services sales occupations |
| 256 | Advertising and related sales jobs |
| 258 | Sales engineers |
| 274 | Salespersons, n.e.c. |
| 275 | Retail sales clerks |
| 276 | Cashiers |
| 277 | Door-to-door sales, street sales, and news vendors |
| 283 | Sales demonstrators / promoters / models |
| 290 | Sales workers--allocated (1990 internal census) |
| 303 | Office supervisors |
| 308 | Computer and peripheral equipment operators |
| 313 | Secretaries |
| 314 | Stenographers |
| 315 | Typists |
| 316 | Interviewers, enumerators, and surveyors |
| 317 | Hotel clerks |
| 318 | Transportation ticket and reservation agents |
| 319 | Receptionists |
| 323 | Information clerks, nec |
| 326 | Correspondence and order clerks |
| 328 | Human resources clerks, except payroll and timekeeping |
| 329 | Library assistants |
| 335 | File clerks |
| 336 | Records clerks |
| 337 | Bookkeepers and accounting and auditing clerks |
| 338 | Payroll and timekeeping clerks |
| 343 | Cost and rate clerks (financial records processing) |
| 344 | Billing clerks and related financial records processing |
| 345 | Duplication machine operators / office machine operators |
| 346 | Mail and paper handlers |
| 347 | Office machine operators, n.e.c. |
| 348 | Telephone operators |
| 349 | Other telecom operators |
| 354 | Postal clerks, excluding mail carriers |
| 355 | Mail carriers for postal service |
| 356 | Mail clerks, outside of post office |
| 357 | Messengers |
| 359 | Dispatchers |
| 361 | Inspectors, n.e.c. |
| 364 | Shipping and receiving clerks |
| 365 | Stock and inventory clerks |
| 366 | Meter readers |
| 368 | Weighers, measurers, and checkers |
| 373 | Material recording, scheduling, production, planning, and expediting clerks |
| 375 | Insurance adjusters, examiners, and investigators |
| 376 | Customer service reps, investigators and adjusters, except insurance |
| 377 | Eligibility clerks for government programs; social welfare |
| 378 | Bill and account collectors |
| 379 | General office clerks |
| 383 | Bank tellers |
| 384 | Proofreaders |
| 385 | Data entry keyers |
| 386 | Statistical clerks |
| 387 | Teacher's aides |
| 389 | Administrative support jobs, n.e.c. |
| 390 | Professional, technical, and kindred workers--allocated (1990 internal census) |
| 391 | Clerical and kindred workers--allocated (1990 internal census) |
| 405 | Housekeepers, maids, butlers, stewards, and lodging quarters cleaners |
| 407 | Private household cleaners and servants |
| 408 | Private household workers--allocated (1990 internal census) |
| 415 | Supervisors of guards |
| 417 | Fire fighting, prevention, and inspection |
| 418 | Police, detectives, and private investigators |
| 423 | Other law enforcement: sheriffs, bailiffs, correctional institution officers |
| 425 | Crossing guards and bridge tenders |
| 426 | Guards, watchmen, doorkeepers |
| 427 | Protective services, n.e.c. |
| 434 | Bartenders |
| 435 | Waiter/waitress |
| 436 | Cooks, variously defined |
| 438 | Food counter and fountain workers |
| 439 | Kitchen workers |
| 443 | Waiter's assistant |
| 444 | Misc food prep workers |
| 445 | Dental assistants |
| 446 | Health aides, except nursing |
| 447 | Nursing aides, orderlies, and attendants |
| 448 | Supervisors of cleaning and building service |
| 453 | Janitors |
| 454 | Elevator operators |
| 455 | Pest control occupations |
| 456 | Supervisors of personal service jobs, n.e.c. |
| 457 | Barbers |
| 458 | Hairdressers and cosmetologists |
| 459 | Recreation facility attendants |
| 461 | Guides |
| 462 | Ushers |
| 463 | Public transportation attendants and inspectors |
| 464 | Baggage porters |
| 465 | Welfare service aides |
| 468 | Child care workers |
| 469 | Personal service occupations, nec |
| 473 | Farmers (owners and tenants) |
| 474 | Horticultural specialty farmers |
| 475 | Farm managers, except for horticultural farms |
| 476 | Managers of horticultural specialty farms |
| 479 | Farm workers |
| 480 | Farm laborers and farm foreman--allocated (1990 internal census) |
| 483 | Marine life cultivation workers |
| 484 | Nursery farming workers |
| 485 | Supervisors of agricultural occupations |
| 486 | Gardeners and groundskeepers |
| 487 | Animal caretakers except on farms |
| 488 | Graders and sorters of agricultural products |
| 489 | Inspectors of agricultural products |
| 496 | Timber, logging, and forestry workers |
| 498 | Fishers, hunters, and kindred |
| 503 | Supervisors of mechanics and repairers |
| 505 | Automobile mechanics |
| 507 | Bus, truck, and stationary engine mechanics |
| 508 | Aircraft mechanics |
| 509 | Small engine repairers |
| 514 | Auto body repairers |
| 516 | Heavy equipment and farm equipment mechanics |
| 518 | Industrial machinery repairers |
| 519 | Machinery maintenance occupations |
| 523 | Repairers of industrial electrical equipment |
| 525 | Repairers of data processing equipment |
| 526 | Repairers of household appliances and power tools |
| 527 | Telecom and line installers and repairers |
| 533 | Repairers of electrical equipment, n.e.c. |
| 534 | Heating, air conditioning, and refigeration mechanics |
| 535 | Precision makers, repairers, and smiths |
| 536 | Locksmiths and safe repairers |
| 538 | Office machine repairers and mechanics |
| 539 | Repairers of mechanical controls and valves |
| 543 | Elevator installers and repairers |
| 544 | Millwrights |
| 549 | Mechanics and repairers, n.e.c. |
| 558 | Supervisors of construction work |
| 563 | Masons, tilers, and carpet installers |
| 567 | Carpenters |
| 573 | Drywall installers |
| 575 | Electricians |
| 577 | Electric power installers and repairers |
| 579 | Painters, construction and maintenance |
| 583 | Paperhangers |
| 584 | Plasterers |
| 585 | Plumbers, pipe fitters, and steamfitters |
| 588 | Concrete and cement workers |
| 589 | Glaziers |
| 593 | Insulation workers |
| 594 | Paving, surfacing, and tamping equipment operators |
| 595 | Roofers and slaters |
| 596 | Sheet metal duct installers |
| 597 | Structural metal workers |
| 598 | Drillers of earth |
| 599 | Construction trades, n.e.c. |
| 614 | Drillers of oil wells |
| 615 | Explosives workers |
| 616 | Miners |
| 617 | Other mining occupations |
| 628 | Production supervisors or foremen |
| 634 | Tool and die makers and die setters |
| 637 | Machinists |
| 643 | Boilermakers |
| 644 | Precision grinders and filers |
| 645 | Patternmakers and model makers |
| 646 | Lay-out workers |
| 649 | Engravers |
| 653 | Tinsmiths, coppersmiths, and sheet metal workers |
| 657 | Cabinetmakers and bench carpenters |
| 658 | Furniture and wood finishers |
| 659 | Other precision woodworkers |
| 666 | Dressmakers and seamstresses |
| 667 | Tailors |
| 668 | Upholsterers |
| 669 | Shoe repairers |
| 674 | Other precision apparel and fabric workers |
| 675 | Hand molders and shapers, except jewelers |
| 677 | Optical goods workers |
| 678 | Dental laboratory and medical appliance technicians |
| 679 | Bookbinders |
| 684 | Other precision and craft workers |
| 686 | Butchers and meat cutters |
| 687 | Bakers |
| 688 | Batch food makers |
| 693 | Adjusters and calibrators |
| 694 | Water and sewage treatment plant operators |
| 695 | Power plant operators |
| 696 | Plant and system operators, stationary engineers |
| 699 | Other plant and system operators |
| 703 | Lathe, milling, and turning machine operatives |
| 706 | Punching and stamping press operatives |
| 707 | Rollers, roll hands, and finishers of metal |
| 708 | Drilling and boring machine operators |
| 709 | Grinding, abrading, buffing, and polishing workers |
| 713 | Forge and hammer operators |
| 717 | Fabricating machine operators, n.e.c. |
| 719 | Molders, and casting machine operators |
| 723 | Metal platers |
| 724 | Heat treating equipment operators |
| 726 | Wood lathe, routing, and planing machine operators |
| 727 | Sawing machine operators and sawyers |
| 728 | Shaping and joining machine operator (woodworking) |
| 729 | Nail and tacking machine operators  (woodworking) |
| 733 | Other woodworking machine operators |
| 734 | Printing machine operators, n.e.c. |
| 735 | Photoengravers and lithographers |
| 736 | Typesetters and compositors |
| 738 | Winding and twisting textile/apparel operatives |
| 739 | Knitters, loopers, and toppers textile operatives |
| 743 | Textile cutting machine operators |
| 744 | Textile sewing machine operators |
| 745 | Shoemaking machine operators |
| 747 | Pressing machine operators (clothing) |
| 748 | Laundry workers |
| 749 | Misc textile machine operators |
| 753 | Cementing and gluing maching operators |
| 754 | Packers, fillers, and wrappers |
| 755 | Extruding and forming machine operators |
| 756 | Mixing and blending machine operatives |
| 757 | Separating, filtering, and clarifying machine operators |
| 759 | Painting machine operators |
| 763 | Roasting and baking machine operators (food) |
| 764 | Washing, cleaning, and pickling machine operators |
| 765 | Paper folding machine operators |
| 766 | Furnace, kiln, and oven operators, apart from food |
| 768 | Crushing and grinding machine operators |
| 769 | Slicing and cutting machine operators |
| 773 | Motion picture projectionists |
| 774 | Photographic process workers |
| 779 | Machine operators, n.e.c. |
| 783 | Welders and metal cutters |
| 784 | Solderers |
| 785 | Assemblers of electrical equipment |
| 789 | Hand painting, coating, and decorating occupations |
| 796 | Production checkers and inspectors |
| 799 | Graders and sorters in manufacturing |
| 803 | Supervisors of motor vehicle transportation |
| 804 | Truck, delivery, and tractor drivers |
| 808 | Bus drivers |
| 809 | Taxi cab drivers and chauffeurs |
| 813 | Parking lot attendants |
| 815 | Transport equipment operatives--allocated (1990 internal census) |
| 823 | Railroad conductors and yardmasters |
| 824 | Locomotive operators (engineers and firemen) |
| 825 | Railroad brake, coupler, and switch operators |
| 829 | Ship crews and marine engineers |
| 834 | Water transport infrastructure tenders and crossing guards |
| 844 | Operating engineers of construction equipment |
| 848 | Crane, derrick, winch, and hoist operators |
| 853 | Excavating and loading machine operators |
| 859 | Misc material moving occupations |
| 865 | Helpers, constructions |
| 866 | Helpers, surveyors |
| 869 | Construction laborers |
| 874 | Production helpers |
| 875 | Garbage and recyclable material collectors |
| 876 | Materials movers: stevedores and longshore workers |
| 877 | Stock handlers |
| 878 | Machine feeders and offbearers |
| 883 | Freight, stock, and materials handlers |
| 885 | Garage and service station related occupations |
| 887 | Vehicle washers and equipment cleaners |
| 888 | Packers and packagers by hand |
| 889 | Laborers outside construction |
| 890 | Laborers, except farm--allocated (1990 internal census) |
| 905 | Military |
| 991 | Unemployed |
| 999 | NIU |

### IND90LY : Industry last year, 1990 basis
| Code | Label |
| :--- | :--- |
| 000 | NIU |
| 010 | Agricultural production, crops |
| 011 | Agricultural production, livestock |
| 012 | Veterinary services |
| 020 | Landscape and horticultural services |
| 030 | Agricultural services, n.e.c. |
| 031 | Forestry |
| 032 | Fishing, hunting, and trapping |
| 040 | Metal mining |
| 041 | Coal mining |
| 042 | Oil and gas extraction |
| 050 | Nonmetallic mining and quarrying, except fuels |
| 060 | All construction |
| 100 | Meat products |
| 101 | Dairy products |
| 102 | Canned, frozen, and preserved fruits and vegetables |
| 110 | Grain mill products |
| 111 | Bakery products |
| 112 | Sugar and confectionery products |
| 120 | Beverage industries |
| 121 | Misc. food preparations and kindred products |
| 122 | Food industries, n.s. |
| 130 | Tobacco manufactures |
| 132 | Knitting mills |
| 140 | Dyeing and finishing textiles, except wool and knit goods |
| 141 | Carpets and rugs |
| 142 | Yarn, thread, and fabric mills |
| 150 | Miscellaneous textile mill products |
| 151 | Apparel and accessories, except knit |
| 152 | Miscellaneous fabricated textile products |
| 160 | Pulp, paper, and paperboard mills |
| 161 | Miscellaneous paper and pulp products |
| 162 | Paperboard containers and boxes |
| 171 | Newspaper publishing and printing |
| 172 | Printing, publishing, and allied industries, except newspapers |
| 180 | Plastics, synthetics, and resins |
| 181 | Drugs |
| 182 | Soaps and cosmetics |
| 190 | Paints, varnishes, and related products |
| 191 | Agricultural chemicals |
| 192 | Industrial and miscellaneous chemicals |
| 200 | Petroleum refining |
| 201 | Miscellaneous petroleum and coal products |
| 210 | Tires and inner tubes |
| 211 | Other rubber products, and plastics footwear and belting |
| 212 | Miscellaneous plastics products |
| 220 | Leather tanning and finishing |
| 221 | Footwear, except rubber and plastic |
| 222 | Leather products, except footwear |
| 229 | Manufacturing, non-durable - allocated |
| 230 | Logging |
| 231 | Sawmills, planing mills, and millwork |
| 232 | Wood buildings and mobile homes |
| 241 | Miscellaneous wood products |
| 242 | Furniture and fixtures |
| 250 | Glass and glass products |
| 251 | Cement, concrete, gypsum, and plaster products |
| 252 | Structural clay products |
| 261 | Pottery and related products |
| 262 | Misc. nonmetallic mineral and stone products |
| 270 | Blast furnaces, steelworks, rolling and finishing mills |
| 271 | Iron and steel foundries |
| 272 | Primary aluminum industries |
| 280 | Other primary metal industries |
| 281 | Cutlery, handtools, and general hardware |
| 282 | Fabricated structural metal products |
| 290 | Screw machine products |
| 291 | Metal forgings and stampings |
| 292 | Ordnance |
| 300 | Miscellaneous fabricated metal products |
| 301 | Metal industries, n.s. |
| 310 | Engines and turbines |
| 311 | Farm machinery and equipment |
| 312 | Construction and material handling machines |
| 320 | Metalworking machinery |
| 321 | Office and accounting machines |
| 322 | Computers and related equipment |
| 331 | Machinery, except electrical, n.e.c. |
| 332 | Machinery, n.s. |
| 340 | Household appliances |
| 341 | Radio, TV, and communication equipment |
| 342 | Electrical machinery, equipment, and supplies, n.e.c. |
| 350 | Electrical machinery, equipment, and supplies, n.s. |
| 351 | Motor vehicles and motor vehicle equipment |
| 352 | Aircraft and parts |
| 360 | Ship and boat building and repairing |
| 361 | Railroad locomotives and equipment |
| 362 | Guided missiles, space vehicles, and parts |
| 370 | Cycles and miscellaneous transportation equipment |
| 371 | Scientific and controlling instruments |
| 372 | Medical, dental, and optical instruments and supplies |
| 380 | Photographic equipment and supplies |
| 381 | Watches, clocks, and clockwork operated devices |
| 390 | Toys, amusement, and sporting goods |
| 391 | Miscellaneous manufacturing industries |
| 392 | Manufacturing industries, n.s. |
| 400 | Railroads |
| 401 | Bus service and urban transit |
| 402 | Taxicab service |
| 410 | Trucking service |
| 411 | Warehousing and storage |
| 412 | U.S. Postal Service |
| 420 | Water transportation |
| 421 | Air transportation |
| 422 | Pipe lines, except natural gas |
| 432 | Services incidental to transportation |
| 440 | Radio and television broadcasting and cable |
| 441 | Wired communications |
| 442 | Telegraph and miscellaneous communications services |
| 450 | Electric light and power |
| 451 | Gas and steam supply systems |
| 452 | Electric and gas, and other combinations |
| 470 | Water supply and irrigation |
| 471 | Sanitary services |
| 472 | Utilities, n.s. |
| 500 | Motor vehicles and equipment |
| 501 | Furniture and home furnishings |
| 502 | Lumber and construction materials |
| 510 | Professional and commercial equipment and supplies |
| 511 | Metals and minerals, except petroleum |
| 512 | Electrical goods |
| 521 | Hardware, plumbing and heating supplies |
| 530 | Machinery, equipment, and supplies |
| 531 | Scrap and waste materials |
| 532 | Miscellaneous wholesale, durable goods |
| 540 | Paper and paper products |
| 541 | Drugs, chemicals, and allied products |
| 542 | Apparel, fabrics, and notions |
| 550 | Groceries and related products |
| 551 | Farm-product raw materials |
| 552 | Petroleum products |
| 560 | Alcoholic beverages |
| 561 | Farm supplies |
| 562 | Miscellaneous wholesale, nondurable goods |
| 571 | Wholesale trade, n.s. |
| 580 | Lumber and building material retailing |
| 581 | Hardware stores |
| 582 | Retail nurseries and garden stores |
| 590 | Mobile home dealers |
| 591 | Department stores |
| 592 | Variety stores |
| 600 | Miscellaneous general merchandise stores |
| 601 | Grocery stores |
| 602 | Dairy products stores |
| 610 | Retail bakeries |
| 611 | Food stores, n.e.c. |
| 612 | Motor vehicle dealers |
| 620 | Auto and home supply stores |
| 621 | Gasoline service stations |
| 622 | Miscellaneous vehicle dealers |
| 623 | Apparel and accessory stores, except shoe |
| 630 | Shoe stores |
| 631 | Furniture and home furnishings stores |
| 632 | Household appliance stores |
| 633 | Radio, TV, and computer stores |
| 640 | Music stores |
| 641 | Eating and drinking places |
| 642 | Drug stores |
| 650 | Liquor stores |
| 651 | Sporting goods, bicycles, and hobby stores |
| 652 | Book and stationery stores |
| 660 | Jewelry stores |
| 661 | Gift, novelty, and souvenir shops |
| 662 | Sewing, needlework, and piece goods stores |
| 663 | Catalog and mail order houses |
| 670 | Vending machine operators |
| 671 | Direct selling establishments |
| 672 | Fuel dealers |
| 681 | Retail florists |
| 682 | Miscellaneous retail stores |
| 691 | Retail trade, n.s. |
| 700 | Banking |
| 701 | Savings institutions, including credit unions |
| 702 | Credit agencies, n.e.c. |
| 710 | Security, commodity brokerage, and investment companies |
| 711 | Insurance |
| 712 | Real estate, including real estate-insurance offices |
| 721 | Advertising |
| 722 | Services to dwellings and other buildings |
| 731 | Personnel supply services |
| 732 | Computer and data processing services |
| 740 | Detective and protective services |
| 741 | Business services, n.e.c. |
| 742 | Automotive rental and leasing, without drivers |
| 750 | Automobile parking and carwashes |
| 751 | Automotive repair and related services |
| 752 | Electrical repair shops |
| 760 | Miscellaneous repair services |
| 761 | Private households |
| 762 | Hotels and motels |
| 770 | Lodging places, except hotels and motels |
| 771 | Laundry, cleaning, and garment services |
| 772 | Beauty shops |
| 780 | Barber shops |
| 781 | Funeral service and crematories |
| 782 | Shoe repair shops |
| 790 | Dressmaking shops |
| 791 | Miscellaneous personal services |
| 800 | Theaters and motion pictures |
| 801 | Video tape rental |
| 802 | Bowling centers |
| 810 | Miscellaneous entertainment and recreation services |
| 812 | Offices and clinics of physicians |
| 820 | Offices and clinics of dentists |
| 821 | Offices and clinics of chiropractors |
| 822 | Offices and clinics of optometrists |
| 830 | Offices and clinics of health practitioners, n.e.c. |
| 831 | Hospitals |
| 832 | Nursing and personal care facilities |
| 840 | Health services, n.e.c. |
| 841 | Legal services |
| 842 | Elementary and secondary schools |
| 850 | Colleges and universities |
| 851 | Vocational schools |
| 852 | Libraries |
| 860 | Educational services, n.e.c. |
| 861 | Job training and vocational rehabilitation services |
| 862 | Child day care services |
| 863 | Family child care homes |
| 870 | Residential care facilities, without nursing |
| 871 | Social services, n.e.c. |
| 872 | Museums, art galleries, and zoos |
| 873 | Labor unions |
| 880 | Religious organizations |
| 881 | Membership organizations, n.e.c. |
| 882 | Engineering, architectural, and surveying services |
| 890 | Accounting, auditing, and bookkeeping services |
| 891 | Research, development, and testing services |
| 892 | Management and public relations services |
| 893 | Miscellaneous professional and related services |
| 900 | Executive and legislative offices |
| 901 | General government, n.e.c. |
| 910 | Justice, public order, and safety |
| 921 | Public finance, taxation, and monetary policy |
| 922 | Administration of human resources programs |
| 930 | Administration of environmental quality and housing programs |
| 931 | Administration of economic programs |
| 932 | National security and international affairs |
| 940 | Army |
| 941 | Air Force |
| 942 | Navy |
| 950 | Marines |
| 951 | Coast Guard |
| 952 | Armed Forces, branch not specified |
| 960 | Military Reserves or National Guard |
| 998 | Unknown |

### OCC10LY : Occupation last year, 2010 basis
| Code | Label |
| :--- | :--- |
| 0010 | Chief executives and legislators |
| 0020 | General and Operations Managers |
| 0040 | Advertising and Promotions Managers |
| 0050 | Marketing and Sales Managers |
| 0060 | Public Relations and Fundraising Managers |
| 0100 | Administrative Services Managers |
| 0110 | Computer and Information Systems Managers |
| 0120 | Financial Managers |
| 0135 | Compensation and benefits managers |
| 0136 | Human Resources Managers |
| 0137 | Training and development managers |
| 0140 | Industrial Production Managers |
| 0150 | Purchasing Managers |
| 0160 | Transportation, Storage, and Distribution Managers |
| 0205 | Farmers, Ranchers, and Other Agricultural Managers |
| 0220 | Construction Managers |
| 0230 | Education Administrators |
| 0300 | Architectural and Engineering Managers |
| 0310 | Food Service Managers |
| 0330 | Gaming Managers |
| 0340 | Lodging Managers |
| 0350 | Medical and Health Services Managers |
| 0360 | Natural Sciences Managers |
| 0410 | Property, Real Estate, and Community Association Managers |
| 0420 | Social and Community Service Managers |
| 0425 | Emergency management directors |
| 0430 | Miscellaneous managers, including funeral service managers and postmasters and mail superintendents |
| 0500 | Agents and Business Managers of Artists, Performers, and Athletes |
| 0510 | Buyers and Purchasing Agents, Farm Products |
| 0520 | Wholesale and Retail Buyers, Except Farm Products |
| 0530 | Purchasing Agents, Except Wholesale, Retail, and Farm Products |
| 0540 | Claims Adjusters, Appraisers, Examiners, and Investigators |
| 0565 | Compliance Officers |
| 0600 | Cost Estimators |
| 0630 | Human Resources Workers |
| 0640 | Compensation, benefits, and job analysis specialists |
| 0650 | Training and development specialists |
| 0700 | Logisticians |
| 0710 | Management Analysts |
| 0725 | Meeting, Convention, and Event Planners |
| 0726 | Fundraisers |
| 0735 | Market Research Analysts and Marketing Specialists |
| 0740 | Business Operations Specialists, All Other |
| 0800 | Accountants and Auditors |
| 0810 | Appraisers and Assessors of Real Estate |
| 0820 | Budget Analysts |
| 0830 | Credit Analysts |
| 0840 | Financial Analysts |
| 0850 | Personal Financial Advisors |
| 0860 | Insurance Underwriters |
| 0900 | Financial Examiners |
| 0910 | Credit Counselors and Loan Officers |
| 0930 | Tax Examiners and Collectors, and Revenue Agents |
| 0940 | Tax Preparers |
| 0950 | Financial Specialists, All Other |
| 1005 | Computer and information research scientists |
| 1006 | Computer Systems Analysts |
| 1007 | Information security analysts |
| 1010 | Computer Programmers |
| 1020 | Software Developers, Applications and Systems Software |
| 1030 | Web Developers |
| 1050 | Computer Support Specialists |
| 1060 | Database Administrators |
| 1105 | Network and Computer Systems Administrators |
| 1106 | Computer network architects |
| 1107 | Computer occupations, all other |
| 1200 | Actuaries |
| 1220 | Operations Research Analysts |
| 1240 | Miscellaneous mathematical science occupations, including mathematicians and statisticians |
| 1300 | Architects, Except Naval |
| 1310 | Surveyors, Cartographers, and Photogrammetrists |
| 1320 | Aerospace Engineers |
| 1340 | Biomedical and agricultural engineers |
| 1350 | Chemical Engineers |
| 1360 | Civil Engineers |
| 1400 | Computer Hardware Engineers |
| 1410 | Electrical and Electronics Engineers |
| 1420 | Environmental Engineers |
| 1430 | Industrial Engineers, including Health and Safety |
| 1440 | Marine Engineers and Naval Architects |
| 1450 | Materials Engineers |
| 1460 | Mechanical Engineers |
| 1520 | Petroleum, mining and geological engineers, including mining safety engineers |
| 1530 | Miscellaneous engineers, including nuclear engineers |
| 1540 | Drafters |
| 1550 | Engineering Technicians, Except Drafters |
| 1560 | Surveying and Mapping Technicians |
| 1600 | Agricultural and Food Scientists |
| 1610 | Biological Scientists |
| 1640 | Conservation Scientists and Foresters |
| 1650 | Medical scientists, and life scientists, all other |
| 1700 | Astronomers and Physicists |
| 1710 | Atmospheric and Space Scientists |
| 1720 | Chemists and Materials Scientists |
| 1740 | Environmental Scientists and Geoscientists |
| 1760 | Physical Scientists, All Other |
| 1800 | Economists |
| 1820 | Psychologists |
| 1840 | Urban and Regional Planners |
| 1860 | Miscellaneous social scientists, including survey researchers and sociologists |
| 1900 | Agricultural and Food Science Technicians |
| 1910 | Biological Technicians |
| 1920 | Chemical Technicians |
| 1930 | Geological and petroleum technicians, and nuclear technicians |
| 1965 | Miscellaneous life, physical, and social science technicians, including social science research assistants |
| 2000 | Counselors |
| 2010 | Social Workers |
| 2015 | Probation officers and correctional treatment specialists |
| 2016 | Social and human service assistants |
| 2025 | Miscellaneous community and social service specialists, including health educators and community health workers |
| 2040 | Clergy |
| 2050 | Directors, Religious Activities and Education |
| 2060 | Religious Workers, All Other |
| 2100 | Lawyers, and judges, magistrates, and other judicial workers |
| 2105 | Judicial law clerks |
| 2145 | Paralegals and Legal Assistants |
| 2160 | Miscellaneous Legal Support Workers |
| 2200 | Postsecondary Teachers |
| 2300 | Preschool and Kindergarten Teachers |
| 2310 | Elementary and Middle School Teachers |
| 2320 | Secondary School Teachers |
| 2330 | Special Education Teachers |
| 2340 | Other Teachers and Instructors |
| 2400 | Archivists, Curators, and Museum Technicians |
| 2430 | Librarians |
| 2440 | Library Technicians |
| 2540 | Teacher Assistants |
| 2550 | Other Education, Training, and Library Workers |
| 2600 | Artists and Related Workers |
| 2630 | Designers |
| 2700 | Actors |
| 2710 | Producers and Directors |
| 2720 | Athletes, Coaches, Umpires, and Related Workers |
| 2740 | Dancers and Choreographers |
| 2750 | Musicians, Singers, and Related Workers |
| 2760 | Entertainers and Performers, Sports and Related Workers, All Other |
| 2800 | Announcers |
| 2810 | News Analysts, Reporters and Correspondents |
| 2825 | Public Relations Specialists |
| 2830 | Editors |
| 2840 | Technical Writers |
| 2850 | Writers and Authors |
| 2860 | Miscellaneous Media and Communication Workers |
| 2900 | Broadcast and sound engineering technicians and radio operators, and media and communication equipment workers, all other |
| 2910 | Photographers |
| 2920 | Television, Video, and Motion Picture Camera Operators and Editors |
| 3000 | Chiropractors |
| 3010 | Dentists |
| 3030 | Dietitians and Nutritionists |
| 3040 | Optometrists |
| 3050 | Pharmacists |
| 3060 | Physicians and Surgeons |
| 3110 | Physician Assistants |
| 3120 | Podiatrists |
| 3140 | Audiologists |
| 3150 | Occupational Therapists |
| 3160 | Physical Therapists |
| 3200 | Radiation Therapists |
| 3210 | Recreational Therapists |
| 3220 | Respiratory Therapists |
| 3230 | Speech-Language Pathologists |
| 3245 | Other therapists, including exercise physiologists |
| 3250 | Veterinarians |
| 3255 | Registered Nurses |
| 3256 | Nurse anesthetists |
| 3258 | Nurse practitioners and nurse midwives |
| 3260 | Health Diagnosing and Treating Practitioners, All Other |
| 3300 | Clinical Laboratory Technologists and Technicians |
| 3310 | Dental Hygienists |
| 3320 | Diagnostic Related Technologists and Technicians |
| 3400 | Emergency Medical Technicians and Paramedics |
| 3420 | Health Practitioner Support Technologists and  Technicians |
| 3500 | Licensed Practical and Licensed Vocational Nurses |
| 3510 | Medical Records and Health Information Technicians |
| 3520 | Opticians, Dispensing |
| 3535 | Miscellaneous Health Technologists and Technicians |
| 3540 | Other Healthcare Practitioners and Technical Occupations |
| 3600 | Nursing, Psychiatric, and Home Health Aides |
| 3610 | Occupational Therapy Assistants and Aides |
| 3620 | Physical Therapist Assistants and Aides |
| 3630 | Massage Therapists |
| 3640 | Dental Assistants |
| 3645 | Medical Assistants |
| 3646 | Medical transcriptionists |
| 3647 | Pharmacy aides |
| 3648 | Veterinary assistants and laboratory animal caretakers |
| 3649 | Phlebotomists |
| 3655 | Healthcare support workers, all other, including medical equipment preparers |
| 3700 | First-Line Supervisors of Correctional Officers |
| 3710 | First-Line Supervisors of Police and Detectives |
| 3720 | First-Line Supervisors of Fire Fighting and Prevention Workers |
| 3730 | First-Line Supervisors of Protective Service Workers, All Other |
| 3740 | Firefighters |
| 3750 | Fire Inspectors |
| 3800 | Bailiffs, Correctional Officers, and Jailers |
| 3820 | Detectives and Criminal Investigators |
| 3840 | Miscellaneous law enforcement workers |
| 3850 | Police officers |
| 3900 | Animal Control Workers |
| 3910 | Private Detectives and Investigators |
| 3930 | Security Guards and Gaming Surveillance Officers |
| 3940 | Crossing Guards |
| 3945 | Transportation security screeners |
| 3955 | Lifeguards and Other Recreational, and All Other Protective Service Workers |
| 4000 | Chefs and Head Cooks |
| 4010 | First-Line Supervisors of Food Preparation and Serving Workers |
| 4020 | Cooks |
| 4030 | Food Preparation Workers |
| 4040 | Bartenders |
| 4050 | Combined Food Preparation and Serving Workers, Including Fast Food |
| 4060 | Counter Attendants, Cafeteria, Food Concession, and Coffee Shop |
| 4110 | Waiters and Waitresses |
| 4120 | Food Servers, Nonrestaurant |
| 4130 | Miscellaneous food preparation and serving related workers, including dining room and cafeteria attendants and bartender helpers |
| 4140 | Dishwashers |
| 4150 | Hosts and Hostesses, Restaurant, Lounge, and Coffee Shop |
| 4200 | First-Line Supervisors of Housekeeping and Janitorial Workers |
| 4210 | First-Line Supervisors of Landscaping, Lawn Service, and Groundskeeping Workers |
| 4220 | Janitors and Building Cleaners |
| 4230 | Maids and housekeeping cleaners |
| 4240 | Pest Control Workers |
| 4250 | Grounds Maintenance Workers |
| 4300 | First-Line Supervisors of Gaming Workers |
| 4320 | First-Line Supervisors of Personal Service Workers |
| 4340 | Animal Trainers |
| 4350 | Nonfarm Animal Caretakers |
| 4400 | Gaming Services Workers |
| 4410 | Motion Picture Projectionists |
| 4420 | Ushers, Lobby Attendants, and Ticket Takers |
| 4430 | Miscellaneous Entertainment Attendants and Related Workers |
| 4460 | Embalmers and Funeral Attendants |
| 4465 | Morticians, undertakers, and funeral directors |
| 4500 | Barbers |
| 4510 | Hairdressers, Hairstylists, and Cosmetologists |
| 4520 | Miscellaneous Personal Appearance Workers |
| 4530 | Baggage Porters, Bellhops, and Concierges |
| 4540 | Tour and Travel Guides |
| 4600 | Childcare Workers |
| 4610 | Personal Care Aides |
| 4620 | Recreation and Fitness Workers |
| 4640 | Residential Advisors |
| 4650 | Personal Care and Service Workers, All Other |
| 4700 | First-Line Supervisors of Retail Sales Workers |
| 4710 | First-Line Supervisors of Non-Retail Sales Workers |
| 4720 | Cashiers |
| 4740 | Counter and Rental Clerks |
| 4750 | Parts Salespersons |
| 4760 | Retail Salespersons |
| 4800 | Advertising Sales Agents |
| 4810 | Insurance Sales Agents |
| 4820 | Securities, Commodities, and Financial Services Sales Agents |
| 4830 | Travel Agents |
| 4840 | Sales Representatives, Services, All Other |
| 4850 | Sales Representatives, Wholesale and Manufacturing |
| 4900 | Models, Demonstrators, and Product Promoters |
| 4920 | Real Estate Brokers and Sales Agents |
| 4930 | Sales Engineers |
| 4940 | Telemarketers |
| 4950 | Door-to-Door Sales Workers, News and Street Vendors, and Related Workers |
| 4965 | Sales and Related Workers, All Other |
| 5000 | First-Line Supervisors of Office and Administrative Support Workers |
| 5010 | Switchboard Operators, Including Answering Service |
| 5020 | Telephone Operators |
| 5030 | Communications Equipment Operators, All Other |
| 5100 | Bill and Account Collectors |
| 5110 | Billing and Posting Clerks |
| 5120 | Bookkeeping, Accounting, and Auditing Clerks |
| 5130 | Gaming Cage Workers |
| 5140 | Payroll and Timekeeping Clerks |
| 5150 | Procurement Clerks |
| 5160 | Tellers |
| 5165 | Financial clerks, all other |
| 5200 | Brokerage Clerks |
| 5220 | Court, Municipal, and License Clerks |
| 5230 | Credit Authorizers, Checkers, and Clerks |
| 5240 | Customer Service Representatives |
| 5250 | Eligibility Interviewers, Government Programs |
| 5260 | File Clerks |
| 5300 | Hotel, Motel, and Resort Desk Clerks |
| 5310 | Interviewers, Except Eligibility and Loan |
| 5320 | Library Assistants, Clerical |
| 5330 | Loan Interviewers and Clerks |
| 5340 | New Accounts Clerks |
| 5350 | Correspondence clerks and order clerks |
| 5360 | Human resources assistants, except payroll and timekeeping |
| 5400 | Receptionists and Information Clerks |
| 5410 | Reservation and Transportation Ticket Agents and Travel Clerks |
| 5420 | Information and Record Clerks, All Other |
| 5500 | Cargo and Freight Agents |
| 5510 | Couriers and Messengers |
| 5520 | Dispatchers |
| 5530 | Meter Readers, Utilities |
| 5540 | Postal Service Clerks |
| 5550 | Postal Service Mail Carriers |
| 5560 | Postal Service Mail Sorters, Processors, and Processing Machine Operators |
| 5600 | Production, Planning, and Expediting Clerks |
| 5610 | Shipping, Receiving, and Traffic Clerks |
| 5620 | Stock Clerks and Order Fillers |
| 5630 | Weighers, Measurers, Checkers, and Samplers, Recordkeeping |
| 5700 | Secretaries and Administrative Assistants |
| 5800 | Computer Operators |
| 5810 | Data Entry Keyers |
| 5820 | Word Processors and Typists |
| 5840 | Insurance Claims and Policy Processing Clerks |
| 5850 | Mail Clerks and Mail Machine Operators, Except Postal Service |
| 5860 | Office Clerks, General |
| 5900 | Office Machine Operators, Except Computer |
| 5910 | Proofreaders and Copy Markers |
| 5920 | Statistical Assistants |
| 5940 | Miscellaneous office and administrative support workers, including desktop publishers |
| 6005 | First-line supervisors of farming, fishing, and forestry workers |
| 6010 | Agricultural Inspectors |
| 6040 | Graders and Sorters, Agricultural Products |
| 6050 | Miscellaneous agricultural workers, including animal breeders |
| 6100 | Fishing and hunting workers |
| 6120 | Forest and Conservation Workers |
| 6130 | Logging Workers |
| 6200 | First-Line Supervisors of Construction Trades and Extraction Workers |
| 6210 | Boilermakers |
| 6220 | Brickmasons, blockmasons, stonemasons, and reinforcing iron and rebar workers |
| 6230 | Carpenters |
| 6240 | Carpet, Floor, and Tile Installers and Finishers |
| 6250 | Cement Masons, Concrete Finishers, and Terrazzo Workers |
| 6260 | Construction Laborers |
| 6300 | Paving, Surfacing, and Tamping Equipment Operators |
| 6320 | Construction equipment operators except paving, surfacing, and tamping equipment operators |
| 6330 | Drywall Installers, Ceiling Tile Installers, and Tapers |
| 6355 | Electricians |
| 6360 | Glaziers |
| 6400 | Insulation Workers |
| 6420 | Painters and paperhangers |
| 6440 | Pipelayers, Plumbers, Pipefitters, and Steamfitters |
| 6460 | Plasterers and Stucco Masons |
| 6515 | Roofers |
| 6520 | Sheet Metal Workers |
| 6530 | Structural Iron and Steel Workers |
| 6600 | Helpers, Construction Trades |
| 6660 | Construction and Building Inspectors |
| 6700 | Elevator Installers and Repairers |
| 6710 | Fence Erectors |
| 6720 | Hazardous Materials Removal Workers |
| 6730 | Highway Maintenance Workers |
| 6740 | Rail-Track Laying and Maintenance Equipment Operators |
| 6765 | Miscellaneous construction workers, including solar photovoltaic installers, septic tank servicers and sewer pipe cleaners |
| 6800 | Derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining |
| 6820 | Earth Drillers, Except Oil and Gas |
| 6830 | Explosives Workers, Ordnance Handling Experts, and Blasters |
| 6840 | Mining Machine Operators |
| 6940 | Miscellaneous extraction workers, including roof bolters and helpers |
| 7000 | First-Line Supervisors of Mechanics, Installers, and Repairers |
| 7010 | Computer, Automated Teller, and Office Machine Repairers |
| 7020 | Radio and Telecommunications Equipment Installers and Repairers |
| 7030 | Avionics Technicians |
| 7040 | Electric Motor, Power Tool, and Related Repairers |
| 7100 | Electrical and electronics repairers, transportation equipment, and industrial and utility |
| 7110 | Electronic Equipment Installers and Repairers, Motor Vehicles |
| 7120 | Electronic Home Entertainment Equipment Installers and Repairers |
| 7130 | Security and Fire Alarm Systems Installers |
| 7140 | Aircraft Mechanics and Service Technicians |
| 7150 | Automotive Body and Related Repairers |
| 7160 | Automotive Glass Installers and Repairers |
| 7200 | Automotive Service Technicians and Mechanics |
| 7210 | Bus and Truck Mechanics and Diesel Engine Specialists |
| 7220 | Heavy Vehicle and Mobile Equipment Service Technicians and Mechanics |
| 7240 | Small Engine Mechanics |
| 7260 | Miscellaneous Vehicle and Mobile Equipment Mechanics, Installers, and Repairers |
| 7300 | Control and Valve Installers and Repairers |
| 7315 | Heating, Air Conditioning, and Refrigeration Mechanics and Installers |
| 7320 | Home Appliance Repairers |
| 7330 | Industrial and Refractory Machinery Mechanics |
| 7340 | Maintenance and Repair Workers, General |
| 7350 | Maintenance Workers, Machinery |
| 7360 | Millwrights |
| 7410 | Electrical Power-Line Installers and Repairers |
| 7420 | Telecommunications Line Installers and Repairers |
| 7430 | Precision Instrument and Equipment Repairers |
| 7510 | Coin, Vending, and Amusement Machine Servicers and Repairers |
| 7540 | Locksmiths and Safe Repairers |
| 7560 | Riggers |
| 7610 | Helpers--Installation, Maintenance, and Repair Workers |
| 7630 | Miscellaneous installation, maintenance, and repair workers, including wind turbine service technicians |
| 7700 | First-Line Supervisors of Production and Operating Workers |
| 7710 | Aircraft Structure, Surfaces, Rigging, and Systems Assemblers |
| 7720 | Electrical, Electronics, and Electromechanical Assemblers |
| 7730 | Engine and Other Machine Assemblers |
| 7740 | Structural Metal Fabricators and Fitters |
| 7750 | Miscellaneous Assemblers and Fabricators |
| 7800 | Bakers |
| 7810 | Butchers and Other Meat, Poultry, and Fish Processing Workers |
| 7830 | Food and Tobacco Roasting, Baking, and Drying Machine Operators and Tenders |
| 7840 | Food Batchmakers |
| 7850 | Food Cooking Machine Operators and Tenders |
| 7855 | Food processing workers, all other |
| 7900 | Computer Control Programmers and Operators |
| 7920 | Extruding and Drawing Machine Setters, Operators, and Tenders, Metal and Plastic |
| 7930 | Forging Machine Setters, Operators, and Tenders, Metal and Plastic |
| 7940 | Rolling Machine Setters, Operators, and Tenders, Metal and Plastic |
| 7950 | Machine tool cutting setters, operators, and tenders, metal and plastic |
| 8030 | Machinists |
| 8040 | Metal Furnace Operators, Tenders, Pourers, and Casters |
| 8100 | Model makers, patternmakers, and molding machine setters, metal and plastic |
| 8130 | Tool and Die Makers |
| 8140 | Welding, Soldering, and Brazing Workers |
| 8220 | Miscellaneous metal workers and plastic workers, including multiple machine tool setters |
| 8250 | Prepress Technicians and Workers |
| 8255 | Printing Press Operators |
| 8256 | Print Binding and Finishing Workers |
| 8300 | Laundry and Dry-Cleaning Workers |
| 8310 | Pressers, Textile, Garment, and Related Materials |
| 8320 | Sewing Machine Operators |
| 8330 | Shoe and leather workers |
| 8350 | Tailors, Dressmakers, and Sewers |
| 8400 | Textile bleaching and dyeing, and cutting machine setters, operators, and tenders |
| 8410 | Textile Knitting and Weaving Machine Setters, Operators, and Tenders |
| 8420 | Textile Winding, Twisting, and Drawing Out Machine Setters, Operators, and Tenders |
| 8450 | Upholsterers |
| 8460 | Miscellaneous textile, apparel, and furnishings workers except upholsterers |
| 8500 | Cabinetmakers and Bench Carpenters |
| 8510 | Furniture Finishers |
| 8530 | Sawing Machine Setters, Operators, and Tenders, Wood |
| 8540 | Woodworking Machine Setters, Operators, and Tenders, Except Sawing |
| 8550 | Miscellaneous woodworkers, including model makers and patternmakers |
| 8600 | Power Plant Operators, Distributors, and Dispatchers |
| 8610 | Stationary Engineers and Boiler Operators |
| 8620 | Water and Wastewater Treatment Plant and System Operators |
| 8630 | Miscellaneous Plant and System Operators |
| 8640 | Chemical Processing Machine Setters, Operators, and Tenders |
| 8650 | Crushing, Grinding, Polishing, Mixing, and Blending Workers |
| 8710 | Cutting Workers |
| 8720 | Extruding, Forming, Pressing, and Compacting Machine Setters, Operators, and Tenders |
| 8730 | Furnace, Kiln, Oven, Drier, and Kettle Operators and Tenders |
| 8740 | Inspectors, Testers, Sorters, Samplers, and Weighers |
| 8750 | Jewelers and Precious Stone and Metal Workers |
| 8760 | Medical, Dental, and Ophthalmic Laboratory Technicians |
| 8800 | Packaging and Filling Machine Operators and Tenders |
| 8810 | Painting Workers |
| 8830 | Photographic Process Workers and Processing Machine Operators |
| 8850 | Adhesive Bonding Machine Operators and Tenders |
| 8910 | Etchers and Engravers |
| 8920 | Molders, Shapers, and Casters, Except Metal and Plastic |
| 8930 | Paper Goods Machine Setters, Operators, and Tenders |
| 8940 | Tire Builders |
| 8950 | Helpers--Production Workers |
| 8965 | Miscellaneous production workers, including semiconductor processors |
| 9000 | Supervisors of Transportation and Material Moving Workers |
| 9030 | Aircraft Pilots and Flight Engineers |
| 9040 | Air Traffic Controllers and Airfield Operations Specialists |
| 9050 | Flight Attendants |
| 9110 | Ambulance Drivers and Attendants, Except Emergency Medical Technicians |
| 9120 | Bus Drivers |
| 9130 | Driver/Sales Workers and Truck Drivers |
| 9140 | Taxi Drivers and Chauffeurs |
| 9150 | Motor Vehicle Operators, All Other |
| 9200 | Locomotive Engineers and Operators |
| 9240 | Railroad Conductors and Yardmasters |
| 9260 | Subway, streetcar, and other rail transportation workers |
| 9300 | Sailors and marine oilers, and ship engineers |
| 9310 | Ship and Boat Captains and Operators |
| 9350 | Parking Lot Attendants |
| 9360 | Automotive and Watercraft Service Attendants |
| 9410 | Transportation Inspectors |
| 9415 | Transportation attendants, except flight attendants |
| 9420 | Miscellaneous transportation workers, including bridge and lock tenders and traffic technicians |
| 9510 | Crane and Tower Operators |
| 9520 | Dredge, Excavating, and Loading Machine Operators |
| 9560 | Conveyor operators and tenders, and hoist and winch operators |
| 9600 | Industrial Truck and Tractor Operators |
| 9610 | Cleaners of Vehicles and Equipment |
| 9620 | Laborers and Freight, Stock, and Material Movers, Hand |
| 9630 | Machine Feeders and Offbearers |
| 9640 | Packers and Packagers, Hand |
| 9650 | Pumping Station Operators |
| 9720 | Refuse and Recyclable Material Collectors |
| 9750 | Miscellaneous material moving workers, including mine shuttle car operators, and tank car, truck, and ship loaders |
| 9800 | Military Officer Special and Tactical Operations Leaders |
| 9810 | First-Line Enlisted Military Supervisors |
| 9820 | Military Enlisted Tactical Operations and Air/Weapons Specialists and Crew Members |
| 9830 | Military, Rank Not Specified |
| 9999 | NIU |

### CLASSWLY : Class of worker last year
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 10 | Self-employed |
| 13 | Self-employed, not incorporated |
| 14 | Self-employed, incorporated |
| 20 | Works for wages or salary |
| 22 | Wage/salary, private |
| 24 | Wage/salary, government |
| 25 | Federal government employee |
| 27 | State government employee |
| 28 | Local government employee |
| 29 | Unpaid family worker |
| 99 | Missing/Unknown |

### WORKLY : Worked last year
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | No |
| 02 | Yes |

### WKSWORK2 : Weeks worked last year, intervalled
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | 1-13 weeks |
| 2 | 14-26 weeks |
| 3 | 27-39 weeks |
| 4 | 40-47 weeks |
| 5 | 48-49 weeks |
| 6 | 50-52 weeks |
| 9 | Missing data |

### WKSUNEM2 : Weeks unemployed last year, intervalled
| Code | Label |
| :--- | :--- |
| 0 | None |
| 1 | 1-4 weeks |
| 2 | 5-10 weeks |
| 3 | 11-14 weeks |
| 4 | 15-26 weeks |
| 5 | 27-39 weeks |
| 6 | 40+ weeks |
| 7 | Over 26 weeks (1962-1967) |
| 8 | Missing/Unknown |
| 9 | NIU |

### FULLPART : Worked full or part time last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Full-time |
| 2 | Part-time |
| 9 | Unknown |

### NWLOOKWK : Weeks looked for work last year (didn't work)
| Code | Label |
| :--- | :--- |
| 00 | Did not look for work/wasn't on layoff |
| 01 | 1 week |
| 02 | 2 weeks |
| 03 | 3 weeks |
| 04 | 4 weeks |
| 05 | 5 weeks |
| 06 | 6 weeks |
| 07 | 7 weeks |
| 08 | 8 weeks |
| 09 | 9 weeks |
| 10 | 10 weeks |
| 11 | 11 weeks |
| 12 | 12 weeks |
| 13 | 13 weeks |
| 14 | 14 weeks |
| 15 | 15 weeks |
| 16 | 16 weeks |
| 17 | 17 weeks |
| 18 | 18 weeks |
| 19 | 19 weeks |
| 20 | 20 weeks |
| 21 | 21 weeks |
| 22 | 22 weeks |
| 23 | 23 weeks |
| 24 | 24 weeks |
| 25 | 25 weeks |
| 26 | 26 weeks |
| 27 | 27 weeks |
| 28 | 28 weeks |
| 29 | 29 weeks |
| 30 | 30 weeks |
| 31 | 31 weeks |
| 32 | 32 weeks |
| 33 | 33 weeks |
| 34 | 34 weeks |
| 35 | 35 weeks |
| 36 | 36 weeks |
| 37 | 37 weeks |
| 38 | 38 weeks |
| 39 | 39 weeks |
| 40 | 40 weeks |
| 41 | 41 weeks |
| 42 | 42 weeks |
| 43 | 43 weeks |
| 44 | 44 weeks |
| 45 | 45 weeks |
| 46 | 46 weeks |
| 47 | 47 weeks |
| 48 | 48 weeks |
| 49 | 49 weeks |
| 50 | 50 weeks |
| 51 | 51 weeks |
| 52 | 52 weeks |
| 99 | NIU |

### PENSION : Pension plan at work
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No pension plan at work |
| 2 | Pension plan at work, but not included |
| 3 | Included in pension plan at work |

### FIRMSIZE : Number of employees
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Under 10 |
| 2 | 10 to 24 |
| 3 | Under 25 |
| 4 | 10 to 49 |
| 5 | 25 to 99 |
| 6 | 50 to 99 |
| 7 | 100 to 499 |
| 8 | 500 to 999 |
| 9 | 1000+ |

### WANTJOB : Want regular job now
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |
| 3 | Maybe, it depends |
| 4 | Do not know |
| 9 | Unknown |

### WHYPTLY : Reason for working part-time last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Could not find full time job |
| 2 | Wanted part time |
| 3 | Slack work |
| 4 | Other |

### USFTPTLW : Usually work full time (part time last week)
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### PAYIFABS : Paid if absent from work last week
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Not Paid |
| 2 | Paid |
| 3 | Self-employed |

### WNLWNILF : When last worked for pay (NILF last week)
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 10 | Within past 12 months |
| 20 | More than 12 months ago |
| 21 | 1 up to 2 years ago |
| 22 | 2 up to 3 years ago |
| 23 | 3 up to 4 years ago |
| 24 | 4 up to 5 years ago |
| 25 | 5 or more years ago |
| 30 | Never worked |

### STRECHLK : Stretches of looking for work last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | 1 stretch |
| 2 | More than 1 stretch |
| 3 | 2 stretches |
| 4 | 3+ stretches |
| 9 | Not specified |

### WHYNWLY : Reason not working last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Could not find work |
| 2 | Ill or disabled |
| 3 | Taking care of home/family |
| 4 | Going to school |
| 5 | Retired |
| 6 | In Armed Forces |
| 7 | Other |
| 9 | Unknown/missing |

### ACTNLFLY : Activity when not in labor force last year (part-year workers)
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 10 | Ill or disabled |
| 20 | Taking care of home/family |
| 30 | Going to school |
| 40 | Retired |
| 50 | Other |
| 51 | Looking for work |
| 52 | No work available |
| 53 | Doing unpaid work |
| 54 | In Armed Forces |

### PTWEEKS : Weeks working part time last year
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | 1 week |
| 02 | 2 weeks |
| 03 | 3 weeks |
| 04 | 4 weeks |
| 05 | 5 weeks |
| 06 | 6 weeks |
| 07 | 7 weeks |
| 08 | 8 weeks |
| 09 | 9 weeks |
| 10 | 10 weeks |
| 11 | 11 weeks |
| 12 | 12 weeks |
| 13 | 13 weeks |
| 14 | 14 weeks |
| 15 | 15 weeks |
| 16 | 16 weeks |
| 17 | 17 weeks |
| 18 | 18 weeks |
| 19 | 19 weeks |
| 20 | 20 weeks |
| 21 | 21 weeks |
| 22 | 22 weeks |
| 23 | 23 weeks |
| 24 | 24 weeks |
| 25 | 25 weeks |
| 26 | 26 weeks |
| 27 | 27 weeks |
| 28 | 28 weeks |
| 29 | 29 weeks |
| 30 | 30 weeks |
| 31 | 31 weeks |
| 32 | 32 weeks |
| 33 | 33 weeks |
| 34 | 34 weeks |
| 35 | 35 weeks |
| 36 | 36 weeks |
| 37 | 37 weeks |
| 38 | 38 weeks |
| 39 | 39 weeks |
| 40 | 40 weeks |
| 41 | 41 weeks |
| 42 | 42 weeks |
| 43 | 43 weeks |
| 44 | 44 weeks |
| 45 | 45 weeks |
| 46 | 46 weeks |
| 47 | 47 weeks |
| 48 | 48 weeks |
| 49 | 49 weeks |
| 50 | 50 weeks |
| 51 | 51 weeks |
| 52 | 52 weeks |

### SRCSURV1 : First source of survivor benefits
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | Company or union survivor pension |
| 02 | Federal government pension |
| 03 | US military retirement survivor pension |
| 04 | State or local govt survivor pension |
| 05 | US railroad retirement survivor pension |
| 06 | Workers compensation pension |
| 07 | Black lung survivor pension |
| 08 | Regular payments from estates or trusts |
| 09 | Regular payments from annuities or paid-up life insurance |
| 10 | Other or do not know |

### SRCSURV2 : Second source of survivor benefits
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | Company or union survivor pension |
| 02 | Federal government pension |
| 03 | US military retirement survivor pension |
| 04 | State or local govt survivor pension |
| 05 | US railroad retirement survivor pension |
| 06 | Workers compensation pension |
| 07 | Black lung survivor pension |
| 08 | Regular payments from estates or trusts |
| 09 | Regular payments from annuities or paid-up life insurance |
| 10 | Other or do not know |

### SRCDISA1 : First source of disability income
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | Workers compensation |
| 02 | Company or union disability |
| 03 | Federal govt disability |
| 04 | US military retirement disability |
| 05 | State or local govt employee disability |
| 06 | US railroad retirement disability |
| 07 | Accident or disability insurance |
| 08 | Black lung miners disability |
| 09 | State temporary sickness |
| 10 | Other or don't know |

### SRCDISA2 : Second source of disability income
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | Workers compensation |
| 02 | Company or union disability |
| 03 | Federal govt disability |
| 04 | US military retirement disability |
| 05 | State or local govt employee disability |
| 06 | US railroad retirement disability |
| 07 | Accident or disability insurance |
| 08 | Black lung miners disability |
| 09 | State temporary sickness |
| 10 | Other or don't know |

### SRCRET1 : First source of retirement income
| Code | Label |
| :--- | :--- |
| 01 | 401k account |
| 02 | 403b account |
| 03 | Roth IRA |
| 04 | Regular IRA |
| 05 | KEOGH plan |
| 06 | Simplified Employee Pension (SEP) plan |
| 07 | Other type of retirement account |
| 99 | NIU |

### SRCRET2 : Second source of retirement income
| Code | Label |
| :--- | :--- |
| 01 | 401k account |
| 02 | 403b account |
| 03 | Roth IRA |
| 04 | Regular IRA |
| 05 | KEOGH plan |
| 06 | Simplified Employee Pension (SEP) plan |
| 07 | Other type of retirement account |
| 99 | NIU |

### SRCPEN1 : First source of pension income
| Code | Label |
| :--- | :--- |
| 01 | Company pension |
| 02 | Union pension |
| 03 | Federal government pension |
| 04 | State government pension |
| 05 | Local government pension |
| 06 | US military pension |
| 07 | US Railroad Retirement |
| 08 | Other pension |
| 99 | NIU |

### SRCPEN2 : Second source of pension income
| Code | Label |
| :--- | :--- |
| 01 | Company pension |
| 02 | Union pension |
| 03 | Federal government pension |
| 04 | State government pension |
| 05 | Local government pension |
| 06 | US military pension |
| 07 | US Railroad Retirement |
| 08 | Other pension |
| 99 | NIU |

### SRCRINT1 : First source of interest income from a retirement account.
| Code | Label |
| :--- | :--- |
| 01 | 401k account |
| 02 | 403b account |
| 03 | Roth IRA |
| 04 | Regular IRA |
| 05 | KEOGH |
| 06 | Simplified Employee Pension (SEP) plan |
| 07 | Other type of retirement account |
| 99 | NIU |

### SRCRINT2 : Second source of interest income from a retirement account.
| Code | Label |
| :--- | :--- |
| 01 | 401k account |
| 02 | 403b account |
| 03 | Roth IRA |
| 04 | Regular IRA |
| 05 | KEOGH |
| 06 | Simplified Employee Pension (SEP) plan |
| 07 | Other type of retirement account |
| 99 | NIU |

### SRCEARN : Source of earnings from longest job
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Wage and salary |
| 2 | Self employment |
| 3 | Farm self employment |
| 4 | Without pay |

### SRCEDUC : Source of educational assistance
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Government assistance |
| 2 | Scholarships, grants etc from school |
| 3 | Other assistance |
| 4 | Govt assistance and scholarships, grants etc from school |
| 5 | Govt assistance and other assistance |
| 6 | Scholarships, grants etc from school and other assistance |
| 7 | Govt assistance, scholarships, grants etc from school, and other assistance |

### SRCUNEMP : Source of unemployment income
| Code | Label |
| :--- | :--- |
| 0 | No supplemental or strike benefits |
| 1 | Supplemental unemployment benefits |
| 2 | Union unemployment or strike benefits |
| 3 | Both |
| 9 | NIU |

### SRCWELFR : Source of welfare income
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | AFDC/TANF |
| 2 | Other |
| 3 | Both AFDC/TANF and other |

### SRCWKCOM : Source of workmen's compensation
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | State Workers Compensation |
| 2 | Employer or employers insurance |
| 3 | Own insurance |
| 4 | Other |

### VETQA : Required to fill out annual income questionnaire for veterans' administration
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### WHYSS1 : First reason for receiving social security income
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Retired |
| 2 | Disabled (adult or child) |
| 3 | Widowed |
| 4 | Spouse |
| 5 | Surviving child |
| 6 | Dependent child |
| 7 | On behalf of surviving, dependent, or disabled child(ren) |
| 8 | Other (adult or child) |

### WHYSS2 : Second reason for receiving social security income
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Retired |
| 2 | Disabled (adult or child) |
| 3 | Widowed |
| 4 | Spouse |
| 5 | Surviving child |
| 6 | Dependent child |
| 7 | On behalf of surviving, dependent, or disabled child(ren) |
| 8 | Other (adult or child) |

### WHYSSI1 : First reason for receiving supplementary security income
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Disabled (adult or child) |
| 2 | Blind (adult or child) |
| 3 | On behalf of a disabled child |
| 4 | On behalf of a blind child |
| 5 | Other (adult or child) |

### WHYSSI2 : Second reason for receiving supplementary security income
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Disabled (adult or child) |
| 2 | Blind (adult or child) |
| 3 | On behalf of a disabled child |
| 4 | On behalf of a blind child |
| 5 | Other (adult or child) |

### GOTVDISA : Received veterans' disability compensation
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### GOTVEDUC : Received veterans' education assistance
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### GOTVOTHE : Received other veterans' payments
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### GOTVPENS : Received veterans' pension
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### GOTVSURV : Received veterans' survivor benefits
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### FILESTAT : Tax filer status
| Code | Label |
| :--- | :--- |
| 0 | No data |
| 1 | Joint, both less than 65 |
| 2 | Joint, one less than 65, one 65+ |
| 3 | Joint, both 65+ |
| 4 | Head of household |
| 5 | Single |
| 6 | Nonfiler |

### MIGSTA1 : State of residence 1 year ago
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | Alabama |
| 02 | Alaska |
| 04 | Arizona |
| 05 | Arkansas |
| 06 | California |
| 08 | Colorado |
| 09 | Connecticut |
| 10 | Delaware |
| 11 | District of Columbia |
| 12 | Florida |
| 13 | Georgia |
| 15 | Hawaii |
| 16 | Idaho |
| 17 | Illinois |
| 18 | Indiana |
| 19 | Iowa |
| 20 | Kansas |
| 21 | Kentucky |
| 22 | Louisiana |
| 23 | Maine |
| 24 | Maryland |
| 25 | Massachusetts |
| 26 | Michigan |
| 27 | Minnesota |
| 28 | Mississippi |
| 29 | Missouri |
| 30 | Montana |
| 31 | Nebraska |
| 32 | Nevada |
| 33 | New Hampshire |
| 34 | New Jersey |
| 35 | New Mexico |
| 36 | New York |
| 37 | North Carolina |
| 38 | North Dakota |
| 39 | Ohio |
| 40 | Oklahoma |
| 41 | Oregon |
| 42 | Pennsylvania |
| 44 | Rhode Island |
| 45 | South Carolina |
| 46 | South Dakota |
| 47 | Tennessee |
| 48 | Texas |
| 49 | Utah |
| 50 | Vermont |
| 51 | Virginia |
| 53 | Washington |
| 54 | West Virginia |
| 55 | Wisconsin |
| 56 | Wyoming |
| 91 | Abroad |
| 99 | Same house |

### WHYMOVE : Reason for moving
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 01 | Change in marital status |
| 02 | To establish own household |
| 03 | Other family reason |
| 04 | New job or job transfer |
| 05 | To look for work or lost job |
| 06 | For easier commute |
| 07 | Retired |
| 08 | Other job-related reason |
| 09 | Wanted to own home, not rent |
| 10 | Wanted new or better housing |
| 11 | Wanted better neighborhood |
| 12 | For cheaper housing |
| 13 | Other housing reason |
| 14 | Attend/leave college |
| 15 | Change of climate |
| 16 | Health reasons |
| 17 | Other reasons |
| 18 | Natural disaster |
| 19 | Foreclosure or eviction |
| 20 | Relationship with unmarried partner |

### MIGRATE1 : Migration status, 1 year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Same house |
| 2 | Different house, place not reported |
| 3 | Moved within county |
| 4 | Moved within state, different county |
| 5 | Moved between states |
| 6 | Abroad |
| 9 | Unknown |

### PAIDGH : Employer paid for group health plan
| Code | Label |
| :--- | :--- |
| 00 | NIU |
| 10 | No |
| 20 | Yes |
| 21 | Yes, paid for part |
| 22 | Yes, paid for all |

### HIMCAIDLY : Covered by Medicaid last year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### HIMCARELY : Covered by Medicare last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### HIMCAIDNW : Current Medicaid, CHIP, or other means-tested coverage
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### HIMCARENW : Current Medicare coverage
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### HICHAMP : Covered by military health insurance last year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### PHINSUR : Reported covered by private health insurance last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### PHIOWN : Private health insurance in own name last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### CAIDLY : Covered by Medicaid last year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### CAIDNW : Current Medicaid coverage
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### CAIDPART : Medicaid coverage for all or part of last year
| Code | Label |
| :--- | :--- |
| 01 | Covered part of last year |
| 02 | Covered all of last year |
| 99 | NIU |

### ANYCOVLY : Any health insurance coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### ANYCOVNW : Covered by health insurance at time of interview
| Code | Label |
| :--- | :--- |
| 1 | Covered |
| 2 | Not covered |

### PUBCOVLY : Any government health insurance coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### PUBCOVNW : Any current government health insurance coverage
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### ANYPART : Any insurance coverage for all or part of last year
| Code | Label |
| :--- | :--- |
| 01 | Covered part of last year |
| 02 | Covered all of last year |
| 99 | NIU |

### PUBPART : Government insurance coverage for all or part of last year
| Code | Label |
| :--- | :--- |
| 01 | Covered part of last year |
| 02 | Covered all of last year |
| 99 | NIU |

### PRVTPART : Private insurance coverage for all or part of last year
| Code | Label |
| :--- | :--- |
| 01 | Covered part of last year |
| 02 | Covered all of last year |
| 99 | NIU |

### PRVTCOVLY : Any private coverage last year (2019 definition)
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### PRVTDEPLY : Private insurance through a household member last year (2019 definition)
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### PRVTOWNLY : Policyholder for private insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### PRVTCOUTLY : Private insurance coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### PRVTCOVNW : Currently covered by private insurance
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### PRVTDEPNW : Currently have private health insurance through a household member
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### PRVTOWNNW : Policyholder for current private insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### PRVTCOUTNW : Current private coverage provided by person outside the household
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### GRPCOVLY : Covered by employment-based group health last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### GRPDEPLY : Dependent covered by employment-based insurance last year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### GRPOWNLY : Policyholder for employment-based insurance last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### GRPOUTLY : Employment-based insurance covered non-household member
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### GRPCOUTLY : Employment-based insurance coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### GRPTYPLY : Type of employment-based coverage last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Family plan |
| 2 | Self only plan |
| 3 | Self plus one plan |

### GRPWHO1 : Line number of first policyholder of employment-based insurance
| Code | Label |
| :--- | :--- |
| 00 | Not covered by 1st group policy of hh member |
| 01 | 1 |
| 02 | 2 |
| 03 | 3 |
| 04 | 4 |
| 05 | 5 |
| 06 | 6 |
| 07 | 7 |
| 08 | 8 |
| 09 | 9 |
| 10 | 10 |
| 11 | 11 |
| 12 | 12 |
| 13 | 13 |
| 14 | 14 |
| 15 | 15 |
| 16 | 16 |

### GRPCOVNW : Currently covered by employment-based insurance
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### GRPDEPNW : Dependent currently covered by employment-based insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### GRPOWNNW : Policyholder for current employment-based insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### GRPOUTNW : Current employment-based coverage covers non-household member
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### GRPCOUTNW : Current employment-based coverage provided by person outside the household
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### GRPTYPNW : Type of current employment-based plan
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### GRPWHONW : Policyholder line number for current employment-based coverage
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### DPCOVLY : Direct-purchase insurance coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### DPDEPLY : Dependent for direct-purchase insurance, previous year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### DPOWNLY : Policyholder for direct-purchase insurance, previous year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### DPOUTLY : Direct-purchase private coverage for non-hh member last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### DPCOUTLY : Direct-purchase insurance coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### DPTYPLY : Type of direct-purchase insurance plan, previous year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | Family plan |
| 2 | Self only plan |
| 3 | Self plus one plan |

### DPWHO1 : Line number of first policyholder of direct-purchase insurance, previous year
| Code | Label |
| :--- | :--- |
| 00 | Not covered by 1st private policy of hh member |
| 01 | 1 |
| 02 | 2 |
| 03 | 3 |
| 04 | 4 |
| 05 | 5 |
| 06 | 6 |
| 07 | 7 |
| 08 | 8 |
| 09 | 9 |
| 10 | 10 |
| 11 | 11 |
| 12 | 12 |
| 13 | 13 |
| 14 | 14 |
| 15 | 15 |
| 16 | 16 |

### DPCOVNW : Currently covered by direct-purchase insurance
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### DPDEPNW : Dependent currently covered by direct-purchase insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### DPOWNNW : Policyholder for current direct-purchase insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### DPOUTNW : Current direct-purchase coverage covers non-household member
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### DPCOUTNW : Current direct-purchase coverage provided by person outside the household
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### DPTYPNW : Type of current direct-purchase plan
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### DPWHONW : Policyholder line number for current direct-purchase coverage
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### MRKCOVLY : Any Marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKDEPLY : Dependent covered by marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKOWNLY : Policyholder for marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKOUTLY : Marketplace insurance covered non-household member last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKCOUTLY : Marketplace insurance coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKTYPLY : Type of marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### MRKWHO1 : Line number of policy holder of marketplace insurance
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### MRKCOVNW : Currently covered by marketplace insurance
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### MRKDEPNW : Dependent currently covered by marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKOWNNW : Policyholder for current marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKOUTNW : Current marketplace coverage covers non-household member.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKCOUTNW : Current marketplace coverage provided by person outside the household.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKTYPNW : Type of current marketplace plan
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### MRKWHONW : Policyholder line number for current marketplace coverage
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### MRKSCOVLY : Any subsidized marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSDEPLY : Dependent covered by subsidized marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSOWNLY : Policyholder for subsidized marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSOUTLY : Subsidized marketplace insurance covered non-household member last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSCOUTLY : Subsidized marketplace insurance coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSTYPLY : Type of subsidized marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### MRKSWHO1 : Line number of policy holder of subsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### MRKSCOVNW : Currently covered by subsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### MRKSDEPNW : Dependent currently covered by subsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSOWNNW : Policyholder for current subsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSOUTNW : Current subsidized marketplace coverage covers non-household member.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSCOUTNW : Current subsidized marketplace coverage provided by person outside the household.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKSTYPNW : Type of current subsidized marketplace plan
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### MRKSWHONW : Policyholder line number for current subsidized marketplace coverage
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### MRKUCOVLY : Any unsubsidized marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUDEPLY : Dependent covered by unsubsidized marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUOWNLY : Policyholder for unsubsidized marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUOUTLY : Unsubsidized marketplace insurance covered non-household member last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUCOUTLY : Unsubsidized marketplace insurance coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUTYPLY : Type of unsubsidized marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### MRKUWHO1 : Line number of policy holder of unsubsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### MRKUCOVNW : Currently covered by unsubsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### MRKUDEPNW : Dependent currently covered by unsubsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUOWNNW : Policyholder for current unsubsidized marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUOUTNW : Current unsubsidized marketplace coverage covers non-household member.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUCOUTNW : Current unsubsidized marketplace coverage provided by person outside the household.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### MRKUTYPNW : Type of current unsubsidized marketplace plan
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### MRKUWHONW : Policyholder line number for current unsubsidized marketplace coverage
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### NMCOVLY : Any non-marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMDEPLY : Dependent covered by non-marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMOWNLY : Policyholder for non-marketplace insurance last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMOUTLY : Non-marketplace insurance covered non-household member last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMCOUTLY : Non-marketplace insurance coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMTYPLY : Type of non-marketplace coverage last year
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### NMWHO1 : Line number of policy holder of non-marketplace insurance
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### NMCOVNW : Currently covered by non-marketplace insurance
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### NMDEPNW : Dependent currently covered by non-marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMOWNNW : Policyholder for current non-marketplace insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMOUTNW : Current unsubsidized marketplace coverage covers non-household member.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMCOUTNW : Current non-marketplace coverage provided by person outside the household.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### NMTYPNW : Type of current non-marketplace plan
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### NMWHONW : Policyholder line number for current non-marketplace coverage
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### TRCCOVLY : Covered by Champus/Tricare last year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### TRCDEPLY : Dependent covered by TRICARE last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCOWNLY : Policyholder for TRICARE last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCOUTLY : TRICARE covered non-household member last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCCOUTLY : TRICARE coverage through someone outside the household last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCTYPLY : Type of TRICARE coverage last year
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### TRCWHO1 : Line number of policy holder of TRICARE
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### TRCCOVNW : Currently covered by TRICARE
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### TRCDEPNW : Dependent currently covered by TRICARE
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCOWNNW : Policyholder for current TRICARE insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCOUTNW : Current TRICARE coverage covers non-household member.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCCOUTNW : Current TRICARE coverage provided by person outside the household.
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### TRCTYPNW : Type of current TRICARE plan
| Code | Label |
| :--- | :--- |
| 01 | Family plan |
| 02 | Self only plan |
| 03 | Self plus one plan |
| 99 | NIU |

### TRCWHONW : Policyholder line number for current TRICARE coverage
| Code | Label |
| :--- | :--- |
| 99 | NIU |

### CHAMPVALY : Covered by CHAMPVA last year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### CHAMPVANW : Current CHAMPVA coverage
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### INHCOVLY : Covered by Indian Health Service last year
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
| 9 | NIU |

### INHCOVNW : Respondent currently covered by Indian Health Service
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### VACOVLY : VACARE coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### VACOVNW : Current VACARE coverage
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### SCHIPLY : State Children's Health Insurance Program coverage last year
| Code | Label |
| :--- | :--- |
| 0 | NIU |
| 1 | No |
| 2 | Yes |

### SCHIPNW : Current State Children's Health Insurance Program coverage
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |

### MULTCOV : Concurent health insurance coverage last year
| Code | Label |
| :--- | :--- |
| 01 | No months with concurrent coveraage |
| 02 | Some moths with concurrent coverage |
| 03 | Concurrent coverage all year |
| 99 | NIU |

### HIELIG : Person was eligible to purchase employer's health insurance plan if one was offered
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINELIG1 : Ineligible for employer health insurance: Don't work enough hours per week or weeks per year
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINELIG2 : Ineligible for employer health insurance: Contract or temporary employees not allowed in plan
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINELIG3 : Ineligible for employer health insurance: Haven't worked for employer long enough to be covered
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINELIG4 : Ineligible for employer health insurance: Have a pre-existing condition
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINELIG5 : Ineligible for employer health insurance: Too expensive
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINELIG6 : Ineligible for employer health insurance: Other/specify
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE1 : Did not purchase employer health insurance: covered by another plan
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE2 : Did not purchase employer health insurance: Traded health insurance for higher pay
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE3 : Did not purchase employer health insurance: Too expensive
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE4 : Did not purchase employer health insurance: Don't need health insurance
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE5 : Did not purchase employer health insurance: Have pre-existing condition
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE6 : Did not purchase employer health insurance: Haven't worked for employer long enough to be covered
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE7 : Did not purchase employer health insurance: Contract or temp employees not allowed in plan
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HINTAKE8 : Did not purchase employer health insurance: other/specify
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### HIOFFER : Person's employer offers health insurance to any of its employees
| Code | Label |
| :--- | :--- |
| 01 | No |
| 02 | Yes |
| 99 | NIU |

### QHIELIG : Data quality flag for HIELIG [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHIELIGD : Data quality flag for HIELIG [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINELIG1 : Data quality flag for HINELIG1 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINELIG1D : Data quality flag for HINELIG1 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINELIG2 : Data quality flag for HINELIG2 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINELIG2D : Data quality flag for HINELIG2 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINELIG3 : Data quality flag for HINELIG3 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINELIG3D : Data quality flag for HINELIG3 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINELIG4 : Data quality flag for HINELIG4 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINELIG4D : Data quality flag for HINELIG4 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINELIG5 : Data quality flag for HINELIG5 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINELIG5D : Data quality flag for HINELIG5 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINELIG6 : Data quality flag for HINELIG6 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINELIG6D : Data quality flag for HINELIG6 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE1 : Data quality flag for HINTAKE1 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE1D : Data quality flag for HINTAKE1 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE2 : Data quality flag for HINTAKE2 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE2D : Data quality flag for HINTAKE2 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE3 : Data quality flag for HINTAKE3 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE3D : Data quality flag for HINTAKE3 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE4 : Data quality flag for HINTAKE4 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE4D : Data quality flag for HINTAKE4 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE5 : Data quality flag for HINTAKE5 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE5D : Data quality flag for HINTAKE5 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE6 : Data quality flag for HINTAKE6 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE6D : Data quality flag for HINTAKE6 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE7 : Data quality flag for HINTAKE7 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE7D : Data quality flag for HINTAKE7 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHINTAKE8 : Data quality flag for HINTAKE8 [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHINTAKE8D : Data quality flag for HINTAKE8 [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### QHIOFFER : Data quality flag for HIOFFER [general version]
| Code | Label |
| :--- | :--- |
| 0 | Not allocated |
| 1 | Allocated |

### QHIOFFERD : Data quality flag for HIOFFER [detailed version]
| Code | Label |
| :--- | :--- |
| 00 | Not allocated |
| 10 | Allocated |
| 11 | Hotdeck imputation |
| 12 | Logical imputation |
| 13 | Whole unit imputation |

### OUT : Covered by policy of person outside the household
| Code | Label |
| :--- | :--- |
| 1 | No |
| 2 | Yes |
