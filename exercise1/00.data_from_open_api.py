import requests
import json

#외부 api 활용 데이터 수집
authKey = '7bef445c204d9255afcb7573fee0163da90a38fa08908431672ea07f73ae3a4d'

url = "http://data4library.kr/api/loanItemSrch?authKey={}&startDt=2022-01-01&endDt=2023-01-01&from_age=20&to_age=39".format(authKey)

res = requests.get(url)

print(res)
print(json.loads(res.text))
# print(json.loads(res.text))
