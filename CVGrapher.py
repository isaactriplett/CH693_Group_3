# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 00:26:53 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format

#same general layout as Nyquist grapher. Make sure to replace my file path with your own.

def CV_grapher(const #Normalizing constant to turn current input into current density output if desired
               ,filenames,title,xlimits,yunits,ylimits,txt,currentDependence,xcolumn,ycolumn,legend,gridlines): #txt is true if dealing with a txt file, and false if dealing with a csv
#currentDependence: True if current is on the y axis.    

    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    if currentDependence == True:
        ax.set_ylabel('Current ' + yunits)
        ax.set_xlabel('Potential (V)')
    else:
        ax.set_ylabel('Potential (V)')   # set the label of the x-axis
        ax.set_xlabel('Current ' + yunits) # set the label of the y-axis
    
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
            if currentDependence == True:
                datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 2/" + filenames[i] + ".csv", skiprows=1, unpack=True,delimiter=',',
                                                     usecols=(xcolumn,ycolumn))
            else:
                datalistY[i],datalistX[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 1/Data/CH693 Project 1 Week 1/CH693 Project 1 Week 1/" + filenames[i] + ".csv", skiprows=1, unpack=True,
                                                     delimiter=',',usecols=(xcolumn,ycolumn))
        elif txt == True:
            if currentDependence == True:
                datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 2/Nafion Data/" + filenames[i] + ".txt", skiprows=1, unpack=True,
                                                     usecols=(0,1))
            else:
                datalistY[i],datalistX[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Echem Project/Data/txt files/Week 3/" + filenames[i] + ".txt", skiprows=1, unpack=True,
                                                     usecols=(0,1))
        ax.plot(datalistX[i], datalistY[i]/const, '.', color=colorlist[i],label=filenames[i])
        i = i + 1
        
    #fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    #ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    # subplot(abc): divide 'fig' into a (row)* b (column) sub-plots, 'ax' will be at the c-th sub-panel.
    #ax.plot(data_X, data_Y/0.0314159265358, '.', color='r')  
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