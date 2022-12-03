import string
letters = string.ascii_letters
file = open('day3.txt')
total = 0
line3 = True
while line3 != '':
    line1 = file.readline().strip()
    line2 = file.readline().strip()
    line3 = file.readline().strip()
    for char in line1:
        if char in line2 and char in line3:
            total = total + letters.find(char)+1
            break
print(total)
file.close()
