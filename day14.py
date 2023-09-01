def printArr(arr):
    for y in range(len(arr[0])):
        for x in range(len(arr)):
            print(arr[x][y],end='')
        print()

def checkMov(arr,c):
    try:
        if arr[c[0]][c[1]+1] == '.':
            return [c[0],c[1]+1]
        if arr[c[0]-1][c[1]+1] == '.':
            return [c[0]-1,c[1]+1]
        if arr[c[0]+1][c[1]+1] == '.':
            return [c[0]+1,c[1]+1]
        return None
    except IndexError:
        return False

file = open('day14.txt')
lines = [line.strip() for line in file]
file.close()
minx = 500
maxx = 500
maxy = 0
for line in lines:
    coords = line.split(' -> ')
    for coord in coords:
        coord = coord.split(',')
        if int(coord[0]) < minx:
            minx = int(coord[0])
        if int(coord[0]) > maxx:
            maxx = int(coord[0])
        if int(coord[1]) > maxy:
            maxy = int(coord[1])
arr = [['.' for i in range(maxy+1)] for j in range(maxx-minx+1)]
arr[500-minx][0] = '+'
for line in lines:
    coords = line.split(' -> ')
    for i in range(len(coords)-1):
        l = [int(c) for c in coords[i].split(',')]
        r = [int(c) for c in coords[i+1].split(',')]
        if l[0] == r[0]: #if same x iterate through y
            for j in range(min(l[1],r[1]),max(r[1],l[1])+1):
                arr[l[0]-minx][j] = '#'
        if r[0] == r[0]: #if same y
            for j in range(min(l[0],r[0]),max(r[0],l[0])+1):
                arr[j-minx][l[1]] = '#'


#printArr(arr)

sand = [500-minx,0]
count = 0
falling = True
while falling:
    moving = True
    c = sand
    while c != None and c != False:
        preC = c
        c = checkMov(arr,c)
    if c == False:
        falling = False
        break

    arr[preC[0]][preC[1]] = 'o'
    count += 1
printArr(arr)
print(count)


