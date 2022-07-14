import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# 전체 페이지 설정
st.set_page_config(
    page_title="KOSIS 소비자 물가지수",
    page_icon="📈",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.balloons()  # 풍선 효과
title('보험료 데이터 회귀 분석')

section('Summary')
image = Image.open('images/Untitled.png')
st.image(image,)
callout([
  '안녕하세요! 멋쟁이 사자처럼 AI SCHOOL 6기를 활동하면서 진행한 팀 프로젝트입니다.',
  'KOSIS의 연도별 지출목적별 소비자물가지수 데이터를 사용하여 2021년도를 기준으로 이전 10년 동안의 소비자물가지수를 EDA 하였습니다. 데이터를 통해 연도별, 지역별, 품목별로 물가 동향이 어떤 특징을 보이는지, 특이 패턴 및 차이점이 보인다면 그 이유가 무엇일지를 유추합니다. 또한 코로나 발생 시점 이전과 이후에 물가수준에 차이를 보이는지 분석합니다. '
])
line_break()
