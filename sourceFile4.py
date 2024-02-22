'''
    - 피해 규모가 크고 위력이 강한 태풍들을 선정해서 분석하기 위한 소스 파일
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import koreanize_matplotlib
import funcFile

# 연도별 태풍 선정
# 선정 기준 : 이재민수 / 총재산피해가 높았던 태풍 및 위력이 강력했던 태풍
# 선정 근처 : 국민재난안전포털 자료 및 나무위키
typhoon_dict = {
    1998: ['예니'],
    1999: ['올가'],
    2001: ['제비'],
    2002: ['루사'],
    2003: ['매미'],
    2004: ['메기'],
    2006: ['애위니아'],
    2009: ['모라꼿'],
    2012: ['볼라벤', '덴빈', '산바'],
    2016: ['차바'],
    2019: ['링링'],
    2020: ['바비', '마이삭'],
    2022: ['힌남노']
}

period = np.arange(1998, 2023)  # 연도 기간
lam = 16 / 25                   # 람다값 : 1년에 발생한 태풍 횟수
print(lam)

# poi :: np.power(lam, x) / scipy.special.factorial(x) * np.exp(-lam)

funcFile.draw_Poi_Ex(lam, 0.65)