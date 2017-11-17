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

print(sys.argv)

if(len(sys.argv) != 3):
    print('Please enter file name:\n $python tweet-rate.py CompleteTweetData.csv NeedTweeData.csv')



else:
    print("Processing Data")
    xData = []
    yData = []
    
    xxData = []
    yyData = []

    # Complete Tweets
    with open(sys.argv[1], 'r') as dataFile:
        for line in dataFile:
            line = line.split("|")
            xData.append(line[0])
            yData.append(line[2])

    # Need Tweets
    with open(sys.argv[2], 'r') as dataFile:
        for line in dataFile:
            line = line.split("|")
            xxData.append(line[0])
            yyData.append(line[2])
            
    labels = []
    
    for line in xData:
        split = line.split('_')
        line = "{}/{}".format(split[0], split[1])   
        labels.append(line)
        
    x = len(labels)
    
    trace1 = go.Scatter(
        x= xData,
        y= yData,
        fill='tozeroy',
        name="Harvey Tweets"
    )
    
    trace2 = go.Scatter(
        x= xxData,
        y= yyData,
        fill='tozeroy',
        name="Need Tweets"
    )
    
    
    data = [trace1, trace2]
    
    print("X_Length: " + str(len(xData)))
    
    layout = dict(
            width = 900,
            heigth = 900,
            legend = dict(
                x = .75,
                y = 1                    
            ),
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
                tickvals= [10,40,70,100,130,160,190,220,250],
                ticktext= ["Aug 17","Aug 22","Aug 27","Sept 1", "Sept 6", "Sept 11", "Sept 16", "Sept 21", "Sept 26"],
                tickwidth=2,
                tickangle=35,
                dtick=30,
                        
            ),
            yaxis = dict(
                showgrid = False,
                zeroline = True,
                showline=True,
                title = "Tweet Rate (per second)",
                titlefont = dict(
                        size = 20,
                        color = "#000"
                ),
                tickfont = dict(
                        size = 14,
                        color = "#000"
                ),
                tickwidth=2,
            ),
        )
    print("Creating Plotly Graph")
    fig = dict(data=data, layout=layout)
    py.image.save_as(fig, filename='TweetRate.png')
    print("Graph Completed\nLook for 'TweetRate.png'")