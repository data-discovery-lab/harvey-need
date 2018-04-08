#Convert tweeter text data into vector, by Yong Wu 04/06/2018
#All input and output files should be .txt format
#If lenth of vocabulary is not 50, this code should be modified a little bit
#File names of the input and output files should be edited within this code

vector_file = open('needs-voc.txt') #input vocabulary
vector_model=[] #setup vocabulary vector
base_vector = {}
for line in vector_file:
    line = line.rstrip() #get rid of newline char at the end of each line
    if len(line) > 2:
        base_vector[line] = len(vector_model)
        vector_model.append(line)


file_name = 'seq-2-seq-needs.txt'
file_output = open('output/' + file_name.replace('.txt', '.vec.txt'), 'w') #output vectors
data_file = open(file_name) #input text data

count = 0
output_content = []
output_line = []

for line in data_file: #parse each line in the input file

    if not line.startswith('Decoded sentence:') and not line.startswith('Input sentence:'):
        continue

    line = line.replace('\n', '')
    if line.startswith('Input sentence:'):
        output_line = []
        output_line.append(line[(2 + line.index(':')):])
        continue
    # initialize a zero vector
    output_vector = []
    for i in range(len(vector_model)):
        output_vector.append('0')


    needs = line[line.index(':') + 1:]

    needs = needs.split(' ')
    for n in needs:
        n = n.strip()
        if len(n) < 2:
            continue
        idx = base_vector[n]
        output_vector[idx] = '1'

    # write output vector into output file
    output_vector_string = ', '.join(output_vector)
    output_line.append('[' + output_vector_string + ']')
    file_output.write(' '.join(output_line) + '\n')

#close input and output files
file_output.close()
data_file.close()
vector_file.close()

    
