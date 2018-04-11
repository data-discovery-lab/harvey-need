import ast
import collections

files = [
    # 'output/n-gram-predicted-needs-1.vec.txt',
    # 'output/prediction-lstm-1.vec.txt',
    # 'output/seq-2-seq-needs.vec.txt',
    # 'output/weather-need.vec.txt',
    # 'output/testing-seq-2-seq-r01.vec.txt',

]

need_size = 50
half_day = False

for file in files:
    my_data = dict()
    with open(file) as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.strip()

            if len(line) < 10:
                continue
            date = line[0:10]
            time = line[11:13]
            time = int(time)

            if half_day:
                if time >= 12:
                    date = date + '-02'
                else:
                    date = date + '-01'

            if date not in my_data:
                my_data[date] = []
                for i in range(need_size):
                    my_data[date].append(0)

            my_needs = my_data[date]

            coming_needs = line[line.index('['):]
            coming_needs = ast.literal_eval(coming_needs)
            if len(coming_needs) != len(my_needs):
                for i in range(len(my_needs), len(coming_needs)):
                    my_needs.append(0)

            for i in range(need_size):
                my_needs[i] = my_needs[i] | coming_needs[i]

    my_data = collections.OrderedDict(sorted(my_data.items()))

    if half_day:
        output = file.replace('.vec', '-half-day.vec')
    else:
        output = file.replace('.vec', '-full-day.vec')

    with open(output, 'w') as writer:
        for time, needs in my_data.items():
            need_string = '['
            for n in needs:
                need_string = need_string + str(n) + ', '

            need_string = need_string.rstrip()
            need_string = need_string.rstrip(',')

            need_string += ']'

            writer.write(time + ' ' + need_string + '\n')

print('done')