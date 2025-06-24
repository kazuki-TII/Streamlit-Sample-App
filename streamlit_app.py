import streamlit as st
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

st.set_page_config(page_title="メインページ", page_icon='image/aurora.png')
st.title("Multiple OSS Access Log Analyzer")
