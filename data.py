import FinanceDataReader as fdr
import streamlit as st

@st.cache
def load_etf_list():
    return fdr.StockListing("ETF/KR")