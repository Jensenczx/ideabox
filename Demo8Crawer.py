__author__ = 'chenjensen'
from BeautifulSoup import BeautifulSoup
from PageGetter import PageGetter
import  re
class Demo8Crawer:

    def __int__(self):
        nameInfoList = []
        urlInfoList = []
        describeInfoList = []
        strUrl='http://www.demo8.com/'
        strReg='http://www.demo8.com/demo/'
        infoGetter = PageGetter(strUrl)
        page = infoGetter.getPage()
        soup = BeautifulSoup(page)
        newProductInfo = soup.find(attrs={'class':'data_list clearfix'})
        nameAndUrlInfo = newProductInfo.findAll('a',attrs={'href':re.compile(r'^(strReg)[0-9]+$')})

    def getName(self):
        for info in self.nameAndUrlInfo:
            self.nameInfoList.append(info.text)
        return self.nameInfoList

    def getUrl(self):
        for info in self.nameAndUrlInfo:
            self.nameInfoList.append(info['href'])
        return self.urlInfoList

    def getDescribe(self):
        for info in self.newProductInfo.findAll('p',attrs={'class':'demo_info'}):
            self.describeInfoList.append(info.text)
        return self.describeInfoList