from requests_html import HTMLSession,UserAgent

session= HTMLSession()
ua= UserAgent().random
r= session.get('https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1,2020',headers= {'user-agent':ua})
r.encoding= 'utf-8'
if r.status_code== 200:
  r.html.render()

class_wp= r.html.xpath('.//div[@class= "list-wp"]/a')
for a in class_wp:
  title= a.find('p span')[0].text
  print("电影名称为:",title)