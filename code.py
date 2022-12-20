import pandas as pd
import numpy as np
import streamlit as st
import sklearn

cat = pd.read_csv('Categories.csv')
col_wor = pd.read_csv('collage_words.csv')

st.header("Добро пожаловать, дорогой друг!")
st.markdown("Мы, создатели этого проекта, хотим, чтобы шопинг для вас стал проще, быстрее, а выбор товаров наиболее точно попадал в ваши запросы.")
st.image("https://assets.teenvogue.com/photos/62e08a1c0273eb8e9a147959/3:4/w_3075,h_4100,c_limit/GettyImages-1177004878.jpg", width = 600)
st.markdown("Пожалуйста, выберите категорию товаров, а мы подберем наиболее подходящие бренды внутри этой категории.")
cat_ch = st.selectbox("Категория", cat['Category'].unique())
scores = pd.read_csv(cat_ch + '.csv')

which = st.radio('Что важнее для вас при подборе брендов', ('Быстрота', 'Точность'))
if(which == 'Быстрота'): n = 5
if(which == 'Точность'): n = 25

scores
summ = 0
type_s = []
for i in scores.columns[1:n + 1]:
  type_s.append(st.radio(i, ('Отрицательно','Нейтрально', 'Положительно'), index = 1))
#st.write(len(type_s))
for i in range(len(scores['index'])):
  brand_rate = 0
  br_sc = list(scores.iloc[i][1:n + 1])
  #st.write(len(br_sc))
  #st.write(br_sc)
  for j in range(len(br_sc)):
    #st.write(int(br_sc[j]))
    if(type_s[j] == 'Отрицательно'): brand_rate = brand_rate + 10 - int(br_sc[j])
    if(type_s[j] == 'Положительно'): brand_rate = brand_rate + int(br_sc[j])
    else: brand_rate = brand_rate
  scores.loc[i, 'rating'] = brand_rate
#scores
sorted_sc = scores.sort_values(by='rating')
sorted_sc
sorted_sc = sorted_sc.reset_index()
st.write("5 самых подходящих по характеристикам брендов:")
for i in range(5):
  st.write(sorted_sc['index'][len(sorted_sc) - 1 - i])
