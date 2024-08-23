import streamlit as st
import time

st.title('Streamlit 超入門')




# st.write('プログレスバーの表示')
# 'Start!!'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress((i + 1))
#     time.sleep(0.1)

# st.write('Done !!!!!')


# st.write('Interactive Widgets')

# left_columnn, right_columun = st.columns(2)
# button = left_columnn.button('右カラムに文字を表示')
# if button:
#     right_columun.write('ここは右カラム')

# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く 1')
# expander.write('問い合わせ内容を書く 2')


# expander1 = st.expander('問い合わせ 1')
# expander1.write('問い合わせの回答 1')
# expander2 = st.expander('問い合わせ 2')
# expander2.write('問い合わせの回答 2')
# expander3 = st.expander('問い合わせ 3')
# expander3.write('問い合わせの回答 3')


# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味は ', text,' です'
# 'コンディション: ', condition


# st.write('Interactive Widgets')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション: ', condition

# option = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は ', option,' です'

# option = st.selectbox(
#     'あなたの好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です'

# st.write('Display Image')
# if st.checkbox('Show Image'):
#     img = Image.open('画像.png')
#     st.image(img, caption='積算計', use_column_width=True)


# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],  # 新宿付近
#     columns=['lat', 'lon']
# )
# st.map(df)


# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


# st.write(df)
# st.table(df)  # 静的テーブル


# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4, 5],
#     '2列目':[10, 20, 30, 40, 35]
# })
# st.dataframe(df.style.highlight_max(axis=0), width=200)  # 引数でいろいろ設定できる


# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
