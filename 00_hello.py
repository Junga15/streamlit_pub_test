import streamlit as st
import pandas as pd

# 웹 제목 설정
st.title('첫 번째 streamlit 앱')

# 텍스트 출력
st.write('안녕하세요! Streamlit입니다.')

# 아나콘다 프롬프트에서 
# 경로 여기까지 온 뒤: c:/sesac/03_시각화/my_streamlit/00_hello.py
# streamlit run 00_hello.py
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 22]} 
df = pd.DataFrame(data)
# 데이터프레임 출력
st.dataframe(df)
# 막대 그래프 생성
st.bar_chart(df['age'])
# 끝낼때는 ctrl c (ctrl z가 아님)

# https://docs.streamlit.io/develop/api-reference 스트림릿 문서 참고하기
