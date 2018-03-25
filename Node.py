import random
class Node:


    def __init__(self,bias,x=[]):

        self.bias=bias

        self.output=[]
        self.input=[]
        self.x=x
        self.v=None
        self.y=None
        self.wo=[]
        self.gradient=None

    def setW(self,w=[]):

        self.w=[]

        if self.input.__len__()==0 :
            self.w.append(1)

        else:
            for i in range (self.input.__len__()):
                self.w.append(w[i])

        return self.w

    def add_output(self ,obj):

        self.output.append(obj)

        return

    def add_input(self ,obj):

        self.input.append(obj)

        return