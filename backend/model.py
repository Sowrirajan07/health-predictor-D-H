# model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# ------------------ Diabetes ------------------
diabetes = pd.read_csv("datasets/diabetes.csv", header=None)

diabetes.columns = ["Pregnancies","Glucose","BP","SkinThickness",
                    "Insulin","BMI","DPF","Age","Outcome"]

X_d = diabetes.drop("Outcome", axis=1)
y_d = diabetes["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X_d, y_d, test_size=0.2)

model_d = RandomForestClassifier()
model_d.fit(X_train, y_train)

pickle.dump(model_d, open("diabetes_model.pkl", "wb"))

# ------------------ Heart ------------------
heart = pd.read_csv("datasets/heart.csv")

X_h = heart.drop("target", axis=1)
y_h = heart["target"]

X_train, X_test, y_train, y_test = train_test_split(X_h, y_h, test_size=0.2)

model_h = RandomForestClassifier()
model_h.fit(X_train, y_train)

pickle.dump(model_h, open("heart_model.pkl", "wb"))

print("Both models trained!")