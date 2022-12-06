file = open('day6.txt')
text = file.readline()
count = 1
nums = []
for i in range(4,len(text)):
    tmp = text[i-4:i]
    found = False
    for char in tmp:
        if tmp.find(char) != tmp.rfind(char):
            found = True
    if not found:
        nums.append(i)
print(nums[0])
file.close()
