# 01_raw_data

This folder contains the original, unmodified datasets used in the analysis.

## Notes
- Files are kept in their original form for transparency and reproducibility.
- Do not edit these files.
- All cleaning and processing is captured in `/02_processed_data`.

## Sources
- Megapower Ltd. Public EV Charging Network (2025): Sessions File; Statistics File
- Barbados Population Census (2020)

# 02_processed_data

This folder contains cleaned and analysis-ready datasets.

## Contents
- EV charging session data (cleaned)
- EV charger statistics (cleaned)
- Parish-level population data (cleaned)

## Notes
- Data has been cleaned, standardised, and prepared for analysis.
- Files are generated using scripts in `/03_scripts`.
- Do not manually edit.

# 03_scripts

This folder contains R scripts used for data cleaning, analysis, and visualisation.

Note: The project files were uploaded directly to GitHub due to persistent authentication and merge conflict issues encountered during the development process, which could not be fully resolved prior to the project deadline. Alternatively, the repository could have been updated using a Python (3.12.10) script in CoCalc to automate the Git push process. A sample script has been included for reproducibility via Python, where the relevant username, email address and personal access token would need to be entered.

## Includes
- Data preprocessing and cleaning
- Exploratory data analysis (EDA); including some outlier analysis
- Spatial and statistical analysis
- Visualisation code

## Notes
- Scripts use data from `/02_processed_data`.
- Use relative paths for reproducibility.

# 04_metadata

This folder contains documentation about the datasets used in the project.

## Includes
- Data dictionaries
- Variable descriptions
- Data sources and processing notes

## Purpose
Supports transparency and helps users understand the data.

# 05_outputs

This folder contains results generated from the analysis.

## Includes
- Charts and visualisations
- Maps

## Notes
- Outputs are created using scripts in `/03_scripts`.
- Files should not be manually edited.
