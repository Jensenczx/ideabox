__author__ = 'chenjensen'
import urllib2
import re
import mysql.connector
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagname=None
        self.flag=0
        self.infolist=[]
    def handle_starttag(self, tag, attrs):
        if(tag=='h4'):
            if(len(attrs)==0):
                pass
            else:
                for variable, value in attrs:
                    if variable == 'class' and  value =='media-heading':
                        self.flag=1
        if(tag=='a'):
            if(len(attrs)==0):
                pass
            else:
                for variable,value in attrs:
                    if self.flag==1 and variable == 'href':
                        self.infolist.append(value)
                        self.tagname='a'
                        self.flag=0
        if(tag=='p'):
            if(len(attrs)==0):
                self.tagname='p'

    def handle_endtag(self, tag):
        self.tagname=None
    def handle_data(self, data):
       if self.tagname=='a' or self.tagname=='p':
            self.infolist.append(data)
urlstr='http://today.itjuzi.com/'
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
    parser.close()
