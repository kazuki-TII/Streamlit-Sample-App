import streamlit as st
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

st.set_page_config(page_title="メインページ", page_icon='image/aurora.png')
st.title("Multiple OSS Access Log Analyzer")

usecols = st.multiselect(
    '何番目の列を解析の対象にしますか？',
    [0, 3, 4, 5, 6],
    [0, 3, 4, 5, 6])

if len(usecols) == 0:
    st.error('解析対象の列が指定されていません。')
