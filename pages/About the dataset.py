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
DATA_URL1 = 'data/KOSIS_소비자물가지수.csv'

# data load function
@st.cache
def load_data(DATA_URL, nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# data load & checkbox1
section("Original Dataset", 250)
check_data1 = st.checkbox('KOSIS Dataset')

if check_data1:
    callout(['KOSIS 지출 목적별 소비자 물가지수 원본 데이터셋입니다.'])
    data_load_state = st.text('Loading data...')
    data = load_data(DATA_URL1, 1000)
    data_load_state.text("")
    st.dataframe(data)

line_break()

# data load & checkbox2
section("Clearning Dataset", 250)
check_data2 = st.checkbox('Clearning Dataset')

DATA_URL2 = 'data/df.csv'

if check_data2:
    callout(['분석에 사용하기 위해 전처리하여 가공한 데이터셋입니다.'])
    data_load_state = st.text('Loading data...')
    data = load_data(DATA_URL2, 1000)
    st.dataframe(data)
    data_load_state.text("")
    
line_break()
