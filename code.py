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
st.image("https://i.pinimg.com/564x/de/39/51/de3951cb7f208704a6af5fd303989639.jpg", width = 300)
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
st.image(cat_ch + ' (1).png')
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
sns.heatmap(scores1.corr(), xticklabels = scores1.corr().columns, yticklabels = scores1.corr().columns, cmap ='RdYlGn', center = 0, annot = False)
plt.title('Коррелограмм', fontsize = 24)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
st.pyplot(fig)

col_wor.dropna(inplace=True)
brandwise = col_wor.groupby(by=['Brand'], as_index=False).agg(lambda x: ", ".join(x))
category1 = list(np.unique(np.array(cat['Category'])))
categorywise1 = []
ccccc = 0
for i in category1:
    print(i)
    categorywise1.append('')
    print(cat.iloc[cat.index[cat['Category'] == i].tolist()]['Brand'])
    for j in cat.iloc[cat.index[cat['Category'] == i].tolist()]['Brand']:
        categorywise1[ccccc] += brandwise.iloc[brandwise.index[brandwise['Brand'] == j].tolist()[0]]['Words']
    ccccc += 1
categorywisedf = pd.DataFrame({'Category': category1, 'Words': categorywise1})
words_stat = pd.Series(categorywisedf.iloc[category1.index(cat_ch)]['Words'].split(", ")).value_counts()
fig = plt.figure(figsize = (10,8), dpi = 80)
words_stat.hist(bins=50, label='Beverages', color='powderblue')
st.pyplot(fig)

st.markdown("Но это еще не всё! Мы хотим дать вам еще больше рекомендаций, основываясь на том, какие бренды косметики нравились пользователям, похожим на вас. При этом мы хотим минимизировать ваше недовольство. Пожалуйста, выберите из следующих списков брендов тот, который нравится вам меньше всего.")
ank = pd.read_csv("ank.csv")
llsstt = []
for i in range(5):
  sttr = ank['anketa0']
  for j in range(5):
    sttr = sttr + ' ' + ank['anketa' + str(i + 1)]
  llsstt.append(sttr)
st.write(llsstt)
not_like = st.radio('', (ank['anketa0'],ank['anketa1'], ank['anketa2'], ank['anketa3'], ank['anketa4']), index = 1)

rec = pd.read_csv("rec.csv")
rec
