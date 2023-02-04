import pandas as pd
import chardet
import numpy as np


with open("data/2.28도서관 장서 대출목록 (2022년 12월) (1).csv",mode="rb") as f:
    d = f.readline()

origin_data = pd.read_csv("data/2.28도서관 장서 대출목록 (2022년 12월) (1).csv", encoding=chardet.detect(d).get('encoding')).drop("Unnamed: 13", axis=1)
web_clawled_data = pd.read_csv("data/pandas_output_books_price_pages.csv")

pages_data = pd.DataFrame(pd.to_numeric(web_clawled_data["쪽수"],errors='coerce'),columns=["쪽수"])

new_web_data = pd.merge(web_clawled_data["가격"],pages_data,left_index=True,right_index=True)

merged_data = pd.merge(origin_data,new_web_data,left_index=True, right_index=True)


res_filtered_data = merged_data[np.isnan(merged_data["쪽수"]) == False]

res_filtered_data.to_csv("data/filtered_merged_data.csv",index=False)
