from requests_html import HTMLSession,UserAgent
session= HTMLSession()
ua=UserAgent().random
r= session.get("http://news.youth.cn/jsxw/index.htm",headers= {'user-agent':ua})
for li in r.html.find('li',containing= '新冠疫情'):
 a= li.search('<a href= "">{}</a>')
 news_title= a[1]
 print(news_title)