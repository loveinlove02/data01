import p03
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'Malgun Gothic'

df = p03.df
# print(df)

N = df.shape[0]     # 5
index = np.arange(N)    # [0 1 2 3 4]
# print(index)

names = [df.index[0], df.index[1], df.index[2], df.index[3], df.index[4]]
# names = df.index.values

korean_scores = df['국어'].tolist()
english_scores = df['영어'].tolist()
math_scores = df['수학'].tolist()
science_scores = df['과학'].tolist()

fig, ax = plt.subplots(figsize=(10,6))

ax.bar(index-0.3, korean_scores,  width=0.2, label='국어')
ax.bar(index-0.1, english_scores, width=0.2, label='영어')
ax.bar(index+0.1, math_scores,    width=0.2, label='수학')
ax.bar(index+0.3, science_scores, width=0.2, label='과학')

for i in range(0, len(index), 1):
    ax.text(i-0.4, korean_scores[i]+1.5, korean_scores[i], va='center', fontsize=11, color='blue')
    ax.text(i-0.2, english_scores[i]+1.5, english_scores[i], va='center', fontsize=11, color='blue')
    ax.text(i, math_scores[i]+1.5, math_scores[i], va='center', fontsize=11, color='blue')
    ax.text(i+0.2, science_scores[i]+1.5, science_scores[i], va='center', fontsize=11, color='blue')

ax.set_xlabel('이름')
ax.set_ylabel('점수')
ax.set_xticks(index, names)
ax.set_yticks(np.arange(0, 120, 20))
ax.legend(loc='upper right', ncol=1)
plt.show()


# https://velog.io/@ysw2946/3-1.-Text-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0