import streamlit as st
from data import *

etf_list = load_etf_list()
st.write(etf_list)

histories = list(map(load_history,
                     etf_list.Symbol))
# st.write(histories)

pv_list = list(map(get_pv, histories))
st.write(pv_list)
