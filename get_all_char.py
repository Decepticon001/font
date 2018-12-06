import requests
from lxml import etree
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'xh.5156edu.com',
    # 'If-Modified-Since':'Tue, 03 Dec 2013 11:14:50 GMT',
    # 'If-None-Match':'"0b1e3e118f0ce1:2ff6"',
    'Referer':'http://xh.5156edu.com/pinyi.html',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
cookies={}
session = requests.session()
session.headers = headers
requests.utils.add_dict_to_cookiejar(session.cookies, cookies)

res = session.get("http://xh.5156edu.com/html2/p102.html",headers=headers).content.decode('gbk','ignore')
# print(res)
selector = etree.HTML(res)
u = selector.xpath('//a[@class="fontbox"]/text()')
print(u)
