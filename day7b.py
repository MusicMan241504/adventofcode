def printTree(root):
    for subtree in root.child:
        printTree(subtree)
        if len(subtree.child) > 0 and subtree.size < 100000:
            print(subtree.name)
            print(subtree.size)

def calcTotal(root):
    total = 0
    for subtree in root.child:
        if len(subtree.child) > 0 and subtree.size < 100000:
            total = total + subtree.size
        total = total + calcTotal(subtree)
    return total

def dirToDelete(root,minDirSize,dirSize=70000000):
    for subtree in root.child:
        dirSize = dirToDelete(subtree,minDirSize,dirSize)
        if subtree.size >= minDirSize:
            if subtree.size < dirSize:
                dirSize = subtree.size
    return dirSize



def totalTree(root):
    for subtree in root.child:
        totalTree(subtree)
        root.size = root.size + subtree.size



class Node:
    def __init__(self,name,parent,size=0):
        self.child = []
        self.name = name
        self.size = size
        self.parent = parent

root = Node('root',None)
tree = root

file = open('day7.txt')
lines = [line.strip() for line in file.readlines()]
i = 0 #will now create extra root directory
while i < len(lines):
    if lines[i].startswith('$ cd'):
        if lines[i].split()[2] != '..':
            for subtree in tree.child:
                if subtree.name == lines[i].split()[2]:
                    tree = subtree
                    break
        else:
            tree = tree.parent

    elif lines[i].startswith('dir'):
        tree.child.append(Node(lines[i].split()[1],tree))
    elif not lines[i].startswith('$'):
        tree.child.append(Node(lines[i].split()[1],tree,int(lines[i].split()[0])))
    i = i + 1



totalTree(root)
#printTree(root)
print(calcTotal(root))
print(dirToDelete(root,30000000-(70000000-root.size)))

