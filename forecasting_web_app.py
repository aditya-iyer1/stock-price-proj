# Forecasting Web App Done w/ (https://www.youtube.com/watch?v=0E_31WqVzCY)


import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet # MOD (FBProphet depracated, use prophet instead)
from prophet.plot import plot_plotly
from plotly import graph_objs as go # Library for interactive graphs
import plotly.express as px


START = "2018-01-01" # Start date
TODAY = date.today().strftime("%Y-%m-%d") # Get current data in Ymd format as a string

st.title("Stock Prediction App") #Title of web app

stocks = ("AAPL","TSLA","SHOP", "GOOG")  # Choices for stocks we can use as stock name (Code) from yfinance
selected_stock = st.selectbox("Select dataset for prediction", stocks) # Creates dropdown to select data set for prediction from `stocks`

n_years = st.slider("Years of prediction:", 1, 4) # Slider for number of years for prediction
period = n_years * 365 # In days


#Each st command adds a widget/feature to the web app and assigns the value to the variable

#To run script in the web app, run `streamlit run app.py` in terminal

#Run `ctrl+C` in terminal to quit app

# Note - cannot use block comments with streamlit

@st.cache_data # Streamlit cache function, caches data from a selected stock and saves it so we don't need to rerun/reload the code from load_data
def load_data(ticker): # Load stock data using ticket as input
	data = yf.download(ticker, START, TODAY) # Returns data from START until TODAY in a pandas df
	data.reset_index(inplace = True) # Puts date in the first column

	return data

data_load_state = st.text("Load data ...") # Streamlit text display
data = load_data(selected_stock)
data_load_state.text("Loading data ... done!") # Changes text display once select stock data is loaded to this



st.subheader("Raw Data")
st.write(data.tail()) #Already a pandas df, easy for streamlit to handle

def plot_raw_data():
	fig = px.line(data, x = data['Date'], y = data['Close'])
	st.plotly_chart(fig)
	
plot_raw_data()



