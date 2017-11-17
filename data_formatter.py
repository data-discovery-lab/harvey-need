
sourceFile = "/home/jstuve/Documents/harvey_data/08_17.csv"
destFile = "/home/jstuve/GitProj/harvey-need/topic-modeling/08_17.txt"


with open(sourceFile, "r") as source:

    f = open(destFile, "w+", encoding="utf-8")

    for line in source:
        input = []
        output = []
        line = line.split("|")

        f.write(line[0] + '\n')


