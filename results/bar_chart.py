#To use: plug in data into the dictionary.
#Then plug in colors as directed here:
#https://matplotlib.org/api/colors_api.html
#Run and go.

import matplotlib.pyplot as plt
import numpy as np

#Dictionary is Label: Value
Data = {
    "Seq. to seq.": 0.846,
    "LSTM": 0.824,
    "N-Gram": 0.719
}
Colors = ['r', 'g', 'b']

x = 0
for value in Data.values():
    plt.bar(x, value, align='center', color=Colors[x], alpha=1)
    x += 1
    if x > len(Colors): x = 0


plt.xticks(np.arange(len(Data.keys())), Data)
plt.yticks(np.arange(0, 1.1, 0.1))

#LABELS HERE
plt.ylabel('Accuracy')
plt.title('Various method accuracies')

plt.show()

