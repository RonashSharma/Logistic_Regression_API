import streamlit as st
import requests
import pandas as pd 

API_URL = "https://logistic-regression-api-1-vtx3.onrender.com/predict"

emp_satisfaction = st.slider(
    'Employee Satisfaction',
    min_value=1,
    max_value=5,
    value=3,
    step=1
)

if st.button("Predict Employee Termination or Active "):
    payload={
        "EmpSatisfaction":emp_satisfaction
    }

    try:
        response= requests.post(API_URL,json=payload)

        if response.status_code == 200:
            result = response.json()

            if result["Predicted_Termination"] == 1:
                st.error("Employee is likely to be terminated!")
            else:
                st.success("Employee is likely to remain active!")
        else:
            st.warning("API ERROR !!")
    except requests.expectaions.RequestException:
        st.error("Could not connect API ")

