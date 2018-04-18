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

def readExel(exelname):
    import xlrd

    ExcelFileName= exelname
    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name("Data")

    num_rows = worksheet.nrows  #Number of Rows
    num_cols = worksheet.ncols  #Number of Columns

    result_data =[]
    for curr_row in range(2,num_rows): # read except header
        row_data = []

        for curr_col in range(1, num_cols): # read except ID
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            # print(data)
            row_data.append(data)

        result_data.append(row_data)
    print("read done")
    # print(result_data[0].__len__())
    return result_data

def preprocess(data,r):


    lmax = list(map(max, zip(*data)))
    lmin = list(map(min, zip(*data)))
    mid=[]
    for i in range(lmax.__len__()):
        mid.append(lmax[i]-lmin[i])

    for i in data:
        for j in range(i.__len__()):
            if i[j]>r or i[j]<-r :
                i[j]=((i[j]-lmin[j])/(mid[j]))
    return data

# data=readExel('Data.xls')
# ans=[]
#
# for i in data :
#     ans.append(int(i.pop(i.__len__()-1)))
def readtext(t):
    with open(t) as text_file:
        s=(text_file.readlines())
    return s

def convertStr(s,n):

    a=s[n].split(",")

    a[0]=float(a[0][1:])
    a[a.__len__()-1]=float(a[a.__len__()-1][:a[a.__len__()-1].__len__()-2])

    for j in range(a.__len__()) :
        a[j]=float(a[j])
    return a


# s=readtext()
#
# for i in range(6):
#     s.pop(0)
#
# print(s)
# for i in range(s.__len__()-1):
#     s[0]=convertStr(s,0)
#     for k in s[0]:
#         print(type(k))
#     print(s.pop(0))
import random
