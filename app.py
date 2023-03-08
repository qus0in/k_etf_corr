import streamlit as st
from data import *

etf_list = load_etf_list()
# st.write(etf_list)

histories = map(etf_list.Symbol, load_history)
st.write(histories)

# df = load_history(etf_list.iloc[0, 0])
# pv = get_pv(df)
# st.write(pv)
