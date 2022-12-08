file = open('day8.txt')
lines = [i.strip() for i in file.readlines()]
file.close()
trees = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        #check trees left of tree
        visible = True
        for k in range(j):
            if lines[i][k] >= lines[i][j]:
                visible = False
        if not visible:
            #check trees right of tree
            visible = True
            for k in range(j+1,len(lines[i])):
                if lines[i][k] >= lines[i][j]:
                    visible = False
            if not visible:
                #check trees above
                visible = True
                for k in range(i):
                    if lines[k][j] >= lines[i][j]:
                        visible = False
                if not visible:
                    #check trees bellow
                    visible = True
                    for k in range(i+1,len(lines)):
                        if lines[k][j] >= lines[i][j]:
                            visible = False
        if visible:
            trees = trees + 1
print(trees)
