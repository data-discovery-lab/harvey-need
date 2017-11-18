
data_path = 'fra.txt'

lines = open(data_path).read().split('\n')

fInput = open("input.txt", "w+")
fOutput = open("output.txt", "w+")

inputTexts = []
outputTexts = []
for line in lines:

    if line == '' or len(line) < 1:
        continue

    input_text, target_text = line.split('\t')

    fInput.write(input_text + "\n")
    fOutput.write(target_text + "\n")

    #
    # inputTexts.append(input_text)
    # outputTexts.append(target_text)
#
# fInput.writelines(inputTexts)
# fOutput.writelines(outputTexts)

fInput.flush()
fOutput.flush()