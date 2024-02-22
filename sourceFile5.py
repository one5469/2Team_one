'''
    - 지역별/시설별 피해 규모를 파악하기 위한 소스 파일
    - 2000년대 이후로 가장 강력했던 루사와 매미 분석
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import koreanize_matplotlib
import funcFile

# 데이터 전처리
DF = pd.read_excel('./DATA/typhoon_damage_detail.xlsx')
drop_col_list = [col for col in DF.columns if 'Unnamed' in col]
clearDF = DF.drop(columns=drop_col_list)
clearDF = clearDF.fillna(method='ffill')
# print(clearDF.head())

# 루사랑 매미 구분하기 위한 컬럼 추출
lusa_cols = ['대분류', '중분류', '소분류', '총계']
maemi_cols = ['대분류', '중분류', '소분류', '총계']

for col in clearDF.columns:
    if '2002' in col:
        lusa_cols.append(col)
    elif '2003' in col:
        maemi_cols.append(col)

lusa_depart = [dep.split(' / ')[0] for dep in lusa_cols[4:]]
maemi_depart = [dep.split(' / ')[0] for dep in maemi_cols[4:]]

# 데이터프레임 나누기
lusaDF = clearDF[lusa_cols]
maemiDF = clearDF[maemi_cols]

# 그래프들 그리기
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[0][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[0][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 이재민수 분포')
plt.legend(['2002년 루사', '2003년 매미'])
plt.xlabel('지역별')
plt.ylabel('이재민수(명)')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[2][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[2][maemi_cols][4:], width=0.3, align='edge')
plt.bar(lusa_depart, lusaDF.iloc[4][lusa_cols][4:], width=-0.3, align='edge', bottom=lusaDF.iloc[2][lusa_cols][4:])
plt.bar(maemi_depart, maemiDF.iloc[4][maemi_cols][4:], width=0.3, align='edge', bottom=maemiDF.iloc[2][maemi_cols][4:])
plt.xticks(rotation=90)

plt.title('지역별 사상자 피해 분포')
plt.legend(['2002년 사망자', '2003년 사망자', '2002년 부상자', '2003년 부상자'])
plt.xlabel('지역별')
plt.ylabel('사상자')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[3][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[3][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 실종자 피해 분포')
plt.legend(['2002년 실종자', '2003년 실종자'])
plt.xlabel('지역별')
plt.ylabel('실종자')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[13][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[13][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 건물 피해 분포')
plt.legend(['2002년 루사', '2003년 매미'])
plt.xlabel('지역별')
plt.ylabel('피해액')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[19][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[19][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 선박 피해 분포')
plt.legend(['2002년 루사', '2003년 매미'])
plt.xlabel('지역별')
plt.ylabel('피해액')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[23][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[23][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 농작지 피해 분포')
plt.legend(['2002년 루사', '2003년 매미'])
plt.xlabel('지역별')
plt.ylabel('피해액')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[23][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[23][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 농작지 피해 분포')
plt.legend(['2002년 루사', '2003년 매미'])
plt.xlabel('지역별')
plt.ylabel('피해액')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[59][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[59][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 공공시설 피해 분포')
plt.legend(['2002년 루사', '2003년 매미'])
plt.xlabel('지역별')
plt.ylabel('피해액')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.plot(figsize=(16, 5))
plt.grid(alpha=0.35)
plt.gca().set_facecolor('aliceblue')
plt.bar(lusa_depart, lusaDF.iloc[67][lusa_cols][4:], width=-0.3, align='edge')
plt.bar(maemi_depart, maemiDF.iloc[67][maemi_cols][4:], width=0.3, align='edge')
plt.xticks(rotation=90)

plt.title('지역별 사유시설 피해 분포')
plt.legend(['2002년 루사', '2003년 매미'])
plt.xlabel('지역별')
plt.ylabel('피해액')
plt.tight_layout()
plt.show()