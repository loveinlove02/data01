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
names = df.index.values # ['홍길동' '김철수' '이영희' '김민수' '김민우']
subject_names = df.columns.values   # ['국어' '영어' '수학' '과학']

# print('index: ', index)
# print('학생 이름:', names)
# print('과목 이름:', subject_names)

korean_scores = df['국어'].to_list()
english_scores = df['영어'].tolist()
math_scores = df['수학'].tolist()
science_scores = df['과학'].tolist()

scores_list = [korean_scores, english_scores, math_scores, science_scores]
# print(scores_list)
# [[36.5, 33.0, 92.5, 18.5, 92.5], [40.5, 43.5, 24.5, 19.5, 58.5], [42.0, 61.0, 52.0, 48.0, 41.5], [73.5, 25.5, 32.5, 39.0, 43.0]]

'''
이것도 가능
scores_list = []
for sub_name in subject_names:
    scores_list.append(df[sub_name].to_list())
'''

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

n = 0

for i in range(0, 2, 1):        # 0 1
    for j in range(0, 2, 1):    # 0 1
        ax[i][j].pie(scores_list[n], labels=names, autopct='%1.1f%%', startangle=90)
        ax[i][j].set_title(subject_names[n])  # 0 0, 0 1, 1 0, 1 1
        n=n+1

plt.legend(loc=(1.0, 0.8))
plt.suptitle('종합성적')
plt.show()
