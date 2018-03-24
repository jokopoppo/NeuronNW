class Node:

    def __init__(self,x=[]):
        self.x=x


node = []
for i in range(3):
    node.append(Node())

for i in range(3):
    node[0].x.append(i)

for i in node:
    print(i.x)