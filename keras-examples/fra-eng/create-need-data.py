
data_path = 'need.csv'

lines = open(data_path).read().split('\n')

input_sequences = []
input_line = ''

fInput = open("need_input.txt", "w+")
fOutput = open("need_output.txt", "w+")

for line in lines:

    my_inputs = line.split("|")
    input_seq = []
    pos = 0
    for ip in my_inputs:
        ip = ip.strip('"').lower()
        pos = pos + 1
        if pos < 2 or pos == 7:
            ip = ip.replace(" ", "-")

        input_seq.append(ip)

    my_output_line = input_seq.pop()

    my_input_line = ' '.join(input_seq)
    fInput.write(my_input_line + '\n')
    fOutput.write(my_output_line + '\n')

fInput.flush()
fOutput.flush()