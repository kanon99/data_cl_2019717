#!/usr/bin/python3
from the_N_excelsheets import *
import pymysql
from functools import lru_cache
#第三步骤

class ne():

    won = xlrd.open_workbook('C:\\Users\\Administrator\\PycharmProjects\\excel_all_data\\a.xlsx')
    sheet0 = won.sheets()[0]
    fi = sheet0.nrows

    @lru_cache(maxsize= 500)
    def cr_ex(self):

        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8'
            )

        cursor = connect.cursor()

        fff = ne().fi
        s0 = ne().sheet0
        for i in range(fff):
            try:
                fva = s0.row_values(i)
                eate = fva[0][9:]
                rer = re.findall(r'\w+', eate)
                names_el = rer[0]
                sqq1 = " CREATE TABLE " + names_el + " LIKE data_excel."+names_el
                cursor.execute(sqq1)
                connect.commit()
            except Exception:
                continue


    @lru_cache(maxsize= 500)
    def cr_e(self):

        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8'
        )

        cursor = connect.cursor()

        fe = ne().fi
        s0e = ne().sheet0

        for i in range(fe):
            try:
                fva = s0e.row_values(i)
                crea = fva[0][9:]
                rer = re.findall(r'\w+', crea)
                names_el = rer[0]
                sqq2 = " INSERT INTO  " + "test." + names_el + " SELECT * FROM data_excel." + names_el
                cursor.execute(sqq2)
                connect.commit()
            except Exception:
                continue


# if __name__ == "__main__":
#
#     #ne().cr_ex()
#     #ne().cr_e()