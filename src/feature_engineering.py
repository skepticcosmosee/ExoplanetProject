import pandas as pd
import numpy as np

def add_features(data):
    r=data['pl_rade']
    m=data['pl_bmasse']

    volume=(4/3)*np.pi*(r**3)
    density=m/volume

    data['pl_density']=density

    return data

if __name__=="__main__":
    from data_loader import load_exoplanet_data

    filepath="data/kepler_data.csv"
    df=load_exoplanet_data(filepath)

    if df is not None:
        df=add_features(df)
        print(df[['pl_rade', 'pl_bmasse', 'pl_density']].head())