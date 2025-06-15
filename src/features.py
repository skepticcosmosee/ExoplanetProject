import pandas as pd
import numpy as np
from data_loader import load_exoplanet_data  # Import your loader function

def add_features(data):
    earth_radius_m = 6.371e6
    earth_mass_kg = 5.972e24

    radius_m = data['pl_rade'] * earth_radius_m
    volume = (4/3) * np.pi * radius_m**3
    mass_kg = data['pl_bmasse'] *earth_mass_kg

    data['density'] = mass_kg / volume

    data['esi'] = (
        (data['pl_rade'] / 1.0).clip(0, 2) +
        (data['pl_bmasse'] / 1.0).clip(0, 2) +
        (data['pl_insol'] / 1.0).clip(0, 2)
    ) / 3

    data['habitable_zone'] = data['pl_insol'].between(0.75, 1.5)

    return data

def save_enhanced_data(data, filepath):
    data.to_csv(filepath, index=False)
    print(f"Saved enhanced data with features to {filepath}")

if __name__ == "__main__":
    cleaned_data_path = 'data/kepler_data.csv'
    df_clean = load_exoplanet_data(cleaned_data_path)  # Use imported function

    if df_clean is not None:
        df_features = add_features(df_clean)
        enhanced_data_path = 'data/kepler_data.csv'
        save_enhanced_data(df_features, enhanced_data_path)
    else:
        print("Failed to load cleaned data, cannot add features.")