import pandas as pd
import numpy as np

cat = pd.read_csv('Categories.csv')
col_wor = pd.read_csv('collage_words.csv')
print(cat['Category'].unique)
#print(col_wor)
