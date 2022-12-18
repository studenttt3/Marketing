import pandas as pd
import numpy as np
import streamlit as st

cat = pd.read_csv('Categories.csv')
col_wor = pd.read_csv('collage_words.csv')
for i in cat['Category'].unique():
  st.write(i)
beauty = cat[cat['Category'] == 'Beauty Products']
beauty
for i in beauty['Brand'].unique():
  st.write(i)
optionals1 = st.expander("диапазон", True)
min1 = optionals1.slider("", min_value = 0, max_value = 10)
st.write(min1)
#print(col_wor)
