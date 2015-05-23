__author__ = 'chenjensen'
import mysql.connector
mycon = mysql.connector.connect(user='root',password='',database='IdeaBox',use_unicode='true')
cursor = mycon.cursor()
cursor.execute('insert into ideas(name,herf) values(%s,%s)',['baidu','www.baidu.com'])
mycon.commit()
cursor.close()
mycon.close()