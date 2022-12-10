file = open('day10.txt')
cmds = [line.strip() for line in file]
file.close()
cycle = 1
process_finish = 1
i = 0
x = 1
cycle_check = [40*n+20 for n in range(6)]
strengths = 0
#CPU clock
while cycle <= cycle_check[5]:
    if process_finish == cycle:
        if i > 0 and cmds[i-1].split()[0] == "addx":
            x = x + int(cmds[i-1].split()[1])
        if cmds[i] == "noop":
            process_finish = cycle + 1
        if cmds[i].split()[0] == "addx":
            process_finish = cycle + 2
        i = i + 1
    if cycle in cycle_check:
        strengths = strengths + cycle * x
    cycle = cycle + 1
print(strengths)
