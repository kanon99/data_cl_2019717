from testing import *
import xlrd
import time
#第一步骤

if __name__ == "__main__":

    start = time.process_time()

    workbook_origin2 = xlrd.open_workbook('C:\\Users\\Administrator\\PycharmProjects\\excel_all_data\\excelalldata.xlsx')
    sheet02 = workbook_origin2.sheets()[0]
    first_row_values0 = sheet02.row_values(0)
    excels = sheet02.nrows

    for j in range(excels):
        first_row_values = sheet02.row_values(j)
        try:
            workbook = xlrd.open_workbook(first_row_values[0])
        except xlrd.biffh.XLRDError:
            pass

        Nsheets = len(workbook.sheet_names())

        for i in range(Nsheets):
            try:
                mainmian(i,j)
            except KeyError or IndexError :
                pass
                continue
            i += 1
        print(first_row_values)
        j += 1

    end = time.process_time()
    t=end-start
    print("Runtime is ：",t)