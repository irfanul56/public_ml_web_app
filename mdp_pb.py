# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 16:31:40 2022

@author: lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model=pickle.load(open('heart_disease.sav','rb'))
parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))


# sidebar to navigate

with st.sidebar:
    selected=option_menu('Multiple disease prediction system',
                         
                         ['Diabetes prediction',
                          'Heart disease prediction',
                          'Parkinsons prediction'],
                         
                         icons=['activity','heart','person'],
                         
                         default_index=0)
    
# Diabetes prediction page

if (selected=='Diabetes prediction'):
    st.title('Diabetes prediction using ML')
    
    # columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('Blood pressure value')
    with col1:
        SkinThickness=st.text_input('Skin thickness value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes predigree function value')
    with col2:
        Age=st.text_input('Age of the person')
    
    
    
    # code for prediction
    diab_diagnosis=''
    
    # create a button for prediction
    if st.button('Diabetes test result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis='The person is diabetic'
        
        else:
            diab_diagnosis='The person is not diabetic'
            
    st.success(diab_diagnosis)
    
    
if (selected=='Heart disease prediction'):
    st.title('Heart disease prediction using ML')
    
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        age=st.text_input('Age of the person')
    with col2:
        sex=st.text_input('sex of the person')
    with col3:
        cp=st.text_input('chest pain type')
    with col4:
        trestbps=st.text_input('resting blood pressure')
    with col5:
        chol=st.text_input('serum cholesterol in mg/dl')
    with col1:
        fbs=st.text_input('fasting blood sugar > 120 mg/dl')
    with col2:
        restecg=st.text_input('resting electrocardiographic results')
    with col3:
        thalach=st.text_input('maximum heart rate achieved')
    with col4:
        exang=st.text_input('exercise induced angina')
    with col5:
        oldpeak=st.text_input('oldpeak = ST depression induced by exercise relative to rest')
    with col1:
        slope=st.text_input('the slope of the peak exercise ST segment')
    with col2:
        ca=st.text_input('number of major vessels (0-3) colored by flourosopy')
    with col3:
        thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable ')


    heart_disease_diagnosis=''
    
    if st.button('Heart disease result'):
        heart_disease_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_disease_prediction[0]==1):
            diagnosis='The person has heart disease'
        
        else:
            diagnosis='The person doesnt have any heart disease'
    
    st.success(heart_disease_diagnosis)
            
if (selected=='Parkinsons prediction'):
    st.title('Parkinsons prediction using ML')
    