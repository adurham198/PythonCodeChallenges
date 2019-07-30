#Anton Durham
#Date: 7/30/2019
#Program Desc: This is a program simply designed to open an excel spreadsheet
#and can be used to assign column names to variables to do some kind
#of processing. This is a work in progress as I am
#trying to learn the Pandas library to do data processing on excel data.


import xlrd

def main():

    workbook = xlrd.open_workbook('Testspreadsheet.xlsx')
    #opens the actualy file
    worksheet = workbook.sheet_by_index(0)
    #opens the first sheet(There are multiple ways to do this)
    firstnames = workbook.sheet_by_index(0).cell(0,0).value
    #opens the first sheet's cell A,0
    print(firstnames)
        


def getlogindetails():
    # function to get ext, fname, lname, login
    print("A test line")
main()
