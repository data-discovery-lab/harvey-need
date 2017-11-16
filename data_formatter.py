
sourceFile = "/home/jstuve/GitProj/harvey-need/input.csv"
destFile = "/home/jstuve/GitProj/harvey-need/topic-modeling/tweets.txt"

with open(sourceFile, "r") as source:

    f = open(destFile, "w+", encoding="utf-8")

    for line in source:
        input = []
        output = []
        line = line.split("|")

        f.write(line[0] + '\n')


