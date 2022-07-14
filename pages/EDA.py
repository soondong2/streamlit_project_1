import streamlit as st
import pandas as pd
import numpy as np
from html_module import section, callout, line_break, title

st.set_page_config(
    page_title="소비자 물가지수 EDA",
    page_icon="📈",
)

title('지출 목적별 소비자 물가지수 EDA')

@st.cache
# 전년비 dataframe function
def CPI_df(data, code, region):
    region_total = df_sample1[(df_sample1["품목코드"] == code) & (df_sample1["도시"] == region)]
    region_total = region_total.drop(["품목코드"], axis=1).reset_index(drop=True)
    
    region_total["전년비"] = 0
    
    if region == "세종특별자치시":
        for idx in range(4, region_total.shape[0]):
            curr_CI = region_total.iloc[idx, 3]
            prev_CI = region_total.iloc[idx - 1, 3]
            region_total.iloc[idx, 4] = (curr_CI - prev_CI) / prev_CI * 100
        region_total = region_total.iloc[3:, :]

    else: 
        for idx in range(1, region_total.shape[0]):
            curr_CI = region_total.iloc[idx, 3]
            prev_CI = region_total.iloc[idx - 1, 3]
            region_total.iloc[idx, 4] = (curr_CI - prev_CI) / prev_CI * 100
        
    return region_total

# 대분류 품목별 물가지수 plot function
def CPI_plot(data, code, region):
    df = CPI_df(data, code, region)
    
    if code == "0":
        label = "CI"
    else:
        label = "CPI"
        
    plt.figure(figsize=(15, 8))
    line_plot = plt.plot(df["연도"], df["물가지수"], label=label, marker="o", linewidth=2.5)
    
    x = df["연도"].to_list()
    y = df["물가지수"].tolist()
    
    for i in range(len(x)):
        height = y[i]
        plt.text(x=x[i], y=height + 0.3, s=round(y[i], 2), ha="center", va="bottom", size=15)
    
    plt.title(f"연도별 {region} 소비자물가지수", fontsize=16)
    plt.xticks(fontsize=12)
    plt.xlabel("연도")
    plt.ylabel("소비자물가지수")
    plt.axhline(100.0, 0.02, 0.98, color='red', linestyle='--', linewidth=1.5, label="기준 (단위 : 100)")
    plt.legend(loc="best", frameon=True, fontsize=13)
    plt.show()

# 대분류 품목별 물가지수 select box
option1 = st.selectbox(
     'What are your want category?',
     ('0', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
     )

option2 = st.selectbox(
     'What are your want region?',
     ('전국', '서울특별시', '울산광역시', '인천광역시', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '세종특별자치시', '제주특별자치도', '강원도', '경기도',
     '경상남도', '경상북도', '전라남도', '전라북도')
     )
