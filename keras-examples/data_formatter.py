
sourceFile = "fra-eng/fra.txt"
destFile = "fra-eng/new.txt"

with open(sourceFile, "r") as source:

    f = open(destFile, "w+", encoding="utf-8")

    for line in source:
        input = []
        output = []
        line = line.split("\t")

        #Split input text
        for word in line[0].split(" "):
            input.append(word)
        #Split output text
        for word in line[1].split(" "):
            output.append(word)

        newLine = str(input) + "\t" + str(output) + "\n"
        f.write(newLine)


