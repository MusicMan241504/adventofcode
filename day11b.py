file = open('day11.txt')
lines = file.readlines()
file.close()
class Monkey:
    def __init__(self,lines):
        self.items = []
        for item in lines[0].split(': ')[1].split(', '):
            self.items.append(int(item))

        self.operation = lines[1].split('= ')[1]

        self.test = int(lines[2].split('by ')[1])
        self.true = int(lines[3].split('monkey ')[1])
        self.false = int(lines[4].split('monkey ')[1])
        self.inspections = 0

        self.calc = lambda x : eval(self.operation.replace('old','x'))

    def doOperation(self,i,mod):
        self.items[i] = self.calc(self.items[i]) % mod
        self.inspections = self.inspections + 1
    def throw(self,i):
        if self.items[i] % self.test == 0:
            return self.true
        else:
            return self.false


#get monkeys
monkeys = []
i = 0
while i < len(lines):
    monkeys.append(Monkey(lines[i+1:i+6]))
    i = i + 7

#clever stuff
mod = 1
for monkey in monkeys:
    mod = mod * monkey.test


#play game
i = 0
while i < 10000:
    for monkey in monkeys:
        for j in range(len(monkey.items)):
            monkey.doOperation(0,mod)
            reciever = monkey.throw(0)
            monkeys[reciever].items.append(monkey.items[0])
            monkey.items.pop(0)
    i = i + 1

#get results
totals = []
for monkey in monkeys:
    totals.append(monkey.inspections)
totals.sort()
print(totals[-1]*totals[-2])
