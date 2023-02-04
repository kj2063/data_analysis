from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pandas as pd

data = pd.read_csv("data/filtered_merged_data.csv")
train_set, test_set = train_test_split(data)

X_train = train_set[['쪽수']]
y_train = train_set['가격']

X_test = test_set[['쪽수']]
y_test = test_set['가격']

lr = LinearRegression()
lr.fit(X_train, y_train)

# score = lr.score(X_test, y_test)
# print(score) # 약 0.1 미만 => 0과 1사이의 값을 갖는데 1에 가까울 수록 좋은 경향성을 보임을 의미.

y_pred = lr.predict(X_test)
# res = mean_absolute_error(y_test,y_pred)
# print(res) # 평균 약 3500원의 차이가 있다.

# res_data = [(i,j) for i,j in zip(X_test['쪽수'],y_pred)]
# print(res_data) # (책의 페이지수, 머신러닝 linearRegrassion 결과로 도출한 책의 가격) 을 튜플 list 로 print 

y_selected_pred = lr.predict([[1],[10],[100],[1000]]) #1,10,100,1000 페이지의 책의 가격을 예측
print(y_selected_pred) #결과.

'''
책의 페이지 수 와 가격은 linearRegrassion에 의해 전체적으로 상승하는 경향을 보이나. score점수나, mean_absolute_err를 통해 정확학 예측은 힘들다는 것 을 알 수 있다.
'''