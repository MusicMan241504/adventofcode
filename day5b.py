file = open('day5.txt')
a1 = ['S','T','H','F','W','R']
a2 = ['S','G','D','Q','W']
a3 = ['B','T','W']
a4 = ['D','R','W','T','N','Q','Z','J']
a5 = ['F','B','H','G','L','V','T','Z']
a6 = ['L','P','T','C','V','B','S','G']
a7 = ['Z','B','R','T','W','G','P']
a8 = ['N','G','M','T','C','J','R']
a9 = ['L','G','B','W']
array = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
for line in file:
    tmp = line.split()
    q = int(tmp[1])
    f = int(tmp[3])
    t = int(tmp[5])
    tmp = array[f-1][-q:]
    array[f-1] = array[f-1][:-q]
    array[t-1] = array[t-1] + tmp
boxes = ''
for stack in array:
    boxes = boxes + stack[-1]
print(boxes)
file.close()
