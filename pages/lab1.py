import streamlit as st
import pandas as pd

st.title("lab1")
url = "https://github.com/myoh0623/dataset/blob/main/student-mat.csv"
df = pd.read_csv(url)

# 성별 평균 성적 비교(G3 컬럼은 성적을 나타낸다)
st.subheader("1. 성별에 따른 평균 최종 성적 (G3 컬럼)")
gender_score = df.groupby("sex")["G3"].mean()

st.bar_chart(gender_score)
