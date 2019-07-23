#from.ffinally import *
from part_2.part_3 import *
import xlrd
import re
from functools import lru_cache
#第二步骤


class ca():

    @lru_cache(maxsize=900)
    def p2(self):
        workbook_origin = xlrd.open_workbook('C:\\Users\\Administrator\\PycharmProjects\\excel_all_data\\excelalldata.xlsx')
        s0 = workbook_origin.sheets()[0]
        ns = s0.nrows
        lr = []
        for i in range(ns):
            fs = s0.row_values(i)
            c1 = fs[0][9:]
            rer = re.findall(r'\w+', c1)
            cl1 = rer[0]
            lr.append(cl1)
        return lr

    def p2loop(self):
        li = ca().p2()
        lii = len(li)

        for t in range(lii):
            tla = li[t]
            conntsql2().rel(tla)
            conntsql2().cnew(tla)
            conntsql2().int(tla)
            conntsql2().inte(tla)


if __name__ == "__main__":

    ca().p2loop()