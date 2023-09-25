import streamlit as st
import pandas as pd
st.markdown("# Racer Page 🎈")
st.sidebar.markdown("#This is Racer Page 🎈")

st.write(' # Mariokart *Stats Website*')

df_racer = pd.read_csv['data/racer_stats.csv']

st.write[df_racer]

