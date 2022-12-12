from collections import deque
file = open('day12.txt')
lines = [line.strip() for line in file]
file.close()

def printGrid(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i].d,end=' ')
        print()


#class to store coordinates
class Coord:
    def __init__(self,x,y,val):
        self.x = x
        self.y = y
        self.val = val
        self.col = 2#white
        self.d = None
        self.pre = None

grid = [[0 for i in range(len(lines))] for j in range(len(lines[0]))]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[j][i] = Coord(j,i,ord(lines[i][j])-ord('a'))# a = 0, z = 25
        if grid[j][i].val == -14:#S
            grid[j][i].val = 0
            start = grid[j][i]
        if grid[j][i].val == -28:#E
            grid[j][i].val = 25
            end = grid[j][i]

start.col = 1
start.d = 0




q = deque([start])
while q:
    u = q.popleft()
    coords = []
    for mov in [[0,1],[1,0],[0,-1],[-1,0]]:
        #check item exists
        if u.x+mov[0] < len(grid) and u.y+mov[1] < len(grid[u.y+mov[0]]) and u.x+mov[0] >= 0 and u.y+mov[1] >= 0:
            #check if possible path
            v = grid[u.x+mov[0]][u.y+mov[1]]
            if v.val <= u.val+1:
                coords.append(v)
    for v in coords:
        if v.col == 2:
            v.col = 1
            v.d = u.d + 1
            v.pre = u
            q.append(v)
    u.col = 0

#printGrid(grid)
print(end.d)
