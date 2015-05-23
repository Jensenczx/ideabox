__author__ = 'chenjensen'
import urllib2
import re
import mysql.connector
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    URL = 'http://www.demo8.com/'
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagname=None
        self.infolist=[]
    def handle_starttag(self, tag, attrs):
        if(tag=='a'):
            if(len(attrs)==0):
                pass
            else:
                for variable, value in attrs:
                    if variable == 'class' and  value =='post-url':
                        self.tagname='a'
                    if(self.tagname=='a'):
                        if variable == 'href':
                            self.infolist.append(value)
        if(tag=='span'):
            for(variable,value)in attrs:
                if variable=='class' and value=='post-tagline':
                    self.tagname='span'
    def handle_endtag(self, tag):
        self.tagname=None
    def handle_data(self, data):
       if self.tagname=='a' or self.tagname=='span':
            self.infolist.append(data)
urlstr='http://next.36kr.com/posts/'
parser = MyHTMLParser()
try:
    response=urllib2.urlopen(urlstr)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    elif hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
else:
    doc=response.read()
    page=doc.decode("utf-8")
    parser.feed(page)
    mycon = mysql.connector.connect(user='root',password='',database='IdeaBox',use_unicode='true')
    cursor = mycon.cursor()
    num = 0
    name =''
    herf =''
    content=''
    for info in parser.infolist:
        print info
        if num%3 == 3:
            name = info
        elif num%3 == 1:
            herf = info
        else:
            content = info
            cursor.execute('insert into ideas(name,herf,content) values(%s,%s)',[name,herf,content])
        num +=1
    mycon.commit()
    cursor.close()
    mycon.close()
    parser.close()






