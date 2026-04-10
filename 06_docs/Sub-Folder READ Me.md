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
