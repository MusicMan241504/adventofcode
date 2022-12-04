file = open('day4.txt')
count = 0
for line in file:
    a,b,c,d = line.replace(',','-').split('-')
    if a <= c and b >= d or c <= a and d >= b:
        count = count + 1
print(count)
file.close()
