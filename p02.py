import pandas as pd
import numpy as np

np.random.seed(888)      

data = np.random.randint(0, 101, size=(5, 4))
# print(data)

col = ['국어', '영어', '수학', '과학']
ind = ['홍길동','김철수','이영희','김민수','김민우']

df = pd.DataFrame(
    data=data, 
    columns=col, 
    index=ind
)

# print(f'*******기말고사 성적******')
# print(df)