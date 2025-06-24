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

help_txt = '''
    以下のフォーマット文字列を解析可能です。詳細については、[公式ページ](https://httpd.apache.org/docs/2.4/ja/mod/mod_log_config.html)を参照して下さい。

    | 列名 | フォーマット文字列 | 説明 | 
    |:-----|:-----:|:-----|
    | Remote Host | `%h` | リモートホスト |
    | Time | `%t` | リクエストを受付けた時刻 | 
    | Request | `\"%r\"` | リクエストの最初の行 | 
    | Status | `%>s` | ステータス | 
    | Size | `%b` | レスポンスのバイト数 | 
    | User Agent | `\"%{User-agent}i\"` | リクエストのUser-agentヘッダの内容 | 
    | Response Time | `%D` または `%T` | リクエストを処理するのにかかった時間 |         
    '''

names = st.multiselect(
    'これらの列を何を意味しますか？',
    ['Remote Host', 'Time', 'Request', 'Status', 'Size', 'User Agent', 'Response Time'],
    help=help_txt,
    label_visibility="visible",
)
