# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:16:57 2022

@author: GIGABYTE
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import numpy as np
from matplotlib.font_manager import FontProperties  # 步骤一

font = FontProperties(fname=r"C:/simsun.ttc", size=14)  


df = pd.read_csv('C:/Users/GIGABYTE/Downloads/出國旅遊資料.txt')
df.head(11)
colors = dict(zip(
    ["香港", "中國大陸", "日本", "南韓", "馬來西亞", "新加坡", "印尼","菲律賓","泰國","越南","加拿大","美國","法國","德國","義大利","荷蘭","英國","澳大利亞","南非",'澳門'],
    ["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff",
     "#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75']
))
fig, ax = plt.subplots(figsize=(16, 9))

def race_barchart(input_year):
    dff = df[df['date'].eq(input_year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()

    ax.barh(dff['country'], dff['value'], color=[colors[x] for x in dff['country']],height=0.8)
    dx = dff['value'].max() / 200
    
    for i, (value, name) in enumerate(zip(dff['value'], dff['country'])):
        ax.text(0, i,name+' ',size=16, weight=600, ha='right', va='center', fontproperties=font)
        ax.text(value+dx, i,f'{value:,.0f}',  size=16, ha='left',  va='center')
            
    ax.text(0.9, 0.2, input_year[:7].replace('-','/'), transform=ax.transAxes, color='#777777', size=72, ha='right', weight=1000, fontproperties=font)
    ax.text(0, 1.06, '旅遊人數 (thousands)', transform=ax.transAxes, size=14, color='#777777', fontproperties=font)
    ax.text(0.59, 0.14, '總觀光人數:'+str(int(dff['value'].sum())), transform=ax.transAxes, size=24, color='#000000',ha='left', fontproperties=font)
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.xaxis.set_ticks_position('top')
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.text(0, 1.15, '台灣赴各國觀光人數',
                transform=ax.transAxes, size=24, weight=600, ha='left', va='top', fontproperties=font)

    plt.box(False)
    
race_barchart('2019-10-01')



#整理Frame數
month = list(set(df.date.values))
month.sort()

fig, ax = plt.subplots(figsize=(16, 9))
animator = animation.FuncAnimation(fig, race_barchart, frames=month)


animator.save("C:/Users/GIGABYTE/Downloads/出國旅遊資料.gif",writer='imagemagick', fps=3)