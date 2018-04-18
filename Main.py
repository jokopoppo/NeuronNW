from Node import Node
import math
import numpy as np
# from test2 import *
from test import *


# initialize neural nw

# end initialize neural nw

def activationFunc(v):
    # print("V = ",v)
    y = 1 / (1 + math.exp(-v))

    return y


def dActivationfuction(y):
    x = y * (1 - y)
    return x


def add_input(o1, o2):
    for i in range(o1.__len__()):
        for j in range(o2.__len__()):
            o1[i].add_input(o2[j])
    return


def add_output(o1, o2):
    for i in range(o1.__len__()):
        for j in range(o2.__len__()):
            o1[i].add_output(o2[j])
    return


def feedfoward(arr):
    # start feed forward

    for i in range(arr.__len__()):
        arr[i].x = []
        for j in range(arr[0].input.__len__()):
            arr[i].x.append(arr[i].input[j].y)
        # print("Input ",i," :",end=" ")
        # print(arr[i].x)

        s = (np.array(arr[i].x) * np.array(arr[i].w))

        arr[i].v = sum(s) + arr[i].bias
        arr[i].y = activationFunc(arr[i].v)

        # produce y form node

    # print("produce y form node\n",)
    return


def setWnew(node, i):
    for j in range(node[i].w.__len__()):
        # print(node[i].w[j],end="  ")
        node[i].w[j] += (node[i].gradient * node[i].x[j] * lr)
        # print("W'",j," from node",i,":",node[i].w[j])

    # print(node[i].bias,end="  ")
    node[i].bias += (node[i].gradient * 1 * lr)
    # print("Bias'"," from node",i,":",node[i].bias)
    return


def outputBPG(outputNode, d, err):
    for i in range(outputNode.__len__()):
        # print("ERR =",d[i],"-",outputNode[i].y,"=",end=" ")
        err.append(d[i] - outputNode[i].y)

        # print(err[i])
        # find delta w from each output node
        outputNode[i].wo = outputNode[i].w
        outputNode[i].gradient = (-err[i] * dActivationfuction(outputNode[i].y))
        # save gradient and w old for hidden BPG
        setWnew(outputNode, i)

    # outputBPG done
    return outputNode


def hiddenBPG(hiddenNode):
    for i in range(hiddenNode.__len__()):
        # find delta w from each hidden node
        hiddenNode[i].wo = hiddenNode[i].w
        sum = 0
        for j in range(hiddenNode[i].output.__len__()):
            sum += (hiddenNode[i].output[j].gradient * hiddenNode[i].output[j].wo[i])
        hiddenNode[i].gradient = (dActivationfuction(hiddenNode[i].y) * sum)
        # save w old for hiddenBPG
        setWnew(hiddenNode, i)
    # hiddenBPG done
    return hiddenNode


def train(outputNode, hiddenNode, data, ans):
    # start train
    ccc=0
    for i in range(data.__len__()):
        # print("\n\n\n*******Row ",i,"Start*****\n\n\n")
        for j in range(data[i].__len__()):
            inputNode[j].y = data[i][j]
        # start feed forward

        feedfoward(hiddenNode)
        feedfoward(outputNode)
        # stop feed forward

        # start back propagation # find error from each output node
        err = []
        d = []

        for j in range(outputNode.__len__()):
            d.append(ans[i])

        outputNode = outputBPG(outputNode, d, err)
        hiddenNode = hiddenBPG(hiddenNode)

    # train done

    return


def test(outputNode, hiddenNode, data, ans):
    # start test
    correct = 0

    for i in range(data.__len__()):
        # print("\n\n\n*******Row ",i,"Start Test*****\n\n\n")
        for j in range(data[i].__len__()):
            inputNode[j].y = inputNode[j].x = data[i][j]
        # start feed forward
        feedfoward(hiddenNode)
        feedfoward(outputNode)
        # stop feed forward

        tmp = outputNode[0].y

        if (abs(tmp - ans[i] ) <= 1/2):
            correct += 1

    # test done

    return correct


inputNode = []
hiddenNode = []
outputNode = []

lr = 1

data = readExel('Data.xls')
data = preprocess(data, 1)

percent=int(data.__len__()*10/100)
random.shuffle(data)

dat=[]

for i in range(10):
    dat.append(data[i*percent:(i+1)*percent])

# random.shuffle(data)
# data=iristest()


# min = list(map(min, zip(*data)))
# max = list(map(max, zip(*data)))


for i in range(data[0].__len__()-1):
    inputNode.append(Node(1, data[0][i]))
    inputNode[i].setW()
    inputNode[i].y = inputNode[i].x

print()
s = readtext("Output.txt")
for i in range(3):
    hiddenNode.append(Node(float(s.pop(0))))
outputNode.append(Node(float(s.pop(0))))

add_input(hiddenNode, inputNode)
add_output(inputNode, hiddenNode)

add_input(outputNode, hiddenNode)
add_output(hiddenNode, outputNode)

for i in range(3):
    s[0] = convertStr(s, 0)
    hiddenNode[i].setW(s.pop(0))
s[0] = convertStr(s, 0)
outputNode[0].setW(s.pop(0))

n = 0
e = 0

acc=[]
while (n < 10):

    datatrain=[]
    datatest=dat[n]

    for i in range(dat.__len__()):
        if(i!=n):
            datatrain+=dat[i]

    random.shuffle(datatrain)

    ans = []
    for i in datatrain:
        ans.append(int(i.pop(i.__len__() - 1)))

    anstest =[]
    for i in datatest:
        anstest.append(int(i.pop(i.__len__() - 1)))

    train(outputNode, hiddenNode, datatrain, ans)
    c = test(outputNode, hiddenNode, datatest, anstest)
    n += 1
    print(n, c)
    acc.append(c)

accurancy=((sum(acc)/acc.__len__())/datatest.__len__())*100
print("Accurancy = ",accurancy,"%")

# save W' and Bias' of all node

with open("Output.txt", "w") as text_file:
    for i in range(hiddenNode.__len__()):
        print(hiddenNode[i].bias, file=text_file)
    print(outputNode[0].bias, file=text_file)
    for i in range(hiddenNode.__len__()):
        print(hiddenNode[i].w, file=text_file)
    print(outputNode[0].w, file=text_file)

    print(n + int(s[s.__len__() - 1]), file=text_file)
