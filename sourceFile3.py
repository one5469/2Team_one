'''
    - 연도별 태풍에 의한 피해를 이재민수와 총재산피해를 통해 분석하기 위한 소스 파일
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import koreanize_matplotlib
import re
from copy import deepcopy

DF = pd.read_excel('./DATA/typhoon_damage.xlsx')
DF.fillna(method='ffill', inplace=True)
DF['구분 / 시설'] = DF['구분 / 시설'].astype('int32')

plt.figure(figsize=(11, 5))
plt.bar(DF['구분 / 시설'].unique(), DF[DF['비고']=='가']['이재민(인)'])
plt.xticks(DF['구분 / 시설'].unique(), rotation=90)
plt.xlabel('연도별')
plt.ylabel('이재민수(명)')
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.tight_layout()
plt.show()

plt.figure(figsize=(11, 5))
plt.bar(DF['구분 / 시설'].unique(), DF[DF['비고']=='나']['합계'])
plt.xticks(DF['구분 / 시설'].unique(), rotation=90)
plt.xlabel('연도별')
plt.ylabel('재산피해총량(조 원)')
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.tight_layout()
plt.show()

# 2002년과 2003년 제외하고 출력
restDF = DF[(DF['구분 / 시설'] != 2002) & (DF['구분 / 시설'] != 2003)]
plt.figure(figsize=(11, 5))
plt.bar(restDF['구분 / 시설'].unique(), restDF[restDF['비고']=='가']['이재민(인)'])
plt.xticks(restDF['구분 / 시설'].unique(), rotation=90)
plt.xlabel('연도별')
plt.ylabel('이재민수(명)')
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.tight_layout()
plt.show()

plt.figure(figsize=(11, 5))
plt.bar(restDF['구분 / 시설'].unique(), restDF[restDF['비고']=='나']['합계'])
plt.xticks(restDF['구분 / 시설'].unique(), rotation=90)
plt.xlabel('연도별')
plt.ylabel('재산피해총량(조 원)')
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.tight_layout()
plt.show()