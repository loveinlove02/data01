import p03
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'Malgun Gothic' 
matplotlib.rcParams['axes.unicode_minus'] = False  

df = p03.df
# print(df)
N = df.shape[0]
index = np.arange(N)    # [0 1 2 3 4]
names = df.index.values

korean_scores  = df['국어'].to_list()
english_scores = df['영어'].tolist()
math_scores = df['수학'].tolist()
science_scores = df['과학'].tolist()

fig, ax = plt.subplots(2, 2, figsize=(10,6))



plt.suptitle('종합성적')
plt.show()
