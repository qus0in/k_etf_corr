import FinanceDataReader as fdr
import streamlit as st

@st.cache
def load_etf_list():
    return fdr.StockListing("ETF/KR")[:400]

@st.cache
def load_history(ticker):
    return fdr.DataReader(ticker)