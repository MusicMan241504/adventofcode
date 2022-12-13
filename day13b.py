def examineList(l,r):
    if type(l) == int and type(r) == int:
        if l < r:
            return True
        elif l > r:
            return False
        else:
            return None
    elif type(l) == list and type(r) == list:
        for i in range(min(len(l),len(r))):
            val = examineList(l[i],r[i])
            if not val == None:
                if not val:
                    return False
                else:
                    return True
        if len(l) < len(r):
            return True
        elif len(l) > len(r):
            return False
        else:
            return None
    else:
        if type(l) == int:
            return examineList([l],r)
        elif type(r) == int:
            return examineList(l,[r])
            

file = open('day13.txt')
lines = [line.strip() for line in file]
file.close()
i = 0
divIndex = [1,2]
while i < len(lines):
    if lines[i] != '':
        arr = eval(lines[i])
        if examineList(arr,[[6]]): #true if less than [[6]]
            divIndex[1] += 1
            if examineList(arr, [[2]]): #true if less than [[2]]
                divIndex[0] += 1
    i += 1
print(divIndex[0]*divIndex[1])
