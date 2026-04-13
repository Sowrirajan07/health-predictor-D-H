import pickle
import numpy as np

# Load models
diabetes_model = pickle.load(open("diabetes_model.pkl", "rb"))
heart_model = pickle.load(open("heart_model.pkl", "rb"))

def predict_diabetes(data):
    data = np.array(data).reshape(1, -1)
    
    prob = diabetes_model.predict_proba(data)[0][1]  # probability
    pred = diabetes_model.predict(data)[0]
    
    return int(pred), float(prob)

def predict_heart(data):
    data = np.array(data).reshape(1, -1)
    
    prob = heart_model.predict_proba(data)[0][1]
    pred = heart_model.predict(data)[0]
    
    return int(pred), float(prob)