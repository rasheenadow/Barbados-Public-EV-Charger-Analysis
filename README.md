# Barbados-Public-EV-Charger-Analysis

## Project Title & Description
**Project Title:** Barbados Public EV Charging Analysis: Access, Demand, Utilisation, and Equity
**Description:** A data science capstone project analysing access, demand, utilisation, and equity across Barbados’ public EV charging network to identify priority parish locations for charger expansion, upgrades, and new installations in support of improved accessibility and national electrification goals.

**Data Utilised:** The analysis focussed on three main data types:

Operational data (Source: Megapower Ltd. Public EV Charging Network 2025): 
- EV charging session records (e.g., session duration, energy delivered, timestamps, session counts) - file: Barbados_public_EV_charger_sessions_full_2025_cleaned.csv;
- EV statistics records (e.g., charger ID, number of unique drivers, number of sessions, geolocation) - file: Barbados_public_EV_charger_statistics_2025_cleaned.csv

Geospatial data (Source:GADM v4.1): Barbados Parish Boundaries – this data was accessed programmatically via the geodata R package. It provides official administrative boundaries for spatial analysis and mapping of EV charging infrastructure.

Demographic data (Source: Barbados Poulation Census Data 2020): Parish-level population statistics - file: Barbados_2020_Population_by_Parish.csv

## File Organization
- 'raw_data/' – Original datasets (CSV, TXT, GIS layers, or other unmodified files).
- 'processed_data/' – Cleaned and transformed datasets ready for analysis.
- 'scripts/' – R scripts used for data cleaning, exploratory data anaylsis (including outlier analysis) and final analysis
- 'metadata/' – Data dictionaries, variable descriptions, and data provenance.
- 'outputs/ – Generated figures, tables, maps, and summary results.

## Requirements
**Software:**

 R (4.0+) - for all data cleaning, analysis and visualisation; R packages: library(sf), library(ggplot2), library(ggspatial), library(geodata), library(dplyr), library(ggrepel), library(tidyverse), library(scales), library(ggthemes), library(lubridate), library(patchwork)

*Note*: The project files were uploaded directly to GitHub due to persistent authentication and merge conflict issues encountered during the development process, which could not be fully resolved prior to the project deadline. Alternatively, the repository could have been updated using a Python (3.12.10) script in CoCalc to automate the Git push process. A sample script has been included for reproducibility via Python, where the relevant username, email address and personal access token would need to be entered.

## Contact Info
**Name:** Rasheena Dow
**Email:** rasheenadow@gmail.com

## License
Educational use only – This project and its contents are for learning and non-commercial use.
