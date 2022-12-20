import pandas as pd
import numpy as np
import streamlit as st
import sklearn


cat = pd.read_csv('Categories.csv')
col_wor = pd.read_csv('collage_words.csv')
scores = pd.read_csv('Beauty Products.csv')
summ = 0
type_s = []
for i in scores.columns[1:]:
  type_s.append(st.radio(i, ('Отрицательно','Нейтрально', 'Положительно')))
  #if(type_s == 'Отрицательно'): summ = summ + scores[
    



