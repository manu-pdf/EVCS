import numpy as np
import streamlit as st
import pandas as pd

DaF = pd.read_csv(r"https://raw.githubusercontent.com/manu-pdf/EVCS/main/drinks.csv")
checker = st.checkbox("Show me the DF")
if checker:
    st.dataframe(DaF)
    
    
