import pandas as pd

from .data_loader import load_exoplanet_data


def run_eda(data):
    data = load_exoplanet_data('data/kepler_data.csv')
    if data is None:
        return

    print("Basic info:")
    print(data.info())

    print("\nSummary statistics:")
    print(data.describe())

    print("\nMissing values per column:")
    print(data.isnull().sum())

    print("\nSample data:")
    print(data.head())

    return data

if __name__ == "__main__":
    run_eda()
