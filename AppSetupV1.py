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




df_stock = yf.Ticker('TSLA').history(period = 'max', interval = '1d')
    
# Met dank aan: https://gist.github.com/mabarm/48af996f43e8b46aa806ebbaed90dcd5




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


# ____________________________________________________________________________________________________________



url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/gross-profit"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")

tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index=index
tesla_gross_profit = pd.DataFrame(columns=["Date","Gross_profit"])

for row in tables[table_index].tbody.find_all('tr'):
    col=row.find_all("td")
    if(col!=[]):
        date=col[0].text
        gross_profit=col[1].text.strip().replace("$","").replace(",","")
        tesla_gross_profit=tesla_gross_profit.append({"Date":date,"Gross_profit":gross_profit}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace=True)
not_empty=tesla_gross_profit["Gross_profit"]!=""
tesla_revenue=tesla_revenue[not_empty]



# ____________________________________________________________________________________________________________





url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/operating-income"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")

tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index=index
tesla_operating_income = pd.DataFrame(columns=["Date","Operating_income"])

for row in tables[table_index].tbody.find_all('tr'):
    col=row.find_all("td")
    if(col!=[]):
        date=col[0].text
        operating_income=col[1].text.strip().replace("$","").replace(",","")
        tesla_operating_income=tesla_operating_income.append({"Date":date,"Operating_income":operating_income}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace=True)
not_empty=tesla_operating_income["Operating_income"]!=""
tesla_revenue=tesla_revenue[not_empty]


# ____________________________________________________________________________________________________________




url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/ebitda"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")

tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index=index
tesla_ebitda = pd.DataFrame(columns=["Date","ebitda"])

for row in tables[table_index].tbody.find_all('tr'):
    col=row.find_all("td")
    if(col!=[]):
        date=col[0].text
        ebitda=col[1].text.strip().replace("$","").replace(",","")
        tesla_ebitda=tesla_ebitda.append({"Date":date,"ebitda":ebitda}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace=True)
not_empty=tesla_ebitda["ebitda"]!=""
tesla_revenue=tesla_revenue[not_empty]



# ____________________________________________________________________________________________________________




url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/net-income"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")

tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index=index
tesla_net_income = pd.DataFrame(columns=["Date","net_income"])

for row in tables[table_index].tbody.find_all('tr'):
    col=row.find_all("td")
    if(col!=[]):
        date=col[0].text
        net_income=col[1].text.strip().replace("$","").replace(",","")
        tesla_net_income=tesla_net_income.append({"Date":date,"net_income":net_income}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace=True)
not_empty=tesla_net_income["net_income"]!=""
tesla_revenue=tesla_revenue[not_empty]



# ____________________________________________________________________________________________________________



url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/eps-earnings-per-share-diluted"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")

tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index=index
tesla_eps = pd.DataFrame(columns=["Date","eps"])

for row in tables[table_index].tbody.find_all('tr'):
    col=row.find_all("td")
    if(col!=[]):
        date=col[0].text
        eps=col[1].text.strip().replace("$","").replace(",","")
        tesla_eps=tesla_eps.append({"Date":date,"eps":eps}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace=True)
not_empty=tesla_eps["eps"]!=""
tesla_revenue=tesla_revenue[not_empty]



# # ____________________________________________________________________________________________________________



url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/shares-outstanding"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")

tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index=index
tesla_shares_outstanding = pd.DataFrame(columns=["Date","shares_outstanding"])

for row in tables[table_index].tbody.find_all('tr'):
    col=row.find_all("td")
    if(col!=[]):
        date=col[0].text
        shares_outstanding=col[1].text.strip().replace("$","").replace(",","")
        tesla_shares_outstanding=tesla_shares_outstanding.append({"Date":date,"shares_outstanding":shares_outstanding}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace=True)
not_empty=tesla_shares_outstanding["shares_outstanding"]!=""
tesla_revenue=tesla_revenue[not_empty]



# ____________________________________________________________________________________________________________


df_combinatie = tesla_revenue
loep = [tesla_gross_profit,tesla_operating_income,tesla_ebitda,tesla_net_income,tesla_eps,tesla_shares_outstanding]
for naam in loep:
    df_combinatie = df_combinatie.merge(naam, on = 'Date')



#____________________________________________________________________________________________________________

# fig = go.Figure()

# fig.add_trace(go.Scatter(x=tesla_gross_profit['Date'],y=tesla_gross_profit['Gross_profit'],mode='markers'))

# fig.show()

#____________________________________________________________________________________________________________
# Data verkenning
# stock data
print(df_stock.head())
print(df_stock.info())

# jaar kolomn maken
# df_stock: Date to date_time
df_stock_index = df_stock.reset_index()
df_stock["Date"] = pd.to_datetime(df_stock_index["Date"], infer_datetime_format=True)
print(df_stock_index.info())
df_stock_index["Year"] = pd.to_datetime(df_stock_index["Date"]).dt.year
df_stock_index["Month"] = pd.to_datetime(df_stock_index["Date"]).dt.month
df_stock_index["Day"] = pd.to_datetime(df_stock_index["Date"]).dt.day
print(df_stock_index.info())

print(df_combinatie.head())
print(df_combinatie.info())
#df_combinatie: date to date_time
df_combinatie_index = df_combinatie.reset_index()
df_combinatie_index["Date"] = pd.to_datetime(df_combinatie_index["Date"], infer_datetime_format=True)
df_combinatie_index["Year"] = pd.to_datetime(df_combinatie_index["Date"]).dt.year
df_combinatie_index["Month"] = pd.to_datetime(df_combinatie_index["Date"]).dt.month
df_combinatie_index["Day"] = pd.to_datetime(df_combinatie_index["Date"]).dt.day
# object naar int of float
df_combinatie_index["eps"] = df_combinatie_index["eps"].astype(float)
df_combinatie_index["Revenue"] = df_combinatie_index["Revenue"].astype(int)
df_combinatie_index["Gross_profit"] = df_combinatie_index["Gross_profit"].astype(int)
df_combinatie_index["Operating_income"] = df_combinatie_index["Operating_income"].astype(int)
df_combinatie_index["ebitda"] = df_combinatie_index["ebitda"].astype(int)
df_combinatie_index["net_income"] = df_combinatie_index["net_income"].astype(int)
df_combinatie_index["shares_outstanding"] = df_combinatie_index["shares_outstanding"].astype(int)
print(df_combinatie_index.info())
df_combinatie_index = df_combinatie_index.sort_values("Date")
print(df_combinatie_index.head())

# df_stock: bar plot over volume per jaar
# fig = go.Figure()
# fig.add_trace(go.Bar(x = df_stock_index["Year"], y = df_stock_index["Volume"]))
# fig.update_layout(title = "Volume of stocks per year", 
#                   xaxis_title = "Years", 
#                   yaxis_title = "Volume (Billion)" )
# plot(fig)

#____________________________________________________________________________________________________________

# maken van een dataframe met dezelfde kwartaal datums
df_berekeningen = df_combinatie_index.merge(df_stock_index, on = "Date", how = "inner")
df_berekeningen = df_berekeningen.drop(["Dividends", "Year_y",  "Month_y", "Day_y"], axis = 1)
print(df_berekeningen.columns)
# P/E ratio = price to earnings berekening
df_berekeningen["P/E_Open"] = df_stock_index["Open"]/df_combinatie_index["eps"]
df_berekeningen["P/E_High"] = df_stock_index["High"]/df_combinatie_index["eps"]
df_berekeningen["P/E_Low"] = df_stock_index["Low"]/df_combinatie_index["eps"]
df_berekeningen["P/E_Close"] = df_stock_index["Close"]/df_combinatie_index["eps"]

#____________________________________________________________________________________________________________

# streamlit visualisaties link met info: https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart


#__________________________________________________________________________
"""

Streamlit opzet V1


"""



st.title("Streamlit Team 10")
st.header("Data keuze ")
st.write("Lorem Ipsum")

st.header("Data verkenning")
st.write("Lorem Ipsum")


"Imort dataframe"


options = st.multiselect("Kies dataset", ["Test1", "test2", "test3"])

st.write(options)
    
checkbox1 = st.checkbox("Check test")

button2 = st.button("Submit")

if button2: 
    st.write("like")
    


st.header("Header test")

options = st.multiselect("Kies iets", ["Test1", "test2", "test3"])
      

num = st.slider("Hoeveel", 1,100,10)

if st.button("reset"):
    st.write


st.write(df_stock_index)

st.linegraph(df_stock)




