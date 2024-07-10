import pandas as pd
import numpy as np

# 난수 생성기를 초기화합니다. 777은 시드 값입니다. 
# 시드 값을 설정하면, 이후에 생성되는 난수들이 항상 동일한 순서로 생성됩니다. 
# 이는 코드 실행 시마다 같은 난수를 얻기 위해 사용됩니다.
np.random.seed(777)      
# print(np.random.rand(5)) # 항상 동일한 값이 출력

# 5행 4열의 2차원 배열을 생성하고, 각 요소는 0과 100 사이의 무작위 수(난수)로 채웁니다.
data = np.random.randint(0, 101, size=(5, 4))
# print(data)

col = ['국어', '영어', '수학', '과학']
ind = ['홍길동','김철수','이영희','김민수','김민우']

df = pd.DataFrame(
    data=data, 
    index=ind, 
    columns=col
)

# print(f'*******중간고사 성적******')
# print(df)