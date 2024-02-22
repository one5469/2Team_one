'''
    - 전체 태풍발생량과 이 중 한국에 영향을 미친 태풍들을 토대로 포아송 분포 및 지수분포를 분석하는 소스 파일
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import koreanize_matplotlib
import re
import funcFile
from copy import deepcopy

# 전체 태풍 발생량
totalDF = pd.read_csv('total_year_typhoon.csv', header=1, index_col='연도/월')
totalDF.drop(columns='0', inplace=True)
totalDF.fillna(0, inplace=True)

# 한국에 영향을 끼친 태풍
korDF = pd.read_csv('kor_year_typhoon.csv', header=1, index_col='연도/월')
korDF.drop(columns='0', inplace=True)
korDF.fillna(0, inplace=True)

plt.figure(figsize=(8,6))

# 30년 평균과 10년 평균을 기준으로 분포 분석
plt.plot(totalDF.loc['30년평균1991-2020'][:-1])
plt.plot(totalDF.loc['10년평균2011-2020'][:-1])
plt.plot(korDF.loc['30년평균1991-2020'][:-1])
plt.plot(korDF.loc['10년평균2011-2020'][:-1])

plt.legend(['종합 30년 평균', '종합 10년 평균', '국내 30년 평균', '국내 10년 평균'], loc='upper left')
plt.xlabel('월별')
plt.ylabel('태풍발생 횟수')
plt.show()

lam30 = korDF.loc['30년평균1991-2020'][-1]
lam10 = korDF.loc['10년평균2011-2020'][-1]
print(lam30, lam10)

funcFile.draw_Poi_Ex(lam30, 0.3)
funcFile.draw_Poi_Ex(lam10,0.3)