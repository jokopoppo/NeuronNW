from Node import Node

def add_input(o1,o2):
    for i in range(o1.__len__()):
        for j in range(o2.__len__()):
            o1[i].add_input(o2[j])
    return

def add_output(o1,o2):
    for i in range(o1.__len__()):
        for j in range(o2.__len__()):
            o1[i].add_output(o2[j])
    return

x=[1,0,1,1]
d=[1,0]
n=0.1

wh=[[0.3,0.1,0.2,0.1],[0.2,0.2,0.1,0.3]]
wo=[[0.1,0.1],[0.2,0.2]]

inputNode=[]
hiddenNode=[]
outputNode=[]

for i in range(4):
    inputNode.append(Node(1,x[i]))
    print(inputNode[i].setW(),end="")
print()

hiddenNode.append(Node(1))
hiddenNode.append(Node(1))

add_input(hiddenNode,inputNode)
add_output(inputNode,hiddenNode)


for i in range(wh.__len__()):
    print(hiddenNode[i].setW(wh[i]),end="")
print()

outputNode.append(Node(1))
outputNode.append(Node(1))

add_input(outputNode,hiddenNode)
add_output(hiddenNode,outputNode)

for i in range(wo.__len__()):
    print(outputNode[i].setW(wo[i]),end="")
print()



