import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

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
col_wor.dropna(inplace=True)
brandwise = col_wor.groupby(by=['Brand'], as_index=False).agg(lambda x: ", ".join(x))
all_words_beauty = list(chain(*words["Words"].apply(lambda x: x.split(", ")).values))
vectorizer = TfidfVectorizer(max_df=0.95, min_df=0.05)

#print(col_wor)
