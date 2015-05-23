__author__ = 'chenjensen'
import urllib2
from classtest import  hehe
urllist = ['http://www.demo8.com/','http://mindstore.io/','http://today.itjuzi.com/','http://next.36kr.com/posts/']
ideas = []
product ={'name','href','content'}
try:
    response=urllib2.urlopen()
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