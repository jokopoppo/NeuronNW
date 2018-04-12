from test import *

def iristest():
    data = readtext("Iris.txt")
    for i in range(data.__len__()):
        data[i]=data[i].split(",")
        for j in range(data[i].__len__()-1):
            data[i][j]=float(data[i][j])

        if(data[i][data[i].__len__()-1] == 'Iris-setosa\n'):
            data[i][data[i].__len__()-1] = 1
        elif(data[i][data[i].__len__()-1] == 'Iris-versicolor\n'):
            data[i][data[i].__len__()-1] = 2
        elif(data[i][data[i].__len__()-1] == 'Iris-virginica\n' or 'Iris-virginica'):
            data[i][data[i].__len__()-1] = 3


    random.shuffle(data)
    return data
