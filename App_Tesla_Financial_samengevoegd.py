import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Studenten: Lucas, Yonni, Thomas en Merel
# ____________________________________________________________________________________________________________

df_stock = yf.Ticker('TSLA').history(period = 'max', interval = '1d')
    
# Met dank aan: https://gist.github.com/mabarm/48af996f43e8b46aa806ebbaed90dcd5

# ____________________________________________________________________________________________________________

url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")
tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index = index
tesla_revenue = pd.DataFrame(columns=["Date","Revenue"])

for row in tables[table_index].tbody.find_all('tr'):
    col = row.find_all("td")
    if(col!= []):
        date = col[0].text
        revenue = col[1].text.strip().replace("$","").replace(",","")
        tesla_revenue = tesla_revenue.append({"Date":date,"Revenue":revenue}, ignore_index=True)

tesla_revenue.dropna(inplace = True)
not_empty=tesla_revenue["Revenue"]!=""
tesla_revenue=tesla_revenue[not_empty]

# ____________________________________________________________________________________________________________

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/gross-profit"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")
tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index = index
tesla_gross_profit = pd.DataFrame(columns=["Date","Gross_profit"])

for row in tables[table_index].tbody.find_all('tr'):
    col=  row.find_all("td")
    if(col!= []):
        date = col[0].text
        gross_profit = col[1].text.strip().replace("$","").replace(",","")
        tesla_gross_profit = tesla_gross_profit.append({"Date":date,"Gross_profit":gross_profit}, ignore_index = True)
tesla_revenue.head()

tesla_revenue.dropna(inplace = True)
not_empty = tesla_gross_profit["Gross_profit"]!=""
tesla_revenue = tesla_revenue[not_empty]

# ____________________________________________________________________________________________________________

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/operating-income"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")
tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index = index
tesla_operating_income = pd.DataFrame(columns=["Date","Operating_income"])

for row in tables[table_index].tbody.find_all('tr'):
    col = row.find_all("td")
    if(col!= []):
        date = col[0].text
        operating_income = col[1].text.strip().replace("$","").replace(",","")
        tesla_operating_income = tesla_operating_income.append({"Date":date,"Operating_income":operating_income}, ignore_index = True)
tesla_revenue.head()

tesla_revenue.dropna(inplace = True)
not_empty=tesla_operating_income["Operating_income"]!=""
tesla_revenue = tesla_revenue[not_empty]


# ____________________________________________________________________________________________________________

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/ebitda"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")
tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index = index
tesla_ebitda = pd.DataFrame(columns=["Date","ebitda"])

for row in tables[table_index].tbody.find_all('tr'):
    col = row.find_all("td")
    if(col!= []):
        date = col[0].text
        ebitda = col[1].text.strip().replace("$","").replace(",","")
        tesla_ebitda = tesla_ebitda.append({"Date":date,"ebitda":ebitda}, ignore_index = True)
tesla_revenue.head()

tesla_revenue.dropna(inplace = True)
not_empty = tesla_ebitda["ebitda"]!=""
tesla_revenue = tesla_revenue[not_empty]

# ____________________________________________________________________________________________________________

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/net-income"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")
tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index = index
tesla_net_income = pd.DataFrame(columns=["Date","net_income"])

for row in tables[table_index].tbody.find_all('tr'):
    col = row.find_all("td")
    if(col!= []):
        date = col[0].text
        net_income = col[1].text.strip().replace("$","").replace(",","")
        tesla_net_income = tesla_net_income.append({"Date":date,"net_income":net_income}, ignore_index = True)
tesla_revenue.head()

tesla_revenue.dropna(inplace = True)
not_empty = tesla_net_income["net_income"]!=""
tesla_revenue = tesla_revenue[not_empty]

# ____________________________________________________________________________________________________________

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/eps-earnings-per-share-diluted"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")
tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index = index
tesla_eps = pd.DataFrame(columns=["Date","eps"])

for row in tables[table_index].tbody.find_all('tr'):
    col = row.find_all("td")
    if(col!= []):
        date = col[0].text
        eps = col[1].text.strip().replace("$","").replace(",","")
        tesla_eps = tesla_eps.append({"Date":date,"eps":eps}, ignore_index = True)
tesla_revenue.head()

tesla_revenue.dropna(inplace = True)
not_empty = tesla_eps["eps"]!=""
tesla_revenue = tesla_revenue[not_empty]

# ____________________________________________________________________________________________________________

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/shares-outstanding"
html_data = requests.get(url).text

beautiful_soup = BeautifulSoup(html_data,"html.parser")
tables = beautiful_soup.find_all("table")

for index,table in enumerate(tables):
    if("Tesla Quarterly Revenue" in str(table)):
        table_index = index
tesla_shares_outstanding = pd.DataFrame(columns=["Date","shares_outstanding"])

for row in tables[table_index].tbody.find_all('tr'):
    col = row.find_all("td")
    if(col!= []):
        date = col[0].text
        shares_outstanding = col[1].text.strip().replace("$","").replace(",","")
        tesla_shares_outstanding = tesla_shares_outstanding.append({"Date":date,"shares_outstanding":shares_outstanding}, ignore_index=True)
tesla_revenue.head()

tesla_revenue.dropna(inplace = True)
not_empty = tesla_shares_outstanding["shares_outstanding"]!=""
tesla_revenue = tesla_revenue[not_empty]

# ____________________________________________________________________________________________________________

df_combinatie = tesla_revenue

loep = [tesla_gross_profit, tesla_operating_income, tesla_ebitda, tesla_net_income, tesla_eps,tesla_shares_outstanding]

for naam in loep:
    df_combinatie = df_combinatie.merge(naam, on = 'Date')
    
#____________________________________________________________________________________________________________

st.title("Streamlit Team 10 Tesla")
st.header("Data keuze ")
st.write("De gebruikte data komt voort uit het ondezoeken van stock data van Tesla en de vele mogelijkheden om deze data te gebruiken en visualiseren.\n")



st.header("Data verkenning")
st.write("De data die verkent wordt is de stockdata van Tesla en de waarde van het bedrijf.")
st.write("Om met de datum van het aandelen dataframe te werken moet eerst de index gereset worden. Daarna kan de datum worden omgezet naar een date time functie.")
         
#____________________________________________________________________________________________________________

st.header("Aandeelkoers Tesla")
st.write("De aandelen van Tesla kunnen weergegeven worden doormiddel van plotly's functie Candlestick.")
st.write("De checkbox zorgt ervoor dat de grafiek wel of niet zichtbaar is.")
df_stoc = df_stock.reset_index()
showgraph = st.checkbox('Aandeelwaarde candlestick')

if showgraph:
    showslider = st.checkbox('Showslider')    
    fig = go.Figure()
    
    fig.add_trace(go.Candlestick(x=df_stoc['Date'],open = df_stoc['Open'],high = df_stoc['High'],low = df_stoc['Low'],close = df_stoc['Close']))
    
    date_buttons = [
    {'label': 'Totaal', 'step': "all"},
    {'count': 10, 'label': '9 jaar', 'step': "year", 'stepmode': "backward"},
    {'count': 3, 'label': '3 jaar', 'step': "year", 'stepmode': "backward"},
    {'count': 15, 'label': '15 maanden', 'step': "month", 'stepmode': "backward"}]   
    
    fig.update_layout(    
          {'xaxis':
        {'rangeselector': {'buttons': date_buttons,'bgcolor':'#1f2202'}}},xaxis_rangeslider_visible=showslider,
              xaxis_title="Tijd",
              yaxis_title="US dollar",
              title="Candlestick Tesla aandelwaarde")
    
    
    st.plotly_chart(fig, use_container_width=True)

#____________________________________________________________________________________________________________

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

#___________________________________________________________________________________________________________

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

st.header("Aandeelkoers")
st.write("Door op de legenda keuren te klikken, kunnen de lijnen in de grafiek aangepast worden. Dit is een functie die plotly zelf bezit.")
st.write("Als je meerdere lossen kolomen wilt laten zien in een grafiek kan hiervoor de .add_trace() functie gebruikt worden van plotly.graph_objects.")

#streamlit visualisaties link met info: https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart
fig2 = go.Figure()
fig2.add_trace(go.Scatter( x = df_stock_index["Date"], y = df_stock_index["Open"], name = "Open"))
fig2.add_trace(go.Scatter( x = df_stock_index["Date"], y = df_stock_index["High"], name = "High"))
fig2.add_trace(go.Scatter( x = df_stock_index["Date"], y = df_stock_index["Low"], name = "Low"))
fig2.add_trace(go.Scatter( x = df_stock_index["Date"], y = df_stock_index["Close"], name = "Close"))

fig2.update_yaxes(title_text="Prijs per Aandeel ($)")
fig2.update_xaxes(title_text="Jaar")
fig2.update_layout(xaxis=dict(autorange=True, range=["2010-06-30", "2022-06-30"],
                             rangeslider= dict(autorange=True, range=["2010-06-30", "2022-06-30"], visible=True), 
                             type="date"))


st.plotly_chart(fig2, use_container_width=True)


#____________________________________________________________________________________________________________

st.header("Histogram PE ratio van openingskoers ")
st.write("Om de P/E ratio te berekenen moet je de aandeelwaarde delen door de eps. Dit kan in een grafiek worden weergegeven met plotly.express.")

# histogram met sliders
fig = px.histogram(df_berekeningen, x = "P/E_Open", color = "Year_x")


sliders = [
    {"steps": [
         {"method": "update", "label": "2010", 
          "args": [{"visible": [True, False, False, False, False, False, False, False, False, False, False, False, False]}]},
         {"method": "update", "label": "2011", 
          "args": [{"visible": [False, True, False, False, False, False, False, False, False, False, False, False, False]}]},
         {"method": "update", "label": "2012", 
          "args": [{"visible": [False, False, True, False, False, False, False, False, False, False, False, False, False]}]},
         {"method": "update", "label": "2013", 
          "args": [{"visible": [False, False, False, True, False, False, False, False, False, False, False, False, False]}]},
         {"method": "update", "label": "2014", 
          "args": [{"visible": [False, False, False, False, True, False, False, False, False, False, False, False, False]}]},
         {"method": "update", "label": "2015", 
          "args": [{"visible": [False, False, False, False, False, True, False, False, False, False, False, False, False]}]},
         {"method": "update", "label": "2016", 
          "args": [{"visible": [False, False, False, False, False, False, True, False, False, False, False, False, False]}]},
         {"method": "update", "label": "2017", 
          "args": [{"visible": [False, False, False, False, False, False, False, True, False, False, False, False, False]}]},
         {"method": "update", "label": "2018", 
          "args": [{"visible": [False, False, False, False, False, False, False, False, True, False, False, False, False]}]},
         {"method": "update", "label": "2019", 
          "args": [{"visible": [False, False, False, False, False, False, False, False, False, True, False, False, False]}]},
         {"method": "update", "label": "2020", 
          "args": [{"visible": [False, False, False, False, False, False, False, False, False, False, True, False, False]}]},
         {"method": "update", "label": "2021", 
          "args": [{"visible": [False, False, False, False, False, False, False, False, False, False, False, True, False]}]},
         {"method": "update", "label": "2022", 
          "args": [{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, True]}]}
     ]}
 ]
fig.update_yaxes(title_text="Aantal")
fig.update_xaxes(title_text="P/E ratio")
fig.update_layout({"bargap":0.2, "sliders": sliders})
st.plotly_chart(fig, use_container_width=True)

#____________________________________________________________________________________________________________

st.header("Dataset filter")
st.write("Hier kan je selecteren in welke kolomen van welke dataset je wilt bekijken.")
datasetlijst = ["Data_stock", "Data_berekening"]

dataframeselect = st.selectbox('Welke set wil je zien', datasetlijst, key='dataframe select')

if (dataframeselect == datasetlijst[0]) & (dataframeselect != ""):
		display_data = df_stock_index
else:
		display_data = df_berekeningen

datakolom = display_data.keys().drop("Date")
datakolom = st.multiselect('Welke set wil je zien', datakolom,default=["High", "Low"], key='kolom select')

displayKolom = display_data[datakolom]

result = pd.concat([display_data["Date"], displayKolom], axis=1)

st.dataframe(result)


st.header("Uitprobeersel")


fig2 = go.Figure()
fig2.add_trace(go.Scatter( x = df_stock_index["Date"], y = df_stock_index["Open"], name = "Open"))


fig2.update_layout(xaxis=dict(autorange=True, range=["2010-06-30", "2022-06-30"],
                             rangeslider= dict(autorange=True, range=["2010-06-30", "2022-06-30"], visible=True), 
                             type="date"))


st.plotly_chart(fig2, use_container_width=True)






#____________________________________________________________________________________________________________
