import streamlit as st
from data import *

etf_list = load_etf_list()
# st.write(etf_list)

histories = list(map(load_history,
                     etf_list.Symbol))
st.write(histories)

# df = load_history(etf_list.iloc[0, 0])
# pv = get_pv(df)
# st.write(pv)
