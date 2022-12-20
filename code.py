import pandas as pd
import numpy as np
import streamlit as st
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

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
if(cat_ch == 'Health products and services'):
  st.image('https://www.dermascope.com/media/k2/items/cache/5904efb920b46f92d82ad6e67c3d77eb_XL.jpg')
if(cat_ch == 'Household Products'):
  st.image('https://www.remodelista.com/wp-content/uploads/2019/01/organized-home-book-sink-detail-matthew-williams-crop-1536x1066.jpg')
if(cat_ch == 'Food and dining'):
  st.image('https://www.eatlovesavor.com/wp-content/uploads/2017/03/les-airelles.jpg')
if(cat_ch == 'Beauty Products'):
  st.image('http://cdn.shopify.com/s/files/1/0254/1915/3493/products/Untitleddesign_34.png?v=1654186690')
if(cat_ch == 'Department Stores'):
  st.image('https://www.japan-guide.com/g20/2072_02.jpg')
if(cat_ch == 'Home design and Decoration'):
  st.image('https://media.designcafe.com/wp-content/uploads/2021/05/19174427/minimalist-home-design-ideas.jpg')
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
  
scores1 = scores.drop(columns=["index", "rating"])

fig = plt.figure(figsize = (10,8), dpi = 80)
sns.heatmap(scores1.corr(), xticklabels = scores1.corr().columns, yticklabels = scores1.corr().columns, cmap ='RdYlGn', center = 0, annot = True)
plt.title('Коррелограмм', fontsize = 24)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
st.pyplot(fig)
