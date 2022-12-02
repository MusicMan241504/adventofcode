file = open("day2.txt")
score = 0
for line in file:
    if line.find('A X') != -1:
        score = score + 1+3
    elif line.find('B X') != -1:
        score = score + 1+0
    elif line.find('C X') != -1:
        score = score + 1+6

    elif line.find('A Y') != -1:
        score = score + 2+6
    elif line.find('B Y') != -1:
        score = score + 2+3
    elif line.find('C Y') != -1:
        score = score + 2+0

    elif line.find('A Z') != -1:
        score = score + 3+0
    elif line.find('B Z') != -1:
        score = score + 3+6
    elif line.find('C Z') != -1:
        score = score + 3+3

print(score)

