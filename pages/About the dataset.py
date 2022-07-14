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
DATA_URL = 'data/KOSIS_소비자물가지수.csv'

# data load function
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# data load & checkbox
section("Original Dataset", 250)
check_data = st.checkbox('KOSIS Dataset')

if check_data:
    callout(['KOSIS 지출 목적별 소비자 물가지수 원본 데이터셋입니다.'])
    data_load_state = st.text('Loading data...')
    data = load_data(1000)
    data_load_state.text("")
    st.dataframe(load_data(1000))

    
