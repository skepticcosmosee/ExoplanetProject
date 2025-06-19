import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier  # Optional: Try more models

from src.data_loader import load_exoplanet_data
from src.preprocess import preprocess_data

def train_model(df):
    # Step 1: Choose features (X) and target (y)
    X = df.drop(columns=['pl_bmasse'])  # drop target
    y = (df['pl_bmasse'] > 2).astype(int)  # Binary classification: "massive" planet or not

    # Step 2: Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 3: Initialize and train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Step 4: Evaluate model
    y_pred = model.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred,labels=[0,1]))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    return model


if __name__ == "__main__":
    filepath = "data/kepler_data.csv"
    df = load_exoplanet_data(filepath)

    if df is not None:
        df = preprocess_data(df)
        model = train_model(df)
