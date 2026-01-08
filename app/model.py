import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
 
features = ['EmpSatisfaction']
target = ['Termd']
 
MODEL_PATH = "model/logistic_termination_model.pkl"
 
def train_model():
    df = pd.read_csv('data/HR_Dataset Refresh.csv')
 
    X = df[features]
    Y = df[target]
 
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )
 
    model = LogisticRegression(
        solver='liblinear',
        random_state=42
    )
 
    model.fit(X_train, Y_train)
 
    joblib.dump(model, MODEL_PATH)
    return model
 
def load_model():
    return joblib.load(MODEL_PATH)