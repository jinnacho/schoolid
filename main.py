import streamlit as st
import pandas as pd

st.title("🎓 학번으로 구글 계정 확인하기")

# CSV 파일 불러오기 (같은 폴더에 있어야 함)
try:
    df = pd.read_csv("emails.csv", encoding='cp949')  # 또는 'cp949', 'euc-kr'
except FileNotFoundError:
    st.error("⚠️ emails.csv 파일이 존재하지 않습니다. 파일을 같은 폴더에 넣어주세요.")
except UnicodeDecodeError:
    st.error("⚠️ 파일 인코딩 오류입니다. 'utf-8' 대신 'cp949' 또는 'euc-kr'을 시도해보세요.")
else:
    hakbun = st.text_input("학번을 입력하세요")

    if hakbun:
        result = df[df["학번"].astype(str) == hakbun]

        if not result.empty:
            email = result.iloc[0]["이메일"]
            st.success(f"📧 이메일 주소: **{email}**")
        else:
            st.warning("해당 학번을 찾을 수 없습니다. 다시 확인해주세요.")
