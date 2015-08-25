__author__ = 'chenjensen'
from BeautifulSoup import  BeautifulSoup
from PageGetter import PageGetter

class NextCrawer:

    def __int__(self):
        herfInfoList = []
        nameInfoList = []
        describeInfoList = []
        getter = PageGetter('http://next.36kr.com/posts')
        page = getter.getPage()
        soup = BeautifulSoup(page)
        newProduct = soup.find(attrs={'class':'post'})
        productInfo=self.newProduct.findAll(attrs={'class':'post-url'})


    def getNameInfo(self):
        for info in self.productInfo:
            self.nameInfoList.append(info.text)
        return self.nameInfoList

    def getUrlInfo(self):
        for info in self.productInfo:
            self.herfInfoList.append(info['href'])
        return self.herfInfoList

    def getDescribe(self):
        productDescirbe=self.newProduct.findAll(attrs={'class':'post-tagline'})
        for info  in productDescirbe:
            self.DescribeInfoList.append(info.text)
