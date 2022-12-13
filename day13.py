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
pairs = []
while i < len(lines)-1:
    l = eval(lines[i])
    r = eval(lines[i+1])
    ordered = examineList(l,r)
    if ordered:
        pairs.append((i+3)/3)
    i += 3
total = 0
for pair in pairs:
    total += pair
print(total)
