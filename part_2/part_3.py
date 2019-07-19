#!/usr/bin/python3
#循环遍历三个表格，若出现不是MISSING的值，则放入新表中
import pymysql
import pandas as pd


class conntsql2(object):

    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='data_excel',
        charset='utf8')

    cursor = connect.cursor()

    def rel(self,tla):
        table_lists = tla
        return table_lists

    def use_databases(self):
        mysqll = 'use data_excel'
        conntsql2().cursor.execute(mysqll)
        conntsql2().connect.commit()

    def showall(self,tla):
        jj = conntsql2().rel(tla)
        sqll = "show tables LIKE '%"+jj+"%'"
        conntsql2().cursor.execute(sqll)
        aa = conntsql2().cursor.fetchall()
        newlist = []
        for i in range(len(aa)):
            newlist.append(aa[i][0])
        return newlist

    def neme(self,tla):

        neme_lt = []
        p = conntsql2().showall(tla)
        for i in range(len(p)):
            st = " SELECT `nemes` FROM " + p[i]
            conntsql2().cursor.execute(st)
            f = conntsql2().cursor.fetchall()
            if f == ():
                pass
            else:
                for j in range(len(f)):
                    if f[j - 1][0] not in neme_lt:
                        neme_lt.append(f[j - 1][0])
        li = list(set(neme_lt))
        return li

    def cnew(self,tla):

        cn_l = conntsql2().rel(tla)
        create_mysql_01 = "CREATE TABLE IF NOT EXISTS "
        create_mysql_21 = """(`ID`  int(11) NOT NULL AUTO_INCREMENT ,
        `nemes`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `entry_data`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `departure`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `phone`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `License_type`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `License_num`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `sex`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `shougu_data`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `stores`  varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `jobs`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `ryzt`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `zw`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `yfgz`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `shgz`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `sfgz`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `jbgz`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `qqj`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `gdgzze`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `nlgz`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `gljt`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `cb`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `qqkk`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `fdgzze`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `yzgz`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        PRIMARY KEY (`ID`)
        )
        ENGINE=InnoDB
        DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci
        ROW_FORMAT=DYNAMIC;
        """

        create_mysql_3 = create_mysql_01 + cn_l  + create_mysql_21
        conntsql2().cursor.execute(create_mysql_3)
        conntsql2().connect.commit()


    def int(self,tla):
        lit =  conntsql2().neme(tla)
        in1 = " INSERT INTO  "
        cn_ll = conntsql2().rel(tla)
        cl_3 = "(`nemes`)"
        ins4 = " VALUES ( '%s') "
        srt = in1 + cn_ll+ cl_3 + ins4
        for i in range(len(lit)):
            data = lit[i]
            conntsql2().cursor.execute(srt % data)
        conntsql2().connect.commit()


    def inte(self,tla):
        cn_ll1 = conntsql2().rel(tla)
        cl_31 = ['phone','entry_data','sex','zw','departure','License_type','License_num','shougu_data']
        l6 = len(cl_31)
        SHALL = conntsql2().showall(tla)
        l4 = len(SHALL)
        l_name = conntsql2().neme(tla)
        l5 = len(l_name)

        #循环表单
        for j in range(l4):
            #循环姓名
            for i in range(l5):
                #循环提取的字段
                for s in range(l6):
                    try :
                        h = l_name[i]
                        if h != None :
                            UI = " SELECT " +"`"+cl_31[s]+"`" + " FROM "  + SHALL[j+1] + " WHERE `nemes` = " +"'"+l_name[i]+"'"
                            conntsql2().cursor.execute(UI)
                            t = conntsql2().cursor.fetchall()
                            if t == ():
                                pass
                                continue
                            elif t[0][0] == 'missing':
                                pass
                                continue
                            elif t[0][0] == '':
                                pass
                                continue
                            else:
                                try:
                                    srt1 = " UPDATE " + cn_ll1 + " SET " + cn_ll1+"."+ cl_31[s] + " = " + "'" + t[0][0] + "'" + " WHERE " + cn_ll1+ ".nemes = " + "'"+l_name[i]+"'"
                                    conntsql2().cursor.execute(srt1)
                                    conntsql2().connect.commit()
                                except TypeError:
                                    pass
                    except IndexError:
                        pass