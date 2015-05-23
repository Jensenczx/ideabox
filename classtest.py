__author__ = 'chenjensen'
# coding=utf-8
import mysql.connector
class dbhelper:
    def getidea(self):
        mycon = mysql.connector.connect(user='root',password='',database='IdeaBox',use_unicode='true')
        cursor = mycon.cursor()
        cursor.execute('select id,name,ideaherf,content from ideas')
        values = cursor.fetchall()
        mycon.commit()
        cursor.close()
        mycon.close()
        return values
    def getoneidea(self,id):
        mycon = mysql.connector.connect(user='root',password='',database='IdeaBox',use_unicode='true')
        cursor = mycon.cursor()
        cursor.execute('select name,ideaherf,content from ideas where id = %s ',[id])
        values = cursor.fetchall()
        mycon.commit()
        cursor.close()
        mycon.close()
        return values
helper = dbhelper()
print helper.getoneidea(1455)
