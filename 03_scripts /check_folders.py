# EV-Charger_Capstone: Folder Check with Visualization
import os

# List of main folders in the project
folders = [
    "01_raw_data",
    "02_processed_data",
    "03_scripts",
    "04_metadata",
    "05_outputs"
    "06_docs"

]

# Check folder existence
status = []
for folder in folders:
    if os.path.exists(folder):
        print(f"✔ Found folder: {folder}")
        status.append(1)
    else:
        print(f"❌ Missing folder: {folder}")
        status.append(0)

print("\nFolder check complete.")
