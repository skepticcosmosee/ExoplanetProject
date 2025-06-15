import pandas as pd

def load_exoplanet_data(filepath):
    try:
        df = pd.read_csv(filepath,comment='#',sep=',')
        print(f"Loaded {len(df)} rows from {filepath}")
        return df
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None

if __name__ == "__main__":
    data = load_exoplanet_data("data/kepler_data.csv")
    if data is not None:
        print(data.head())          
        print(data.columns)         
