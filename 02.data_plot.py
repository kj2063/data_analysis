import matplotlib.pyplot as plt
import pandas as pd

#페이지 수와 가격의 상관관계 시각화

data_frame = pd.read_csv("data/filtered_merged_data.csv")

fig = plt.figure(figsize=(19,5))

ax = fig.subplots()

ax.scatter(data_frame["가격"],data_frame["쪽수"])

ax.set_xlabel("$price(KRW)$")
ax.set_ylabel("$pages$")

ax.axis([0,100000,0,1000])

plt.show()