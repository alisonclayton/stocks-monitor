import streamlit as it
import pandas as pd
import investpy as ip
from datetime import datetime, timedelta
import plotly.graph_objs as go

countries = ['brazil', 'united states', 'portugal', 'switzerland']
intervals = ['daily', 'weekly', 'monthly']

start_date = datetime.today().timedelta(days=7)
end_date = datetime.today()

@st.cache
def consulta_acao(stock, country, from_date, to_date, interval):
    df = ip.get_stock_historical_data(stock=stock, country=country, from_date=from_date, to_date=to_date, interval=interval)
    return df

def format_date(dt,format='%d/%m/%Y'):
    return dt.strftime(format)

