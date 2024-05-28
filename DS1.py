import streamlit as st
import pickle
import numpy as np

model=pickle.load(open('saved_model.sav','rb'))
st.title("Welcome to Iris Prediction")
sepal_length=st.number_input("Sepal Length")
sepal_width=st.number_input("Sepal Width")
petal_length=st.number_input("Petal Length")
petal_width=st.number_input("Petal Width")
btn=st.button("Predict")
if btn:
    pred=model.predict([[sepal_length,sepal_width,petal_length,sepal_width]])[0]
    print(pred)

    st.subheader(pred)