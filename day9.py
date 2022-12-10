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
h, t = [0,0], [0,0]
history = []
count = 0
for line in file:
    for i in range(int(line.split()[1])):
        match line.split()[0]:
            case 'U':
                h[1] = h[1]+1
            case 'D':
                h[1] = h[1]-1
            case 'L':
                h[0] = h[0]-1
            case 'R':
                h[0] = h[0]+1
        t = move(h,t)
        if t not in history:
            count = count + 1
            history.append([t[0],t[1]])
print(count)
file.close()
