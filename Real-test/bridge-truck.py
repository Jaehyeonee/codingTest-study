
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight =0
    bridge = [0]*bridge_length

    while len(truck_weights)==0:
        if 



    
    return answer


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def load_csv(path):
    '''pandas를 이용하여 데이터를 DataFrame의 형태로 불러와 반환하는 load_csv 함수를 작성합니다.'''
    data = pd.read_csv(path)
    data = pd.DataFrame(data)
    return data
457
def main():

    # 데이터 주소
    TRAIN_PATH = 'data/train.csv'
    TEST_PATH = 'data/test.csv'
    SUBMISSION_PATH = 'data/sample_submission.csv'
                
    # load_csv 함수를 사용하여 데이터를 불러와 저장합니다.
    train = load_csv(TRAIN_PATH)
    test = load_csv(TEST_PATH)
    submission = load_csv(SUBMISSION_PATH)

    # 문자열에 대한 원핫인코딩 
    train_df = pd.get_dummies(train)
    print(train_df.columns)

    x = train_df[train_df.columns.difference(['price'])]
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    y = train_df["price"]

    model = LinearRegression()

    X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=42)
    model.fit(X_train,y_train)

    # test 데이터의 문자열에 대한 원핫인코딩
    test_df = pd.get_dummies(test)

    # 모델을 사용하여 test 데이터에 대한 'price' 예측
    y_pred = model.predict(test_df)

    # 예측값을 원본 test 데이터에 추가합니다.
    test['predicted_price'] = y_pred

    # 예측값이 추가된 test 데이터를 저장하거나 분석에 활용합니다.
    # test.to_csv('predicted_test.csv', index=False)  # 예측값을 CSV 파일로 저장 (옵션)
    submission['price'] = y_pred
    # test 데이터에 대한 'price' 예측값을 확인
    print(submission)
    # return submission
    return submission
if __name__ == "__main__":
    sys.exit(main())
