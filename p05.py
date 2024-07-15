import p03
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# ⑬ 종합성적 과목별 막대그래프 그리기

df = p03.df
N = df.shape[0]
index = np.arange(N)    # [0 1 2 3 4]
names = df.index.values
# names = [df.index[0], df.index[1], df.index[2], df.index[3], df.index[4]]

korean_scores = df['국어'].tolist()
english_scores = df['영어'].tolist()
math_scores = df['수학'].tolist()
science_scores = df['과학'].tolist()

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0][0].bar(names, korean_scores, label='국어')
# ax[0][0].bar(names, df['국어'], label='국어')
ax[0][0].set_title('국어 점수')

ax[0][1].bar(names, english_scores, label='영어')
ax[0][1].set_title('영어 점수')

ax[1][0].bar(names, math_scores, label='수학')
ax[1][0].set_title('수학 점수')

ax[1][1].bar(names, science_scores, label='과학')
ax[1][1].set_title('과학 점수')

plt.suptitle('종합성적')
plt.show()