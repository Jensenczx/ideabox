__author__ = 'chenjensen'
import mysql.connector
class DatabaseOperateUtil:

    def __init__(self,username,password,databaseName,ifUseUnicode):
        self.username = username
        self.password = password
        self.databaseName = databaseName
        self.ifUseUnicode = ifUseUnicode

    def getideas(self):
        mconnect = mysql.connector.connect(user=self.username,password=self.password,database=self.databaseName)
        mcursor = mconnect.cursor()
        mcursor.execute('select name,like_num,address,content from ideas')
        ideadata = mcursor.fetchall()
        mconnect.commit()
        mcursor.close()
        mconnect.close()
        return ideadata

    def saveIdeas(self,name,address,content,nameList,addressList,contentList):
        mconnect = mysql.connector.connect(user=self.username,password=self.password,database=self.databaseName)
        mcursor = mconnect.cursor()
        for i in range(len(nameList)):
            mcursor.execute('insert into ideas(name,address,content) values (%s,%s,%s)',[nameList[i],addressList[i],contentList[i]])
        mconnect.commit()
        mcursor.close()
        mconnect.close()