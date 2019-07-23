from the_N_excelsheets import *
import xlrd
#获取第N张sheet表格
from datetime import datetime
from xlrd import xldate_as_tuple
import pandas as pd
from the_N_excelsheets import *
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from functools import lru_cache

@lru_cache(maxsize= 700)
def todaota(Now_N_sheets,j):

    sheet = get_excelNsheets(Now_N_sheets,j)[0]
    try:
        first_row_values = sheet.row_values(0)
    except IndexError:
        first_row_values = []
    nrows = sheet.nrows
    list = []
    num = 1

    try:
        for row_num in range(1, nrows):
            row_values = sheet.row_values(row_num)
            if row_values:
                str_obj = {}
            for i in range(len(first_row_values)):
                ctype = sheet.cell(num, i).ctype
                cell = sheet.cell_value(num, i)
                if ctype == 2 and cell % 1 == 0.0:
                    cell = int(cell)
                    cell = str(cell)
                elif ctype == 3:
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%m/%d %H:%M:%S')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                str_obj[first_row_values[i]] = cell
            list.append(str_obj)
            num = num + 1
        list = pd.DataFrame(list)
        return list
    except:
        list = []
        return list