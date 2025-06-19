# src/preprocessor.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(df):
    """
    Perform preprocessing steps on the exoplanet dataset.
    Returns the cleaned and transformed DataFrame.
    """
    df = df.copy()
    # 5. Add Goldilocks Habitability Label
    # Define habitability based on stellar temperature and orbital distance
    temp_cond = (df['st_teff'] >= 4800) & (df['st_teff'] <= 6300)
    orbit_cond = (df['pl_orbsmax'] >= 0.95) & (df['pl_orbsmax'] <= 1.37)
    mass_cond = df['pl_bmasse'] > 2

    df['is_habitable'] = (temp_cond & orbit_cond & mass_cond).astype(int)



    # 1. Drop rows with missing target values (if any)
    df.dropna(subset=['pl_bmasse', 'pl_rade'], inplace=True)

    # 2. Fill or drop remaining missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # 3. Encode categorical columns
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    # 4. Scale numerical features
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])



    return df

if __name__ == "__main__":
    from data_loader import load_exoplanet_data

    df = load_exoplanet_data("data/kepler_data.csv")
    if df is not None:
        df_clean = preprocess_data(df)
        print(df_clean.head())
