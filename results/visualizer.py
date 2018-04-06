
##
##distance_files = {
##    'file1.out.txt': '#CCCCCC',
##    'file2.out.txt': '#FF00FF',
##    'file3.out.txt': '#DD00FF'
##}

#First part of tuple is prediction results
#Second part is true results
#Can use same true file for all input files.
#Dictionary value is the color for the graph.
distance_files = {
    ('input-vectors.testsample.txt','input-vectors.testtrue.txt') : '#33AA33',
    ('input-vectors.testsample2.txt','input-vectors.testtrue.txt') : '#AA3333'
}

def ReadVectorArray(rawLine):
    line = rawLine.split('[')[1].split(']')[0]
    vector = [int(val.strip()) for val in line.split(',')]
    return vector


import matplotlib.pyplot as plt
from scipy import spatial

for filePair in distance_files:
    #Get each line in the file.
    predictionVectors = []
    trueVectors = []
    with open(filePair[0], 'r') as source:
        for rawLine in source:
            predictionVectors.append(ReadVectorArray(rawLine))
    with open(filePair[1], 'r') as source2:
        for rawLine in source2:
            trueVectors.append(ReadVectorArray(rawLine))

    cosineList = []
    for i in range(0, min(len(predictionVectors), len(trueVectors))):
        similarity = 1 - spatial.distance.cosine(predictionVectors[i], trueVectors[i])
        cosineList.append(similarity)

    plt.plot(cosineList, color=distance_files[filePair])
    
plt.show()

