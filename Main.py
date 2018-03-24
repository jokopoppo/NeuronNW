from Node import Node
import math

def activationFunc(v):
    y=1/(1+math.e**-v)
    return y

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

# initialize neural nw
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
    inputNode[i].y=inputNode[i].x
print()

hiddenNode.append(Node(0.2))
hiddenNode.append(Node(0.4))

add_input(hiddenNode,inputNode)
add_output(inputNode,hiddenNode)

# set W hidden node
for i in range(wh.__len__()):
    print(hiddenNode[i].setW(wh[i]),end="")
print()

outputNode.append(Node(0.1))
outputNode.append(Node(0.2))

add_input(outputNode,hiddenNode)
add_output(hiddenNode,outputNode)

# set W output node
for i in range(wo.__len__()):
    print(outputNode[i].setW(wo[i]),end="")
print("\n\nend initialize neural nw\n")

# end initialize neural nw

def feedfoward(arr):
    # start feed forward
    for i in range(arr.__len__()):
        arr[i].x=[]
        for j in range(arr[0].input.__len__()):
            arr[i].x.append(arr[i].input[j].y)
        print(arr[i].x)

    # why append array in one object can affect to the others ??

    for i in range(arr.__len__()):
        sum=0
        for j in range(arr[i].x.__len__()):
            sum+=arr[i].x[j]*arr[i].w[j]

        arr[i].v=sum+arr[i].bias
        arr[i].y=activationFunc(arr[i].v)
        print(arr[i].y)

        # produce y form node

    print("produce y form node",)
    return

feedfoward(hiddenNode)
feedfoward(outputNode)

# stop feed forward

# start back propagation