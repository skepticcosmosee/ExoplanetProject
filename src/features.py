import numpy as np
import pandas as pd

from data_loader import load_exoplanet_data

def add_features(data):
    earth_radious_m=6.371e6
    eart_mass_kg=5.972e24

    radius_m=data['p1_rade']