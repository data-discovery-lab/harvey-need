#Convert tweeter text data into vector, by Yong Wu 04/06/2018
#All input and output files should be .txt format
#If lenth of vocabulary is not 50, this code should be modified a little bit
#File names of the input and output files should be edited within this code

vector_file = open('needs-voc.txt') #input vocabulary
vector_model=[] #setup vocabulary vector
for line in vector_file:
    line = line.rstrip() #get rid of newline char at the end of each line
    vector_model.append(line)
    
vecter_output = open('vecter_output.txt', 'w') #output vectors
data_file = open('prediction-lstm-2.txt') #input text data

count = 0
for line in data_file: #parse each line in the input file
    count=count+1
    line = line.rstrip() #get rid of newline char at the end of each line
    split_line = line.split(' ') #get rid of whitespace

    if count%4==1:
       vecter_output.write( str(" ".join(split_line[4:9]))+': ')
    if count%4==3:
       vector_out=[]  #initialize output vector of a line of tweeter text data
       for index in range(50): #compare words with vocabulary list
          if vector_model[index] in split_line:
             vector_out.append(1)
          else:
             vector_out.append(0)
       vecter_output.write( str(vector_out)+'\n')


    #write output vector into output file
    #vecter_output.write( str(" ".join(split_line[4:8]))+': '+str(vector_out)+'\n')

#close input and output files
vecter_output.close()
data_file.close()
vector_file.close()

    
