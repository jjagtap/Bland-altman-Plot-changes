#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:14:12 2021

@author: m235103
"""

import sys
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
import numpy as np
import os
import pandas as pd
import pyCompare



"""Figure1: Reader1vsReader2"""

filename1='Reader1_Reader2_CTS.xlsx'
dfs1 = pd.read_excel(filename1, sheet_name='Sheet1', engine='openpyxl')
figname=os.path.join('mode23/','Reader1vsReader2_corr1109.png')

data11= dfs1['Reader1']#.tolist()
data11 = data11[~np.isnan(data11)]
data22= dfs1['AI-Prediction']#.tolist()
data22 = data22[~np.isnan(data22)]
df={"Reader1":data11,"Reader2":data22}

fig, ax = plt.subplots()
xlim = [0,14000]
ax.set_xlim(xlim)

sns.set(style="darkgrid",font_scale=1.1 )#
# color = sns.color_palette()[2]
Rsquare=stats.pearsonr(data11,data22)[0] ** 2
pvalue=stats.pearsonr(data11,data22)[1]
print(['Rsquare=',Rsquare,'pvalue=',pvalue])


g = sns.regplot(data11,data22, data=df, marker='o',color='black',scatter_kws={'s':25}, ax=ax,truncate=False,ci=95)
# g.axes.set_xlim(0, 2500); g.axes.set_ylim(0, 2500)#,color='k',height=10,ratio=3)
plt.xlabel("Reader1 (mL)", fontsize=15, fontweight='bold')
plt.ylabel("Reader2 (mL)", fontsize=15, fontweight='bold')#,
# import matplotlib.ticker as ticker
ax.set_ylim([0,15000])
ax.set_xlim([0,15000])
plt.xticks(fontsize=15, fontweight='normal'); plt.yticks(fontsize=15, fontweight='normal')
g.text(250,13000, 'p<0.0001', fontstyle='italic',size=15, fontweight='normal')#R square = 0.81, p < .5
g.text(70, 11000, 'Rsquare=0.81', fontstyle='italic',size=15, fontweight='normal')#R square = 0.81, p < .5

plt.tight_layout();plt.show()
fig1 = g.get_figure()
# fig1.savefig(figname, dpi=600)

# sys.exit("Exit message")

#%% Plot_ Bland Altman


# '''


"""Figure1: Reader1vsReader2 Train"""
# filename1='Similarity_metrics_HHvsAG.xlsx'
# dfs1 = pd.read_excel(filename1, sheet_name='updated 014', engine='openpyxl') #updated 014
figname=os.path.join('out/','Reader1vsReader2_blandAltman_1109.png')

# data11= dfs1['Reader1']#.tolist()
# data11 = data11[~np.isnan(data11)]
# data22= dfs1['Reader2']#.tolist()
# data22 = data22[~np.isnan(data22)]
# df={"Reader1":data11,"Reader2":data22}

# fig = plt.figure(figsize=(6,4))
# ax1 = fig.add_axes([0,0,1,1])

# figname=os.path.join('/.../modelOct2021/','Reader1vsReader2_1101.png')
# ax2=pyCompare.blandAltman(data11, data22,limitOfAgreement=1.96,confidenceInterval=95,confidenceIntervalMethod='approximate',percentage=True,
#                       detrend=None, pointColour='k')#,title='Bland-Altman Plot: Reader2 vs AI prediction',figureSize=(3.6,2.1),dpi=300,savePath=figname


fig = plt.figure(figsize=(6,4))
ax1 = fig.add_axes([0,0,1,1])

figname=os.path.join('/.../Manuscript/','Reader1vsReader2_1031.png')
ax2=pyCompare.blandAltman(data11, data22,limitOfAgreement=1.96,confidenceInterval=95,confidenceIntervalMethod='approximate',
                      detrend=None, percentage=True,
                      ax=ax1,pointColour='k')#title='Bland-Altman Plot: Reader2 vs AI prediction',figureSize=(3.6,2.1),dpi=300,savePath=figname
ax2.set_ylim([-100,100])
ax2.set_yticks(np.arange(-100, 110, 50))
ax2.set_ylabel('(Reader1-Reader2)/Mean %',fontdict=dict(weight='bold'))
ax2.set_xlabel('Means of Reader1 and Reader2', fontdict=dict(weight='bold'))
plt.rcParams.update({'font.size': 20})
# fig.savefig(figname,bbox_inches='tight',  dpi=300)#
plt.show()




# ax2.set_ylim([-100,100])
# ax2.set_yticks(np.arange(-100, 110, 50))
# ax2.set_ylabel('(Reader1-Reader2)/Mean %',fontdict=dict(weight='bold'))
# ax2.set_xlabel('Means of Reader1 and Reader2: Large dataset', fontdict=dict(weight='bold'))
# plt.rcParams.update({'font.size': 20})
# fig = ax2.get_figure()
# fig.savefig(figname,bbox_inches='tight',  dpi=300)#
# plt.show()
