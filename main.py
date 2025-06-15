# main.py

import sys
print(sys.path)

from src.data_loader import load_exoplanet_data
from src.eda import run_eda
from src.feature_engineering import add_features


def main():
    filepath = "data/kepler_data.csv"
    df = load_exoplanet_data(filepath)
    print(type(df))

    if df is None:
        print("Data loading failed. Exiting...")
        return  # stop running if data load failed

    df = run_eda(df)
    df = add_features(df)

    print(df[['pl_rade', 'pl_bmasse', 'pl_density']].head())

if __name__ == "__main__":
    main()

