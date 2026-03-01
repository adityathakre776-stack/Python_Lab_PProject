
# hardcore_ml_module.py
# Advanced ML Training Module for SmartEdge ML Platform

import pandas as pd
import numpy as np
import json
import sys
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

def train_model(file_path, target_column, algorithm):

    # Load dataset
    data = pd.read_csv(file_path)

    # Encode categorical columns
    for col in data.columns:
        if data[col].dtype == 'object':
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])

    # Separate features and target
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Select algorithm dynamically
    if algorithm == "Logistic Regression":
        model = LogisticRegression(max_iter=1000)
    elif algorithm == "Decision Tree":
        model = DecisionTreeClassifier()
    elif algorithm == "Random Forest":
        model = RandomForestClassifier()
    elif algorithm == "KNN":
        model = KNeighborsClassifier()
    elif algorithm == "SVM":
        model = SVC()
    elif algorithm == "Linear Regression":
        model = LinearRegression()
    elif algorithm == "Decision Tree Regressor":
        model = DecisionTreeRegressor()
    elif algorithm == "Random Forest Regressor":
        model = RandomForestRegressor()
    else:
        raise ValueError("Unsupported Algorithm Selected")

    # Train model
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Prepare results
    results = {}

    # Classification Metrics
    if algorithm in ["Logistic Regression", "Decision Tree", "Random Forest", "KNN", "SVM"]:
        results["accuracy"] = float(accuracy_score(y_test, y_pred))
        results["precision"] = float(precision_score(y_test, y_pred, average='weighted'))
        results["recall"] = float(recall_score(y_test, y_pred, average='weighted'))
        results["f1_score"] = float(f1_score(y_test, y_pred, average='weighted'))

    # Regression Metrics
    else:
        results["r2_score"] = float(r2_score(y_test, y_pred))

    return results


if __name__ == "__main__":
    # Example usage:
    # python hardcore_ml_module.py dataset.csv target_column "Logistic Regression"

    file_path = sys.argv[1]
    target_column = sys.argv[2]
    algorithm = sys.argv[3]

    output = train_model(file_path, target_column, algorithm)
    print(json.dumps(output))
