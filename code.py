import pandas as pd
import numpy as np
import streamlit as st
import sklearn

cat = pd.read_csv('Categories.csv')
col_wor = pd.read_csv('collage_words.csv')

st.header("Добро пожаловать, дорогой друг!")
st.markdown("Мы, создатели этого проекта, хотим, чтобы шопинг для вас стал проще, быстрее, а выбор товаров наиболее точно попадал в ваши запросы.")
st.image("https://assets.teenvogue.com/photos/62e08a1c0273eb8e9a147959/3:4/w_3075,h_4100,c_limit/GettyImages-1177004878.jpg", width = 300)
st.markdown("Пожалуйста, выберите категорию товаров, а мы подберем наиболее подходящие бренды внутри этой категории.")
cat_ch = st.selectbox("Категория", cat['Category'].unique())
if(cat_ch == 'Beverages'):
  st.image("https://www.mbbmanagement.com/wp-content/uploads/2020/03/beverage-management.jpg")
if(cat_ch == 'Clothing products'):
  st.image("https://images.squarespace-cdn.com/content/v1/58c90e50bebafbba1ac44f56/1603290772524-SKGGCSIPRRDR7HSVVA6X/baby+clothes.jpg")
if(cat_ch == 'Cars'):
  st.image("https://aif-s3.aif.ru/images/016/664/d7018fd8b45e9c280c4f70f0692d400e.jpg")
scores = pd.read_csv(cat_ch + '.csv')

st.markdown("В зависимости от располагаемого времени выберите тип подбора. Мы можем сделать более быстрый подбор с меньшим количеством вопросов в опроснике или более точный, но требующий от вас большего количества ответов.")
which = st.radio('Что важнее для вас при подборе брендов', ('Быстрота', 'Точность'))
if(which == 'Быстрота'): n = 5
if(which == 'Точность'): n = 25

st.markdown("Мы отобрали для вас самые популярные слова, используемые для характеристик брендов внутри выбранной вами категории. К каждой характеристике или ассоциации выберите ваше отношение к ней в продукте.")
type_s = []
for i in scores.columns[1:n + 1]:
  type_s.append(st.radio(i, ('Отрицательно','Нейтрально', 'Положительно'), index = 1))
for i in range(len(scores['index'])):
  brand_rate = 0
  br_sc = list(scores.iloc[i][1:n + 1])
  for j in range(len(br_sc)):
    if(type_s[j] == 'Отрицательно'): brand_rate = brand_rate + 10 - int(br_sc[j])
    if(type_s[j] == 'Положительно'): brand_rate = brand_rate + int(br_sc[j])
    else: brand_rate = brand_rate
  scores.loc[i, 'rating'] = brand_rate
sorted_sc = scores.sort_values(by='rating')
#sorted_sc
sorted_sc = sorted_sc.reset_index()
st.write("5 самых подходящих по характеристикам брендов:")
for i in range(5):
  st.write(sorted_sc['index'][len(sorted_sc) - 1 - i])
