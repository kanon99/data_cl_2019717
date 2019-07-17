from testing import *
import xlrd
import time

if __name__ == "__main__":

    start = time.process_time()

    workbook_origin2 = xlrd.open_workbook('C:\\Users\\Administrator\\PycharmProjects\\excel_all_data\\excelalldata.xlsx')
    sheet02 = workbook_origin2.sheets()[0]
    first_row_values0 = sheet02.row_values(0)
    excels = sheet02.nrows

    for j in range(excels):
        first_row_values = sheet02.row_values(j)
        workbook = xlrd.open_workbook(first_row_values[0])
        Nsheets = len(workbook.sheet_names())

        for i in range(Nsheets):
            try:
                mainmian(i,j)
            except KeyError:
                pass
                continue

            i += 1
        j += 1

    end = time.process_time()
    t=end-start
    print("Runtime is ：",t)