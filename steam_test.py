import numpy as np
import streamlit as st
import pandas as pd

DaF = pd.read_csv(r"C:\Users\trach\Desktop\drinks.csv")
checker = st.checkbox("Show me the DF")
if checker:
    st.dataframe(DaF)
    
    