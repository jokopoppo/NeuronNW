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

def preprocess(data):


    lmax = list(map(max, zip(*data)))
    lmin = list(map(min, zip(*data)))
    mid=[]
    for i in range(lmax.__len__()):
        mid.append(lmax[i]-lmin[i])

    for i in data:
        for j in range(i.__len__()):
            if i[j]>10 or i[j]<-10 :
                i[j]=((i[j]-lmin[j])/(mid[j]))
    return data

# data=readExel('Data.xls')
# ans=[]
#
# for i in data :
#     ans.append(int(i.pop(i.__len__()-1)))
x="KKKKK"
with open("Output.txt", "w") as text_file:
    for i in range(30):
        print(f"Purchase Amount: {x}", file=text_file)