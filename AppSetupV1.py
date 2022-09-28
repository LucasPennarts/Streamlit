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


url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")

tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index=index
tesla_revenue = pd.DataFrame(columns=["Date","Revenue"])

for row in tables[table_index].tbody.find_all('tr'):
    col=row.find_all("td")
    if(col!=[]):
        date=col[0].text
        revenue=col[1].text.strip().replace("$","").replace(",","")
        tesla_revenue=tesla_revenue.append({"Date":date,"Revenue":revenue}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace=True)
not_empty=tesla_revenue["Revenue"]!=""
tesla_revenue=tesla_revenue[not_empty]


st.title("Streamlit Team 10")
st.header("Data keuze ")
st.write("Lorem Ipsum")

st.header("Data verkenning")
st.write("Lorem Ipsum")


"Imort dataframe"

#dftest = pd.read_csv("TestdataStreamlit.csv")


















options = st.multiselect("Kies dataset", ["Test1", "test2", "test3"])

if options == "Test1":
    st.write(tesla_revenue)

    

    
chart_data = tesla_revenue

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
