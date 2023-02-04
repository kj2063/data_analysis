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
score = lr.score(X_test, y_test)

print(score) # 0.7~0.8

# y_pred = lr.predict(X_test)
# res = mean_absolute_error(y_test,y_pred)
# print(res) # 3400 ~ 3500

'''
책의 페이지 수 와 가격에는 거의 연관성이 없다는 것을 알 수 있다.
'''