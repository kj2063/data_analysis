import requests
import pandas as pd
import chardet
from bs4 import BeautifulSoup

#web crawling for get price & pages
with open("2.28도서관 장서 대출목록 (2022년 12월) (1).csv",mode="rb") as f:
    d = f.readline()

books_pd = pd.read_csv("2.28도서관 장서 대출목록 (2022년 12월) (1).csv",encoding=chardet.detect(d).get("encoding"))

total_data_size = books_pd['번호'].count()

complete_cnt = 0
request_cnt = 0

def getBookScrapData(data_row):
    try:
        global complete_cnt
        global request_cnt

        complete_cnt += 1

        yes24_url = "http://www.yes24.com/product/search?query={}".format(data_row["ISBN"])
        request_cnt += 1
        yes24_res = requests.get(yes24_url)

        soup = BeautifulSoup(yes24_res.text, 'html.parser')
        tag_data = soup.find('a', attrs={'class':'gd_name'})
        
        print('진행된 데이터 수 : {} / {}'.format(complete_cnt,total_data_size))

        if tag_data is None:
            return pd.Series([None,None],index=(['가격','쪽수']))
        else:
            book_detail_url = tag_data["href"]
            request_cnt += 1
            yes24_detail_res = requests.get('http://www.yes24.com' + book_detail_url)

            detail_price_soup = BeautifulSoup(yes24_detail_res.text, 'html.parser')
            detail_price_tag_data = detail_price_soup.find('em', attrs={'class':'yes_m'})

            price = detail_price_tag_data.contents[0].text.rstrip('원').replace(',','')

            detail_page_soup = BeautifulSoup(yes24_detail_res.text, 'html.parser')
            detail_page_div_tag_data = detail_page_soup.find('div', attrs={'id':'infoset_specific'})
            detail_page_tr_tag_list = detail_page_div_tag_data.find_all('tr')

            for tr in detail_page_tr_tag_list:
                if tr.find('th').get_text() == '쪽수, 무게, 크기':
                    pages = tr.find('td').get_text().split()[0].rstrip('쪽')
                    return pd.Series([price, pages],index=(['가격','쪽수']))

            return pd.Series([None,None],index=(['가격','쪽수']))

    except Exception:
        return pd.Series([None,None],index=(['가격','쪽수']))
        # print("error : {} requests attempted".format(request_cnt))
    

books_price = books_pd.apply(getBookScrapData ,axis=1)

books_price.to_csv("pandas_output_books_price_pages.csv",index=False)

