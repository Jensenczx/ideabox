__author__ = 'chenjensen'
#!/usr/bin/python
#coding＝utf-8
import requests
url="http://sendcloud.sohu.com/webapi/mail.send.json"
  #files={ "file1": (u"1.pdf", open(u"1.pdf", "rb")),
  #        "file2": (u"2.pdf", open(u"2.pdf", "rb"))}
  # 不同于登录SendCloud站点的帐号，您需要登录后台创建发信子帐号，使用子帐号和密码才可以进行邮件的发送。
  params = {"api_user": "Jensen_test_5uyihP", \
    "api_key" : "API_KEY已发送到您的注册邮箱",\
    "to" : "1753969686@qq.com", \
    "from" : "service@sendcloud.im", \
    "fromname" : "IdeaBox收藏", \
    "subject" : "来自SendCloud的第一封邮件！", \
    "html": "云集，让网页像app一样" \
  }

  r = requests.post(url, files={}, data=params)
  print r.text
