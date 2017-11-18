
data_path = 'need.csv'

lines = open(data_path).read().split('\n')

input_sequences = []
input_line = ''

fInput = open("need_input.txt", "w+")
fOutput = open("need_output.txt", "w+")

day_map ={
    'aug-17': 'day1',
    'aug-18': 'day2',
    'aug-19': 'day3',
    'aug-20': 'day4',
    'aug-21': 'day5',
    'aug-22': 'day6',
    'aug-23': 'day7',
    'aug-24': 'day8',
    'aug-25': 'day9',
    'aug-26': 'day10',
    'aug-27': 'day11',
    'aug-28': 'day12',
    'aug-29': 'day13',
    'aug-30': 'day14',
    'aug-31': 'day15',
    'sep-01': 'day16',
    'sep-02': 'day17',
}

line_pos = 0
for line in lines:
    if line == '' or len(line) < 1:
        continue

    my_inputs = line.split("|")
    input_seq = []
    pos = 0
    line_pos = line_pos + 1

    for ip in my_inputs:
        ip = ip.strip('"').lower()
        pos = pos + 1
        if pos < 2 or pos == 7:
            ip = ip.replace(" ", "-")
        if pos == 3 or pos == 4:
            continue

        if pos < 2:
            ip = day_map[ip]

        input_seq.append(ip)

    my_output_line = input_seq.pop()

    print("line", line_pos, '=', len(my_output_line.split()))

    my_input_line = ' '.join(input_seq)
    fInput.write(my_input_line + '\n')
    fOutput.write(my_output_line + '\n')

fInput.flush()
fOutput.flush()