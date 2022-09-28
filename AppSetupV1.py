# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:22:07 2022

@author: lpnnr
"""

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st

from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import plotly.io as pio

df_stock = yf.Ticker('TSLA').history(period = 'max', interval = '1d')


st.title("Streamlit Team 10")
st.header("Data keuze ")
st.write("Lorem Ipsum")

st.header("Data verkenning")
st.write("Lorem Ipsum")


"Imort dataframe"

#dftest = pd.read_csv("TestdataStreamlit.csv")


















options = st.multiselect("Kies dataset", ["Test1", "test2", "test3"])

if options == "Test1":
    st.write(df_stock)

    

    
chart_data = df_stock

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