#Written by Nicholas Alvarez
#Contact me at nicholas.alvarez@ttu.edu for help using this.



#First part of tuple is prediction results
#Second part is true results, for verification
#Can use same true file for all input files.
#Dictionary value is the color for the graph.
#Follow this format with any number of input files.

#The 'trueFile' is the accurate versions for training.
trueFilePath = './output/vecter_output-weather-need.txt'
distance_files = {
    ('./output/vecter_output-n-gram-predicted-needs-1.txt',
         trueFilePath) : '#FF0000',
    ('./output/vecter_output-n-gram-predicted-needs-2.txt',
         trueFilePath) : '#00FF00',
    ('./output/vecter_output-n-gram-predicted-needs-3.txt',
         trueFilePath) : '#0000FF',
    ('./output/vecter_output-prediction-lstm-1.txt',
         trueFilePath) : '#000000',
    ('./output/vecter_output-prediction-lstm-2.txt',
         trueFilePath) : '#00FFFF',
    ('./output/vecter_output-seq-2-seq-needs.txt',
         trueFilePath) : '#FFFF00'
}

def ReadVectorArray(rawLine):
    if len(rawLine.split('[')) < 2:
        return "ERROR"
    line = rawLine.split('[')[1].split(']')[0]
    vector = [int(val.strip()) for val in line.split(',')]
    return vector


import matplotlib.pyplot as plt
import math
from scipy import spatial

for filePair in distance_files:
    #Get each line in the file.
    predictionVectors = []
    trueVectors = []
    #Open the prediction file and read its vectors
    with open(filePair[0], 'r') as source:
        x = 0
        for rawLine in source:
            x += 1
            vectorArray = ReadVectorArray(rawLine)
            if vectorArray == "ERROR":
                print("Bad input at line " + str(x) + " in file " + filePair[0])
                print("Ignoring...")
                #Append [0] so it can be nan'd later and ignored in the graph.
                predictionVectors.append([0])
            else:
                predictionVectors.append(vectorArray)
    #Open the true file and read its vectors.
    with open(filePair[1], 'r') as source2:
        x = 0
        for rawLine in source2:
            x += 1
            vectorArray = ReadVectorArray(rawLine)
            if vectorArray == "ERROR":
                print("Bad input at line " + str(x) + " in file " + filePair[1])
                print("Ignoring...")
                #Append [0] so it can be nan'd later and ignored in the graph.
                trueVectors.append([0])
            else:
                trueVectors.append(vectorArray)
            
    cosineList = []
    for i in range(0, min(len(predictionVectors), len(trueVectors))):
        #Default to the value being ignored.
        similarity = float('nan')
        if all(v == 0 for v in predictionVectors[i]):
            print("Line " + str(i+1) + " in file " + filePair[0] + " has a magnitude of 0!")
        elif all(v == 0 for v in trueVectors[i]):
            print("Line " + str(i+1) + " in file " + filePair[1] + " has a magnitude of 0!")
        else:
            #If it's not a magnitude 0, calculate the similarity!
            similarity = 1 - spatial.distance.cosine(predictionVectors[i], trueVectors[i])
        cosineList.append(similarity)

    plt.plot(cosineList, color=distance_files[filePair])

plt.title("Accuracy Visualization")
plt.show()

