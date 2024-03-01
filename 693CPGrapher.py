# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:11:02 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format

#same general layout as Nyquist grapher. Make sure to replace my file path with your own.

def CP_grapher(filenames,title,xlimits,ylimits,txt,legend,gridlines,xlabel,ylabel,xcolumn,
                   ycolumn,cutoff,const): #txt is true if dealing with a txt file, and false if dealing with a csv
    #xlimits and ylimits set custom limits. Set to None if you want autoscaling.
    #legend is True if there is a legend.
    #gridlines is True if there are gridlines
    #xcolumn and ycolumn specify the columns which hold the relevant data

    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 

    ax.set_ylabel(ylabel)   # set the label of the x-axis
    ax.set_xlabel(xlabel) # set the label of the y-axis
    
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    X6 = []
    X7 = []
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    Y5 = []
    Y6 = []
    Y7 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]

    i=0
    

    while(i < len(filenames)):
        if txt == False:
            datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 2/" + filenames[i] + ".csv", skiprows=1, unpack=True,delimiter=',',
                                                     usecols=(xcolumn,ycolumn))

        elif txt == True:
            datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Echem Project/Data/txt files/3 cycles/" + filenames[i] + ".txt", skiprows=1, unpack=True
                ,usecols=(xcolumn,ycolumn))
        
        if cutoff == None:
            cutoff = len(datalistX[i])
        ax.plot((datalistX[i][0:cutoff]-datalistX[i][0])/const, (datalistY[i][0:cutoff]), '.', color=colorlist[i],label=filenames[i])
        #normalizes time and reports voltage absolute value
        average_value = np.average(datalistY[i][0:cutoff])
        max_time = np.max(datalistX[i][cutoff])
        
        i = i + 1
        
    
    # make a plot 'ax', with markers and lines, color=red
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
    #ax.set_xlabel('Potential, V')   # set the label of the x-axis
    #ax.set_ylabel('Current, mA/cm^2') # set the label of the y-axis
    if legend == True:
        ax.legend(loc='upper left')       # place the legend at the 'upper left'
    if gridlines == True:
        ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
        ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    if title != None:
        ax.set_title(title)

    plt.show()   # display 'ax'
    print(average_value)
    print(max_time)
    if cutoff != None:
        print(datalistX[i-1][cutoff])