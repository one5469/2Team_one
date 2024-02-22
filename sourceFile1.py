'''
    - 크롤링으로 데이터를 받아 csv파일로 추출하기 위한 소스 파일
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.weather.go.kr/w/typhoon/typ-stat.do')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table = soup.select('div.over-scroll > table')[1]

header = table.select_one('tr.tablesorter-headerRow')
rows = table.select('tbody > tr')

col_names = [h.text for h in header.select('th > div.tablesorter-header-inner')]
total_data_list = [col_names]
kor_data_list = [col_names]

for row in rows:
    th = row.select_one('th')
    tds = row.select('td')
    total_row_list = [th.text.strip()]
    kor_row_list = [th.text.strip()]

    for td in tds:
        value = td.text.strip()
        if '(' in value:
            t, k = value.split('(')
            total_row_list.append(t)
            kor_row_list.append(k[:-1])
        else:
            total_row_list.append(value)
            kor_row_list.append(0)

    total_data_list.append(total_row_list)
    kor_data_list.append(kor_row_list)

print('Data crawling complete.')
print()
print('Data List :: ')
print(total_data_list)

totalDF = pd.DataFrame(total_data_list)
korDF = pd.DataFrame(kor_data_list)
print('Construction DataFrame complete.')
print()
print('DataFrame :: ')

totalDF.to_csv('total_year_typhoon.csv')
korDF.to_csv('kor_year_typhoon.csv')
print('Exporting data complete.')