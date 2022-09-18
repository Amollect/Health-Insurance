# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:57:29 2022

@author: Amol
"""

import streamlit as st
import joblib

def main():
    html_temp="""
    <div style="background-color:lightblue,padding:16px">
    <h2 style="color:black",text-align:center>HEALTH INSURANCE COST PREDICTION<h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
     # load the model
    model = joblib.load('model_joblib_gr')
    
    p1=st.slider("Enter your Age",18,100)
    
    s1=st.selectbox('Sex',('male','Female'))
    if s1=='male':
        p2=1
    else:
        p2=0
    
    p3 =st.number_input("Enter Your BMI Value")
    p4 = st.slider("Enter Number of Children",0,4) 
    
    s2=st.selectbox("Smoker",("Yes","No"))
    if s2=="Yes":
        p5=1
    else:
        p5=0
        
    p6 = st.slider("Enter Your Region [1-4]",1,4)
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
        st.heart()
        st.success('Insurance Amount is {} '.format(round(prediction[0],2)))    
    
if __name__=='__main__':
    main()
