# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:52:48 2024

@author: isaac
"""

import numpy as np

def avg_abs_I(filename, Vrange):
    dataX,dataY=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 2/Nafion Data/" + filename + '.txt', skiprows=1, unpack=True,
                   usecols=(0,1))
    Itotal = 0
    count = 0
    i = 0
    while (i < len(dataX)):
        if dataX[i] > Vrange[0] and dataX[i] < Vrange[1]:
            
            if dataY[i] > 0:
                Itotal = Itotal + dataY[i]
                count = count + 1
            
        i = i + 1
    avgabsI = Itotal/count
    return avgabsI/1000

def charge_integrator(filename, Vrange, desorption, scan_rate, DLI,scans): #scan_rate in V/s! DLI - Average double layer current
    # returns charge in Coulombs
    dataX,dataY=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 2/Nafion Data/" + filename + '.txt', skiprows=1, unpack=True,
                   usecols=(0,1))
    
    V1 = np.array([])
    I1 = np.array([])
    Q = 0
    
    i = 0
    while (i < len(dataX)):
        if dataX[i] > Vrange[0] and dataX[i] < Vrange[1]:
            V1 = np.append(V1, dataX[i])
            I1 = np.append(I1, dataY[i]/1000)
        i = i + 1
    
    i = 0
    
    V2 = []
    I2 = []
    
    if desorption == True:
        DLI1 = DLI
        while (i < len(I1)):
            if I1[i] > DLI1:
                V2 = np.append(V2,V1[i])
                I2 = np.append(I2,I1[i])
            i = i + 1
    else:
        DLI1 = - DLI
        while (i < len(I1)):
            if I1[i] < DLI1:
                V2 = np.append(V2,V1[i])
                I2 = np.append(I2,I1[i])
            i = i + 1
    
    i = 1
    
    while (i < len(V2)):
        Q = Q + ((I2[i]- DLI1 )*(np.abs(V2[i]-V2[i-1]))/scan_rate)
        i = i + 1
    
    return Q/scans
