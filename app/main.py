from app.model import load_model, features
import pandas as pd
from app.schema import EmployeeTerm
from fastapi import FastAPI

app = FastAPI()

model = load_model()

#API EndPoints
@app.get("/")
def home():
    return "Home Page"
@app.post("/predict")
def predict(data:EmployeeTerm):
    input_data =pd.DataFrame([
        data.dict()
    ],columns=features)

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0]

    return{
        "Predicted_Termination":int(prediction),
        "Status":"Termination" if prediction == 1 else "Active",
        "Probability":{
            "Active":prob[0],
            "Terminated":prob[1]
        }
    }