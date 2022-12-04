file = open('day4.txt')
count = 0
for line in file:
    found = False
    a,b,c,d = [int(i) for i in line.replace(',','-').split('-')]
    for i in range(a,b+1):
        if i >= c and i <= d:
            found = True
    if found:
        count = count + 1
print(count)
file.close()
