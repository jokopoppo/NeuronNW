from Node import Node
import math
import random
from test import readExel
def activationFunc(v):
    y=1/(1+math.e**-v)
    return y

def dActivationfuction(y):
    x=y*(1-y)
    return x

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

def testtree():
    x=[1,0,1,1]
    d=[1,0]
    lr=0.1

    wh=[[0.3,0.1,0.2,0.1],[0.2,0.2,0.1,0.3]]
    wo=[[0.1,0.1],[0.2,0.2]]



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

    return
# initialize neural nw

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

    print("produce y form node\n",)
    return

def setWnew(node,i):

    for j in range(node[i].w.__len__()):
        print(node[i].w[j],end="  ")
        node[i].w[j] += (node[i].gradient*node[i].x[j]*lr)
        print("W'",j," from node",i,":",node[i].w[j])

    print(node[i].bias,end="  ")
    node[i].bias += (node[i].gradient*1*lr)
    print("Bias'"," from node",i,":",node[i].bias)
    return

def outputBPG(d,err):

    for i in range(outputNode.__len__()):
        print("ERR =",d[i],"-",outputNode[i].y,"=",end=" ")
        err.append(d[i]-outputNode[i].y)
        print(err[i])
        # find delta w from each output node
        outputNode[i].wo=outputNode[i].w
        outputNode[i].gradient=(-err[i]*dActivationfuction(outputNode[i].y))
        # save gradient and w old for hidden BPG
        setWnew(outputNode,i)

    # outputBPG done
    return

def hiddenBPG(hiddenNode):
    for i in range(hiddenNode.__len__()):
        # find delta w from each hidden node
        hiddenNode[i].wo=hiddenNode[i].w
        sum=0
        for j in hiddenNode[i].output:
            sum+=(j.gradient*j.wo[i])
        hiddenNode[i].gradient = (dActivationfuction(hiddenNode[i].y)*sum)
        # save w old for hiddenBPG
        setWnew(hiddenNode,i)
    # hiddenBPG done
    return

inputNode=[]
hiddenNode=[]
outputNode=[]

lr=0.1
data=readExel('Data.xls')
ans=[]

for i in data :
    ans.append(int(i.pop(i.__len__()-1)))

print(data[0].__len__())
for i in range(data[0].__len__()):
    inputNode.append(Node(1,data[0][i]))
    inputNode[i].setW()
    inputNode[i].y=inputNode[i].x

print()

for i in range(3):
    hiddenNode.append(Node(random.uniform(0.5,1)))
    outputNode.append(Node(random.uniform(0.5,1)))

add_input(hiddenNode,inputNode)
add_output(inputNode,hiddenNode)

add_input(outputNode,hiddenNode)
add_output(hiddenNode,outputNode)

for i in range(3):
    hiddenNode[i].setW()
    outputNode[i].setW()

# for i in range(ans.__len__()):
#     for j in range(data[i].__len__()):
#         inputNode[j].y=inputNode[j].x=data[i][j]
#     # start feed forward
#     feedfoward(hiddenNode)
#     feedfoward(outputNode)
#     # # stop feed forward
#
#     # start back propagation # find error from each output node
#     err=[]
#     d=[]
#     for j in range(outputNode.__len__()):
#         d.append(ans[i])
#     outputBPG(d,err)
#     print("\noutputBPG done\n")
#     hiddenBPG(hiddenNode)





