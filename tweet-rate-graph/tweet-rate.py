#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:40:52 2017

@author: joshuastuve
"""
import sys
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('JStuve', 'mVRUE6CCF94yvNnRxeuu') # Replace the username, and API key with your credentials.

if(len(sys.argv) != 2):
    print('Please enter file name:\n $python tweet-rate.py data.csv')

else:
    print("Processing Data")
    xData = []
    yData = []
    
    with open(sys.argv[1], 'r', encoding='utf8', errors='ignore') as dataFile:
        for line in dataFile:
            line = line.split(" ")
            xData.append(line[0])
            yData.append(line[2])
                    
    
    trace1 = go.Scatter(
        x= xData,
        y= yData,
        fill='tozeroy'
    )
    
    
    data = [trace1]
    
    layout = dict(
            width = 900,
            heigth = 900,
            xaxis = dict(
                showgrid = False,
                zeroline=True,
                showline=True,
                title = "Date",
                titlefont = dict(
                        size = 20,
                        color = "#000"
                ),
                tickfont = dict(
                        size = 14,
                        color = "#000"
                ),
                dtick=30,
                        
            ),
            yaxis = dict(
                showgrid = False,
                zeroline = True,
                showline=True,
                title = "Tweets per Second",
                titlefont = dict(
                        size = 20,
                        color = "#000"
                ),
                tickfont = dict(
                        size = 14,
                        color = "#000"
                ),
            ),
        )
    print("Creating Plotly Graph")
    fig = dict(data=data, layout=layout)
    py.image.save_as(fig, filename='TweetRate.png')
    print("Graph Completed\nLook for 'TweetRate.png'")