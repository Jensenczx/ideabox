__author__ = 'chenjensen'
import urllib2

class PageGetter:

    def __init__(self,urlstr):
        self.urlstr = urlstr

    def getPage(self):
        try:
            response=urllib2.urlopen(self.urlstr)
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
            elif hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
        else:
            doc=response.read()
            return doc.decode("utf-8")