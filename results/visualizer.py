import matplotlib.pyplot as plt
import math
from scipy import spatial
from ast import literal_eval

files = {
    'output/n-gram-predicted-needs-1.vec.txt': '#FF0000',
    'output/prediction-lstm-1.vec.txt': '#00FF00',
    'output/seq-2-seq-needs.vec.txt': '#00FF00'
}


trueVector = []

for file, color in files.items():

    with open(file) as myFile:
        cosineList = []
        for line in myFile:
            line = line.replace('\n', '')
            line = line.strip()
            if len(line) < 10:
                continue
            vector_string = line[line.index('['):]
            compared_vector = literal_eval(vector_string)

            if len(trueVector) != len(compared_vector):
                trueVector = []
                for i in range(len(compared_vector)):
                    trueVector.append(1)

            similarity = 1 - spatial.distance.cosine(compared_vector[i], trueVector[i])
            cosineList.append(similarity)

        plt.plot(cosineList, color=color)

plt.title("Accuracy Visualization")
plt.show()

