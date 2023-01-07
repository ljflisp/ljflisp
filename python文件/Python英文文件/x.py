from requests_html import HTMLSession,UserAgent

session= HTMLSession()
url= 'http://news.youth.cn/'
r= session.get(url)
print(r.html)

#post请求
session2= HTMLSession()
data= {'user':'admin','password':123456}
r2= session2.post('http://httpbin.org/post',data= data)
if r2.status_code== 200:
  print(r2.text)

session3= HTMLSession()
ua= UserAgent().random
r3= session.get('http://httpbin.org/get',headers= {'user-agent':ua})
if r3.status_code== 200:
  print(r3.text)