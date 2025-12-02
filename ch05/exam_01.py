import platform

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# macOS인 경우
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')

# Windows의 경우
elif platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')

# 한글 깨짐 방지용
plt.rcParams['axes.unicode_minus'] = False


df = pd.DataFrame({
   '돼지': [20, 18, 489, 675, 1776],
   'horse': [4, 25, 281, 600, 1900]
   }, index=[1990, 1997, 2003, 2009, 2014])
df.plot.line()

plt.show()

