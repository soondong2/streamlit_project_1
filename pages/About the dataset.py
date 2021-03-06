import streamlit as st
import pandas as pd
import numpy as np
from html_module import section, callout, line_break, title

st.set_page_config(
    page_title="CPI Dataset",
    page_icon="π",
)
title('About the dataset')

# λ°μ΄ν° νλ μ κ°μ Έμ€κΈ°
DATA_URL1 = 'data/KOSIS_μλΉμλ¬Όκ°μ§μ.csv'

# data load function
@st.cache
def load_data(DATA_URL, nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# data load & checkbox1
section("Original Dataset", 250)
check_data1 = st.checkbox('Show Original Dataset')

if check_data1:
    callout(['KOSIS μ§μΆ λͺ©μ λ³ μλΉμ λ¬Όκ°μ§μ μλ³Έ λ°μ΄ν°μμλλ€.'])
    data_load_state = st.text('Loading data...')
    data = load_data(DATA_URL1, 1000)
    data_load_state.text("")
    st.dataframe(data)

line_break()

# data load & checkbox2
section("Clearning Dataset", 250)
check_data2 = st.checkbox('Show Clearning Dataset2')

DATA_URL2 = 'data/df.csv'

if check_data2:
    callout(['λΆμμ μ¬μ©νκΈ° μν΄ μ μ²λ¦¬νμ¬ κ°κ³΅ν λ°μ΄ν°μμλλ€.'])
    data_load_state = st.text('Loading data...')
    data = load_data(DATA_URL2, 1000)
    st.dataframe(data)
    data_load_state.text("")
    
line_break()
