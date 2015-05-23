__author__ = 'chenjensen'
import urllib2
import re
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    URL = 'http://mindstore.io/'
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagname=None
        self.infolist=[]
        self.flag =0
    def handle_starttag(self, tag, attrs):
        if(tag=='a'):
            for variable,value in attrs:
                if variable == 'class' and value=='mind-title':
                    self.tagname='a'
                    self.flag=1
            if(self.flag==1):
                for variable,value in attrs:
                    if variable == 'href':
                        self.flag=0
                        self.infolist.append(value)
        if(tag=='div'):
            if(len(attrs)>0):
                for variable,value in attrs:
                    if variable =='class' and value=='mind-des':
                        self.tagname='div'

    def handle_endtag(self, tag):
        self.tagname=None
    def handle_data(self, data):
       if self.tagname=='a' or self.tagname=='div':
            self.infolist.append(data)
urlstr='http://mindstore.io/'
parser = MyHTMLParser()
try:
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
                 "Referer": urlstr}
    req = urllib2.Request(urlstr, headers=i_headers)
    response=urllib2.urlopen(req)
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
    try :
        parser.feed(page)
    except :
        pass
    finally:
        for info in parser.infolist:
            print info
    parser.close()
