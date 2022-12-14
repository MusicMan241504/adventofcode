import string
letters = string.ascii_letters
file = open('day3.txt')
total = 0
for line in file:
    text = line.strip()
    l = text[:int(len(text)/2)]
    r = text[int(len(text)/2):]
    for char in l:
        if char in r:
            total = total + letters.find(char)+1
            break
print(total)
file.close()
