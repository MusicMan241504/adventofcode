file = open("day1.txt")
n = 1
big_n = 0
big_total = 0
total = 0
totals = []
for line in file:
    if line != '\n':
        total = total + int(line)

    else:
        if total > big_total:
            big_total = total
            big_n = n
        totals.append(total)
        total = 0
        n = n + 1
#print(big_total)
#print(big_n)
totals.sort()
print(totals)
l = len(totals)
print(totals[l-1]+totals[l-2]+totals[l-3])
