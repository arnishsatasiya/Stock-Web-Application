import streamlit as st
import pandas as pd
from PIL import Image
import yfinance as yf

# add title and an image
st.write("""
# Stock Market Web Application
**Visually** show data on a stock! 
""")



# create a sidebar header
st.sidebar.header("User Input")


# create function to get input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-08-04")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol


# load the data from the yfinance
def get_data(symbol, start_, end_):
    company = yf.Ticker(symbol)
    df = company.history(period='1d', start=start_, end=end_)
    return df

# company_website


def get_website(symbol):
    company = yf.Ticker(symbol)
    return company.info['website']


# get the user input
start, end, symbol = get_input()
df = get_data(symbol, start, end)
company_website = get_website(symbol)

# display the close price
st.header(symbol + " Close Price\n")
st.line_chart(df['Close'])

# display the volume
st.header(symbol + " Volume\n")
st.line_chart(df['Volume'])

# get statistics on data
st.header("Data Statistic")
st.write(df.describe())
