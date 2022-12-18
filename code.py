import pandas as pd
import numpy as np
import streamlit as st

cat = pd.read_csv('Categories.csv')
col_wor = pd.read_csv('collage_words.csv')
for i in cat['Category'].unique():
  st.write(i)
#print(col_wor)
