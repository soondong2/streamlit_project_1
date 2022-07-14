import streamlit as st
import pandas as pd
import numpy as np
from html_module import section, callout, line_break, title

st.set_page_config(
    page_title="CPI Dataset",
    page_icon="📈",
)
title('About the dataset')

# 데이터 프레임 가져오기
DATA_URL = 'data/KOSIS_소비자물가지수'

# data load function
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# data load & checkbox
check = st.checkbox('Original Dataset')

if check:
  data_load_state = st.text('Loading data...')
  data = load_data(1000)
  data_load_state.text("")
