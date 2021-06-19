import streamlit as st
# import pandas as pd
# from PIL import Image
import time

# ターミナル
# cd /Users/honda/Documents/python/streamlit
# streamlit run main.py

st.title('Hello Streamlit')

# st.sidebar.write('Interractive Widgets')
st.write('プログレスバーの表示')
'START'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='test', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたが好きな数字は', option, 'です'

# text = st.sidebar.text_input('あなたの趣味を教えて')
# condition = st.sidebar.slider('調子は？', 0, 100, 50)
# text = st.text_input('あなたの趣味を教えて')
# condition = st.slider('調子は？', 0, 100, 50)

# '趣味：', text
# 'コンディション：', condition

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字追加')
if button:
    right_column.write('こんにちはTくん')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容')

