file = open('day10.txt')
cmds = [line.strip() for line in file]
file.close()
cycle = 1
process_finish = 1
i = 0
x = 1
crt = 0
cycle_check = [40*n for n in range(7)]
line = ''
lines = []
#CPU clock
while cycle <= cycle_check[6]:
    if process_finish == cycle:
        if i > 0 and cmds[i-1].split()[0] == "addx":
            x = x + int(cmds[i-1].split()[1])
        if cmds[i] == "noop":
            process_finish = cycle + 1
        if cmds[i].split()[0] == "addx":
            process_finish = cycle + 2
        i = i + 1
    if crt in [x-1,x,x+1]:
        line = line + '#'
    else:
        line = line + '.'
    if cycle in cycle_check:
        lines.append(line)
        line = ''
        crt = -1
    cycle = cycle + 1
    crt = crt + 1
for i in lines:
    print(i)
