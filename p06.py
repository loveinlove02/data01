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
subject_names = df.columns.values

korean_scores  = df['국어'].to_list()
english_scores = df['영어'].tolist()
math_scores = df['수학'].tolist()
science_scores = df['과학'].tolist()

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

n = 0

for i in range(0, 2, 1):
    for j in range(0, 2, 1):
        name = names[n]

        ax[i][j].pie(korean_scores, labels=names, autopct='%1.1f%%', startangle=90)    
        ax[i][j].set_title(subject_names[n])
        n=n+1

plt.legend(loc=(1.0, 0.8))
plt.suptitle('종합성적')
plt.show()