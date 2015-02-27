# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 10:18:49 2015

@author: Ziqi
"""

import numpy as np
A = np.genfromtxt("C:\Users\Ziqi\Desktop\MODI_Matrix_IDWed.csv",delimiter=',',skiprows=1)

A = A[:,3:]
B = np.zeros([5,120])
B[B==0]=np.nan
C = np.zeros([10,120])
C[C==0]=np.nan
print A[1][3:] 
print B[0]
#%%
for i in range(0,10000):
    if A[i][0] == 1:
        B[0] = np.nanmean([B[0],A[i][3:]],axis=0)
    if A[i][0] == 2:
        B[1] = np.nanmean([B[1],A[i][3:]],axis=0)
    if A[i][0] == 3:
        B[2] = np.nanmean([B[2],A[i][3:]],axis=0)
    if A[i][0] == 4:
        B[3] = np.nanmean([B[3],A[i][3:]],axis=0)
    if A[i][0] == 5:
        B[4] = np.nanmean([B[4],A[i][3:]],axis=0)
        
    if A[i][1] == 1:
        C[0] = np.nanmean([C[0],A[i][3:]],axis=0)
    if A[i][1] == 2:
        C[1] = np.nanmean([C[1],A[i][3:]],axis=0)
    if A[i][1] == 3:
        C[2] = np.nanmean([C[2],A[i][3:]],axis=0)
    if A[i][1] == 4:
        C[3] = np.nanmean([C[3],A[i][3:]],axis=0)
    if A[i][1] == 5:
        C[4] = np.nanmean([C[4],A[i][3:]],axis=0)
    if A[i][1] == 201:
        C[5] = np.nanmean([C[0],A[i][3:]],axis=0)
    if A[i][1] == 202:
        C[6] = np.nanmean([C[1],A[i][3:]],axis=0)
    if A[i][1] == 203:
        C[7] = np.nanmean([C[2],A[i][3:]],axis=0)
    if A[i][1] == 204:
        C[8] = np.nanmean([C[3],A[i][3:]],axis=0)
    if A[i][1] == 205:
        C[9] = np.nanmean([C[4],A[i][3:]],axis=0)
        
print B
#np.savetxt("C:\Users\Ziqi\Desktop\ddda.csv", B, delimiter=",",fmt='%.2f')
np.savetxt("C:\Users\Ziqi\Desktop\ccc.csv", C, delimiter=",",fmt='%.2f')