__author__ = 'chenjensen'
import urllib2
import re
from HTMLParser import HTMLParser
class Demo8HTMLParser(HTMLParser):
    URL = 'http://www.demo8.com/'
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagname=None
        self.flag=0
        self.flag1=0
        self.infolist=[]
    def handle_starttag(self, tag, attrs):
        if tag=='h3':
            if len(attrs)==0:
                pass
            else:
                for variable, value in attrs:
                    if variable == 'class' and  value =='demo_tit':
                        self.flag=1
        if tag=='a':
            if self.flag==1:
                for variable,value in attrs:
                    if variable == 'href' and re.match(r'^.{1}demo.{1}[0-9]{5}$',value):
                        self.flag=0
                        self.tagname='a'
                        self.infolist.append(value)
        if tag=='p':
            for variable,value in attrs:
                if variable=='class'and value=='demo_info':
                    self.tagname='p'
    def handle_endtag(self, tag):
        self.tagname=None
    def handle_data(self, data):
       if self.tagname=='a' or self.tagname=='p':
            self.infolist.append(data)
urlstr='http://www.demo8.com/'
parser = MyHTMLParser()
