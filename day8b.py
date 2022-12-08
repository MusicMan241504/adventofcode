file = open('day8.txt')
lines = [i.strip() for i in file.readlines()]
file.close()
trees = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        #check trees left of tree
        scores = [0,0,0,0]
        for k in range(j):
            scores[0] = k+1
            if lines[i][j-k-1] >= lines[i][j]:
                break
        #check trees right of tree
        for k in range(len(lines[i])-j-1):
            scores[1] = k+1
            if lines[i][j+k+1] >= lines[i][j]:
                break
        #check trees above
        for k in range(i):
            scores[2] = k+1
            if lines[i-k-1][j] >= lines[i][j]:
                break
        #check trees bellow
        for k in range(len(lines)-i-1):
            scores[3] = k+1
            if lines[i+k+1][j] >= lines[i][j]:
                break
        total = 1
        for score in scores:
            total = total * score
        if total > trees:
            trees = total
print(trees)
