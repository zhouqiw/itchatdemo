# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: re_test.py
@time: 2017/10/10 下午7:49
"""


# -*- coding: UTF-8 -*-

#安装MYSQL DB for python
import MySQLdb as mdb


class mysql_dbs:
    def __init__(self,database):

        self.database = database;
    def __getconnect(self):
        if not self.database:
            raise(NameError,"no setting db info")
        #连接mysql的方法：connect('ip','user','password','dbname')
        self.con = mdb.connect('localhost', 'root',
            'rooter', self.database);

        # #所有的查询，都在连接con的一个模块cursor上面运行的
        cur = self.con.cursor()
        if not cur:
            raise (NameError,"connected failed")
        else:
            return cur

    def execQuery(self,sql):

        try:
            cur = self.__getconnect()
            cur.execute(sql)
            ret = cur.fetchall()
            cur.close()
            self.con.close()

        except mdb.Error, e:
            return []
            print e
        return ret

    def execnnoQuery(self,sql):

        cur = self.__getconnect()
        cur.execute(sql)
        # cur.commit()
        cur.close()
        self.con.close()
        print "++++++++"
    def insert(self,tupl):

        sql="insert into card VALUES ('v1','v2','v3')"
        tuplin = ('v1','v2','v3')
        for i in range(3):
            sql = sql.replace(tuplin[i],tupl[i])

        # print sql
        cur = self.__getconnect()
        cur.execute(sql)
        self.con.commit()
        cur.close()
        self.con.close()
        # print "++++++++"
    def insert_0(self,tupl):

        sql="insert into card_0 VALUES ('v1','v2','v3')"
        tuplin = ('v1','v2','v3')
        for i in range(3):
            sql = sql.replace(tuplin[i],tupl[i])

        # print sql
        cur = self.__getconnect()
        cur.execute(sql)
        self.con.commit()
        cur.close()
        self.con.close()
        # print "++++++++"

    def show(self):
        sql = "select * from card where price >200"
        re = self.execQuery(sql)
        for i in re:
            for j in i:
                print j

    def getcar_informtion(self,table):
        sql = "select * from card where price >200"
        re = self.execQuery(sql)
        for i in re:
            for j in i:
                print j
# mys = mysql_dbs('agent')


# nn = ('123456124','2017-09-11 10:05:57','100.95')
#
# mys.insert(nn)
# mys.show()








        #
        # #执行一个查询
        # cur.execute("SELECT VERSION()")
        #
        # #取得上个查询的结果，是单个结果
        # data = cur.fetchone()
        # print "Database version : %s " % data
        # with con:
        #     # 仍然是，第一步要获取连接的cursor对象，用于执行查询
        #     cur = con.cursor()
        #     # 类似于其他语言的query函数，execute是python中的执行查询函数
        #     cur.execute("SELECT * FROM card")
        #
        #     # 使用fetchall函数，将结果集（多维元组）存入rows里面
        #     rows = cur.fetchall()
        #
        #     # 依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
        #     for row in rows:
        #         print row[0]
    # finally:
    #     if con:
    #         #无论如何，连接记得关闭
    #         con.close()