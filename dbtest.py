__author__ = 'chenjensen'
# coding=utf-8
import mysql.connector
class dbhelper:
    def getidea(self):
        mycon = mysql.connector.connect(user='root',password='',database='IdeaBox',use_unicode='true')
        cursor = mycon.cursor()
        cursor.execute('select id,name,ideaherf,content,image from ideas')
        values = cursor.fetchall()
        mycon.commit()
        cursor.close()
        mycon.close()
        return values
    def getoneidea(self,id):
        mycon = mysql.connector.connect(user='root',password='',database='IdeaBox',use_unicode='true')
        cursor = mycon.cursor()
        cursor.execute('select id,name,ideaherf,content,image from ideas where id=%s',[id])
        ideainfo = cursor.fetchall()
        mycon.commit()
        cursor.close()
        mycon.close()
        return ideainfo[0]
helper = dbhelper()
print helper.getoneidea(1455)
