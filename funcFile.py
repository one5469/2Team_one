'''
    - 함수 파일
'''
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt

# 포아송분포
def Poi(lam, x):
    return np.power(lam, x) / scipy.special.factorial(x) * np.exp(-lam)

# 지수분포
def Ex(lam, x):
    if x:
        return lam * np.exp(-lam * x)
    else:
        return 0


# 포아송분포 및 지수분포 시각화
def draw_Poi_Ex(lam, ylim=0.5):
    plt.figure(figsize=(10, 6))
    plt.bar(range(0, 6), [Poi(lam, x) for x in range(0, 6)], color='royalblue')
    plt.plot(range(1, 6), [Ex(lam, x) for x in range(1, 6)],
             color='gold', marker='o')
    plt.ylim(0.0, ylim)

    plt.grid(alpha=0.35)
    plt.ylabel('Probability')
    plt.legend(['Ex(λ)', 'Poi(λ)'])
    plt.title('Probability Distribution')
    plt.gca().set_facecolor('aliceblue')

    for x in range(0, 6):
        plt.text(x=x, y=Poi(lam, x) + 0.01,
                 s=f'{round(Poi(lam, x), 3)}',
                 horizontalalignment='center',
                 color='r')

    for x in range(2, 6):
        plt.text(x=x, y=Ex(lam, x) + 0.01,
                 s=f'{round(Ex(lam, x), 3)}',
                 horizontalalignment='center',
                 color='r')
    plt.show()