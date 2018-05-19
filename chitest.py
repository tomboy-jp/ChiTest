import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

measured = pd.DataFrame(
    [[2254, 2746],[2567, 2433]],
    columns=['きのこが好き', 'たけのこが好き'],
    index=['男','女']
    )

# Pythonだけでやる場合
measured['合計'] = measured.sum(axis=1).astype(int)
measured = measured.append(measured.sum(axis=0), ignore_index=True)
measured.index = ['男', '女', '合計']
measured.iloc[2,1]

expectation = pd.DataFrame(
    [[(measured.iloc[2,0]*measured.iloc[0,2]/measured.iloc[2,2]),(measured.iloc[2,1]*measured.iloc[0,2]/measured.iloc[2,2])],
    [(measured.iloc[2,0]*measured.iloc[1,2]/measured.iloc[2,2]),(measured.iloc[2,1]*measured.iloc[1,2]/measured.iloc[2,2])]],
    columns=['きのこが好き', 'たけのこが好き'],
    index=['男','女']
    )

chi = pd.DataFrame(
    [[((measured.iloc[0,0]-expectation.iloc[0,0])**2/expectation.iloc[0,0]), ((measured.iloc[0,1]-expectation.iloc[0,1])**2/expectation.iloc[0,1])],
    [((measured.iloc[1,0]-expectation.iloc[1,0])**2/expectation.iloc[1,0]), ((measured.iloc[1,1]-expectation.iloc[1,1])**2/expectation.iloc[1,1])]],
    columns=['きのこが好き', 'たけのこが好き'],
    index=['男','女']
    )

# 面倒だし、少しズレる
print(chi.values.sum())

# scipyで一気にやると簡単だし正確
print(stats.chi2_contingency(measured.iloc[:2,:2])[0])
