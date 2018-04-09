import matplotlib.pyplot as plt
import math
from scipy import spatial
from ast import literal_eval
from sklearn.metrics import jaccard_similarity_score
import numpy as np

true_file = 'output/weather-need-half-day.vec.txt'
files = {
    'output/n-gram-predicted-needs-1-half-day.vec.txt': '#FF0000',
    'output/prediction-lstm-1-half-day.vec.txt': '#00FF00',
    'output/seq-2-seq-needs-half-day.vec.txt': '#0000FF'

    # 'output/n-gram-predicted-needs-1.vec.txt': '#FF0000',
    # 'output/prediction-lstm-1.vec.txt': '#00FF00',
    # 'output/seq-2-seq-needs.vec.txt': '#0000FF'
}


f = open(true_file)
lines = f.readlines()

trueVector = []

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

            similarity = jaccard_similarity_score(compared_vector, trueVector)
            similarity_scores.append(similarity)

        print('average:', file, np.average(similarity_scores))
        plt.plot(similarity_scores, color=color)

plt.title("Accuracy Visualization")
plt.show()

