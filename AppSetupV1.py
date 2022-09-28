# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:22:07 2022

@author: lpnnr
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Team 10")
st.header("Data keuze ")
st.write("Lorem Ipsum")

st.header("Data verkenning")
st.write("Lorem Ipsum")


"Imort dataframe"

dftest = pd.read_csv("TestdataStreamlit.csv")


# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )



















options = st.multiselect("Kies dataset", ["Test1", "test2", "test3"])

if options == "Test1":
    st.write(dftest)

    

    
chart_data = dftest

st.line_chart(chart_data)














st.write(options)

button1 = st.button("Click")

if button1: 
    st.write("Tekst")
    
checkbox1 = st.checkbox("Check test")

button2 = st.button("Submit")

if button2: 
    st.write("like")
    


st.header("Header test")

options = st.multiselect("Kies iets", ["Test1", "test2", "test3"])
      

num = st.slider("Hoeveel", 1,100,10)

if st.button("reset"):
    st.write