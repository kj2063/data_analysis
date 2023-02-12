from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data/filtered_merged_data.csv")
train_set, test_set = train_test_split(data)

X_train = train_set[['쪽수']]
y_train = train_set['가격']

X_test = test_set[['쪽수']]
y_test = test_set['가격']

lr = LinearRegression()
lr.fit(X_train, y_train)

score = lr.score(X_test, y_test)
print("fit score : ",score) # 약 0.1 미만 => 0과 1사이의 값을 갖는데 1에 가까울 수록 좋은 경향성을 보임을 의미.

y_pred = lr.predict(X_test)
res = mean_absolute_error(y_test,y_pred)
print("fit mean absolute err : ",res) # 평균 약 3500원의 차이가 있다.

# res_data = [(i,j) for i,j in zip(X_test['쪽수'],y_pred)]
# print(res_data) # (책의 페이지수, 머신러닝 linearRegrassion 결과로 도출한 책의 가격) 을 튜플 list 로 print 

y_selected_pred = lr.predict(pd.DataFrame(np.array([[1],[10],[100],[1000]]), columns=['쪽수'])) #1,10,100,1000 페이지의 책의 가격을 예측
print("predicted price of 1,10,100,1000 pages book (KRW) => ",y_selected_pred) #결과.

'''
책의 페이지 수 와 가격은 linearRegrassion에 의해 전체적으로 상승하는 경향을 보이나. score점수나, mean_absolute_err를 통해 정확한 예측은 힘들다는 것을 알 수 있다.
'''



""" 
plot 
"""

fig = plt.figure(figsize=(6,4))

x= np.linspace(0,1000)

ax = fig.subplots()

ax.scatter(data["쪽수"],data["가격"],s=2,label="data")
ax.plot(x, lr.coef_*x + lr.intercept_, c='orange', label="predicted")

ax.set_xlabel("$pages$")
ax.set_ylabel("$price(KRW)$")

ax.legend(loc='upper right',fontsize='x-small')

ax.axis([0,1000,0,100000])

plt.show()