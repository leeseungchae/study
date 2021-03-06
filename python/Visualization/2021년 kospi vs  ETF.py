
import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy as np

import FinanceDataReader as fdr

# 2021년 ~ 2022년 1월 23일 
# 종합지수 , 반도체 ,2차전지 , 바이오 ,금융 지수 비교

kospi = fdr.DataReader('KS11','2021-01-04', '2022-01-23')

#se =반도체
se = fdr.DataReader('091230', '2021-01-04', '2022-01-23')   
#ba =2차전지
ba = fdr.DataReader('364960', '2021-01-04', '2022-01-23')
#bio =바이오
bio = fdr.DataReader('244580', '2021-01-04', '2022-01-23')
#inv =금융
inv = fdr.DataReader('139270', '2021-01-04', '2022-01-23')

#날짜 데이터
date=kospi.index 

#종가 불러오기
kospi=kospi['Close']

se=se['Close']
ba=ba['Close']
bio = bio['Close']
inv = inv['Close']


# 종가 가격 코스피 기준 조정 함수
def cor(ticker):
    a = fdr.DataReader(ticker, '2021-01-04', '2021-01-04')
    kospi = fdr.DataReader('KS11', '2021-01-04', '2021-01-04')
    a = a['Close']
    kospi = kospi['Close']
    div = kospi/a
    return div


# 2021/01/04 코스피 지수  2944

# print(cor('091230'))  #0.083
# print(cor('364960'))  #0.241
# print(cor('244580'))  #0.168
# print(cor('139270'))  #0.497

y1 = kospi        
y2 = se*0.083
y3 = ba *0.241
y4 = bio *0.168
y5 = inv *0.497

x1=date

color_1 = 'tab:blue'  
color_2 = 'tab:orange'
color_3 = 'tab:red'
color_4 = 'tab:green'
color_5 = 'tab:pink'


# pearson = np.corrcoef(y1,y2)


plt.xlabel('Date') 

plt.plot(x1, y1,marker='s', color=color_1,label='KOSPI(KS11)') 
plt.plot(x1, y2,marker='s', color=color_2,label='SEMI(091230)') 
plt.plot(x1, y3,marker='s', color=color_3,label='BATTERY(364960)') 
plt.plot(x1, y4,marker='s', color=color_4,label='BIO(244580)') 
plt.plot(x1, y5,marker='s', color=color_5,label='FINANCE(139270)') 

plt.legend()

plt.tick_params(axis='y', labelcolor=color_1)

#print(pearson)
plt.show()






