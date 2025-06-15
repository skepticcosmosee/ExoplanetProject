import pandas as pd
from data_loader import load_exoplanet_data

def clean_data(filepath):
    data = load_exoplanet_data(filepath)
    if data is None:
        return None

    # Focus on key columns
    cols = ['pl_rade', 'pl_bmasse', 'st_teff']

    # How many missing values in these columns?
    print("Missing values before cleaning:")
    print(data[cols].isnull().sum())

    # Drop rows where any of these are missing
    data_clean = data.dropna(subset=cols)

    print("\nMissing values after dropping:")
    print(data_clean[cols].isnull().sum())

    return data_clean

if __name__ == "__main__":
    cleaned = clean_data('data/kepler_data.csv')
    if cleaned is not None:
        print(f"Data size before cleaning: {len(cleaned)} rows")
        print(f"Data size after cleaning: {len(cleaned)} rows")
