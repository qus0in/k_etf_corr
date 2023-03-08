import FinanceDataReader as fdr
import streamlit as st

@st.cache_data
def load_etf_list():
    return fdr.StockListing("ETF/KR")[:400]


@st.cache_data
def load_history(ticker):
    return fdr.DataReader(ticker)

def get_pv(df):
    v = df.iloc[-1].tail(20)
    return (v.Close * v.Volume).mean()