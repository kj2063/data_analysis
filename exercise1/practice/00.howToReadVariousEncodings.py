import chardet
import pandas as pd

with open("2.28도서관 장서 대출목록 (2022년 12월) (1).csv",mode="rb") as f:
    d = f.readline()

print(chardet.detect(d))


with open("2.28도서관 장서 대출목록 (2022년 12월) (1).csv",encoding="EUC-KR") as file:
    print(file.readline())


'''
 지금 버전 판다스는 3개 다 잘되는듯?
'''
# pd_read = pd.read_csv("2.28도서관 장서 대출목록 (2022년 12월) (1).csv",encoding="EUC-KR")
# pd_read = pd.read_csv("2.28도서관 장서 대출목록 (2022년 12월) (1).csv",encoding="EUC-KR", low_memory=False)
pd_read = pd.read_csv("2.28도서관 장서 대출목록 (2022년 12월) (1).csv",encoding="EUC-KR", dtype={"ISBN":str, "세트 ISBN":str, "주제분류번호":str}, )

# print(pd_read)
print(pd_read.head())

'''
판다스 데이터프레임을 csv파일로 저장
'''
# pd_read.to_csv("pandas_output_csv_file.csv") 
# pd_read.to_csv("pandas_output_csv_file.csv",index=False) 