def move(h, t):
    #if touching
    if t[0] in [h[0]-1,h[0],h[0]+1] and t[1] in [h[1]-1,h[1],h[1]+1]:
        return t
    #change x
    if t[0] < h[0]:
        t[0] = t[0]+1
    elif t[0] > h[0]:
        t[0] = t[0]-1
    #change y
    if t[1] < h[1]:
        t[1] = t[1]+1
    elif t[1] > h[1]:
        t[1] = t[1]-1

    return t
file = open('day9.txt')
rope = []
for i in range(10):
    rope.append([0,0])
history = []
count = 0
for line in file:
    for i in range(int(line.split()[1])):
        match line.split()[0]:
            case 'U':
                rope[0][1] = rope[0][1]+1
            case 'D':
                rope[0][1] = rope[0][1]-1
            case 'L':
                rope[0][0] = rope[0][0]-1
            case 'R':
                rope[0][0] = rope[0][0]+1
        for i in range(9):
            rope[i+1] = move(rope[i],rope[i+1])
        if rope[9] not in history:
            count = count + 1
            history.append([rope[9][0],rope[9][1]])
print(count)
file.close()
