#查询数据库所有表的zw列
import pymysql
import time

class eo():

    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='test',
        charset='utf8'
    )

    cursor = connect.cursor()

    def cselc(self):

        q = " SELECT table_name FROM information_schema. TABLES WHERE information_schema.`TABLES`.TABLE_SCHEMA='test'"
        eo().cursor.execute(q)
        #获得所有表单list
        alllists = eo().cursor.fetchall()
        g = len(alllists)
        summ = 0
        for i in range(g-1):
            rr = " select count(*) from " +  alllists[i][0] + " where `departure`<> 'Null' "
            eo().cursor.execute(rr)
            countt = eo().cursor.fetchall()
            summ += int(str(countt[0][0]))
        print(summ)


    #合并导出
    def altoone(self):

        q = " SELECT table_name FROM information_schema. TABLES WHERE information_schema.`TABLES`.TABLE_SCHEMA='test'"
        eo().cursor.execute(q)
        # 获得所有表单list
        alllists = eo().cursor.fetchall()
        g = len(alllists)
        time0 = time.process_time()
        for i in range(g-1):
            sql_0 = " drop temporary table if exists tmp_table "
            eo().cursor.execute(sql_0)
            sql_1 = "  CREATE TEMPORARY TABLE IF NOT EXISTS tmp_table SELECT  `nemes`,`sex`,`entry_data`,`License_num`,`phone`,`departure`,`shougu_data`,`jobs`,`zw` FROM test."+ alllists[i][0] + " as bb "
            eo().cursor.execute(sql_1)
            sql_2 = " alter table tmp_table add column `prj_name` varchar(200) "
            eo().cursor.execute(sql_2)
            sql_3 = " UPDATE tmp_table set `prj_name` = " + "'"+str(alllists[i][0])+"'"
            eo().cursor.execute(sql_3)
            sql_4 = " INSERT INTO aoll.allin SELECT * FROM tmp_table as bb"
            eo().cursor.execute((sql_4))
            print("add",alllists[i][0])
        time1 = time.process_time()
        t = time1 - time0
        print(t)


if __name__ == "__main__":

    #eo().cselc()
    eo().altoone()