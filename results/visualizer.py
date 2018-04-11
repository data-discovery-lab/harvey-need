import matplotlib.pyplot as plt
import math
from scipy import spatial
from ast import literal_eval
from sklearn.metrics import jaccard_similarity_score
import numpy as np


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Bar
from plotly import tools

tools.set_credentials_file(username='evanwilson', api_key='XVhzaBtJIMl1bjUZj0zo')


from scipy.interpolate import spline

def PlotStuff(dataToPlot, dataName, dataColor):

    #Currently limiting to 2 decimal places to make prettier.
    dataToPlot = [round(x*100)/100 for x in dataToPlot]

    #Smoothed? Remove and uncomment other lines to return to prior format.
    #The last value is the smoothing factor. Sweet spot for working hoverover uncertain.
    #xnew = np.linspace(0, len(dataToPlot)-1, len(dataToPlot) * 11)
    #smoothedY = spline(np.arange(len(dataToPlot)), dataToPlot, xnew)
    #smoothedX = spline(np.arange(len(dataToPlot)), np.arange(len(dataToPlot)), xnew)
    
    dataPlot = Scatter(
        x = np.arange(len(dataToPlot)),#smoothedX,
        y = dataToPlot,#smoothedY,
        name = dataName,
        line = dict(
            color = dataColor,
            width = 4
            ),
        marker = dict(
            symbol = 'triangle-up',
            size = 17
            )
        )
    return dataPlot









true_file = 'output/weather-need-full-day.vec.txt'
files = {
    'output/n-gram-predicted-needs-1-full-day.vec.txt': '#FF0000',
    'output/prediction-lstm-1-full-day.vec.txt': '#00FF00',
    'output/testing-seq-2-seq-r01-full-day.vec.txt': '#0000FF'

    # 'output/n-gram-predicted-needs-1.vec.txt': '#FF0000',
    # 'output/prediction-lstm-1.vec.txt': '#00FF00',
    # 'output/seq-2-seq-needs.vec.txt': '#0000FF'
}


f = open(true_file)
lines = f.readlines()

trueVector = []

plotData = []

for file, color in files.items():

    with open(file) as myFile:
        similarity_scores = []
        for i, line in enumerate(myFile):
            line = line.replace('\n', '')
            line = line.strip()
            if len(line) < 10:
                continue

            vector_string = line[line.index('['):]
            compared_vector = literal_eval(vector_string)

            # setup true vector for comparison. This is all 1(s) vector
            test_text = line[0:15]
            true_line = lines[i]
            if not true_line.startswith(test_text):
                raise Exception('Invalid line at:', i, 'is:', true_line, ':test_text:', test_text)

            vector_string = true_line[true_line.index('['):]
            trueVector = literal_eval(vector_string)
            if len(trueVector) != len(compared_vector):
                for i in range(len(trueVector), len(compared_vector)):
                    trueVector.append(1)

            similarity = jaccard_similarity_score(compared_vector, trueVector)
            similarity_scores.append(similarity)

        print('average:', file, np.average(similarity_scores))
        #Nick: Adjustments here ------------------------------------
        plotData.append(PlotStuff(similarity_scores, file, color))
        #Create smoothing effect.
        #xnew = np.linspace(0, len(similarity_scores)-1, 100)
        #smooth = spline(np.arange(len(similarity_scores)), similarity_scores, xnew)
        #Plot the smoothed line...
        #plt.plot(xnew, smooth, color=color)
        #Plot the original, transparently.
        #plt.plot(similarity_scores, color=color + "22")

#plt.title("Accuracy Visualization")
#plt.yticks(np.arange(0, 1.1, step=0.1))
#plt.show()

layout = dict(
    xaxis = dict(
        title = 'X Axis Label',
        ),
    yaxis = dict(
        title = 'Accuracy',
        range = [0, 1]
        ),
    legend = dict(
        #x = 0,
        #y = 1.0,
        bgcolor = 'rgba(255, 255, 255, 0)',
        bordercolor = 'rgb(0, 0, 0)',
        borderwidth = 1#,
        #orientation = 'h'
        )
    )


fig = dict(data=plotData, layout=layout)
plot(fig, filename='line-graph-test.html')








