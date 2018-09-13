#--coding:utf-8--

'''
    pip.exe install MySQL-python OR
        根据安装包来安装python所需要的模块
'''

import MySQLdb

con = MySQLdb.connect(host='192.168.126.111',user='spark',passwd='spark2016',db='testdb')

cursor =con.cursor()

sql ="select * from good_student_info"

cursor.execute(sql)
#conn连接有两个重要的方法commit【提交新增和修改】,rollback【撤销新增或修改】

row=cursor.fetchone()

print row

cursor.close()

con.close()