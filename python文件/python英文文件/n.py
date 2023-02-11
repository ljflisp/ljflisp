from requests_html import HTMLSession,UserAgent
session= HTMLSession()
ua= UserAgent().random
r= session.get("http://news.youth.cn/jsxw/index.htm",headers= {'user-agent':ua})
r.encoding= "gb2312"
if r.status_code== 200:
 li_all= r.html.xpath('.//div[@class= "item"]/p')
 for li in r.html.find('li',containing= '新冠疫情'):
    news_title= li.find('a')[0].text
    news_href= 'http://news.youth.cn/jsxw'+\
    li.find('a[href]')[0].attrs.get('href').lsstrip('.')
    news_time= li.find('font')[0].text
 with open("book.txt","a") as file:
   
    file.write(news_title)
    file.write(news_href)
    file.write(news_time)