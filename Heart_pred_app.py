#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import numpy as np
import joblib


# In[6]:


#Connecting trained machine learning model
model = joblib.load('best_heart_disease_model.pkl')

#Predictions Function
def predict_heart_disease(data):
    prediction = model.predict(data)
    return prediction[0]


# In[7]:


#App Name
st.title("Heart Disease Prediction")

# Form for patient details
with st.form(key='patient_form'):
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, step=1)
    cholestrol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, step=1)
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["True", "False"])
    resting_electrocardiographic_results = st.selectbox("Resting Electrocardiographic Results", ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"])
    maximum_heart_rate_achieved = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, step=1)
    exercise_induces_anginga = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    old_peak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=3, step=1)
    status_of_the_heart = st.selectbox("Status of the Heart", ["Normal", "Fixed Defect", "Reversible Defect"])

    submit_button = st.form_submit_button(label='Predict')



# In[8]:


# When the form is submitted
if submit_button:
    if age and resting_blood_pressure and cholestrol and maximum_heart_rate_achieved and old_peak is not None:
       
        #Connect categorical inputs to numerical values
        sex = 1 if sex == "Male" else 0
        chest_pain_type = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index( chest_pain_type)
        fasting_blood_sugar = 1 if fasting_blood_sugar == "True" else 0
        resting_electrocardiographic_results = ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"].index(resting_electrocardiographic_results)
        exercise_induces_anginga = 1 if exercise_induces_anginga == "Yes" else 0
        slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
        status_of_the_heart = ["Normal", "Fixed Defect", "Reversible Defect"].index(status_of_the_heart)
        
        #Prepare data fused for predicting
        data = np.array([[age, sex, chest_pain_type, resting_blood_pressure, cholestrol, fasting_blood_sugar, resting_electrocardiographic_results,  maximum_heart_rate_achieved,exercise_induces_anginga, old_peak, slope, ca, status_of_the_heart]])
        
        #Predict
        prediction = predict_heart_disease(data)
        
        #Show Results
        if prediction == 1:
            st.error("The patient is likely to suffer from heart disease. Further tests or treatment is recommended.")
        else:
            st.success("The patient is unlikely to suffer from heart disease.")
    else:
        st.error("Please fill out all fields.")


# In[11]:




