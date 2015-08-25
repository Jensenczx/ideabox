__author__ = 'chenjensen'
from BeautifulSoup import BeautifulSoup
from PageGetter import PageGetter
class MindStoreCrawer:

    def __init__(self):
        nameList=[]
        hrefList=[]
        describeList=[]
        strUrl = 'http://mindstore.io/'
        geter = PageGetter(strUrl)
        page = geter.getPage()
        soup = BeautifulSoup(page)
        newProductInfo = soup.find('li',attrs={'class':'m-b-30'})
        productInfo = newProductInfo.findAll('a',attrs={'class':'mind-title'})

    def getName(self):
        for info in self.productInfo:
            self.nameList.append(info.text)
        return self.nameList

    def getUrl(self):
        for info in self.productInfo:
            self.hrefList.append(info['href'])
        return self.hrefList

    def getDescribe(self):
        describeInfo = self.newProductInfo.findAll('div',attrs={'class':'mind-des'})
        for info in describeInfo:
            self.describeList.append(info.text)
        return self.describeList


