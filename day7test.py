def printTree(root):
    for subtree in root.child:
        printTree(subtree)
        print(subtree.name)
        print(subtree.size)

def totalTree(root):
    for subtree in root.child:
        totalTree(subtree)
        root.size = root.size + subtree.size


class Node:
    def __init__(self,name,size=0):
        self.child = []
        self.name = name
        self.size = size

root = Node('/')
root.child.append(Node('docs'))
root.child[0].child.append(Node('file.txt', 100))
root.child.append(Node('file2.txt', 200))



totalTree(root)
printTree(root)


