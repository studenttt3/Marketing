import pandas as pd
import numpy as np
import streamlit as st
import sklearn


cat = pd.read_csv('Categories.csv')
col_wor = pd.read_csv('collage_words.csv')
scores = pd.read_csv('Beauty Products.csv')
scores
summ = 0
type_s = []
for i in scores.columns[1:]:
  type_s.append(st.radio(i, ('Отрицательно','Нейтрально', 'Положительно'), index = 1))
#st.write(len(type_s))
for i in range(len(scores['index'])):
  brand_rate = 0
  br_sc = list(scores.iloc[i][1:])
  #st.write(len(br_sc))
  #st.write(br_sc)
  for j in range(len(br_sc)):
    st.write(int(br_sc[j]))
    #if(type_s[j] == 'Отрицательно'): brand_rate = brand_rate + (10 - int(br_sc[j]))
    #if(type_s[j] == 'Положительно'): brand_rate = brand_rate + int(br_sc[j])
  #scores.loc[i, 'rating'] = brand_rate
#scores
