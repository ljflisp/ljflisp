import requests
import parsel
url= "https://www.phei.com.cn/xwxx/index.shtml"
resp= requests.get(url)
sel= parsel.Selector(resp.content.decode("utf8"))
li= sel.css(".web_news_list url li.li_b60")
for news in li:
  title= news.css("p.li_news_title::text").extract_first()
  pub_time= news.css("span::text").extract_first()
  desc= news.css("p.li_news_summary::text").extract_first()
  image= news.css("div.li_news_line imag::attr('src')").extract_first()
print(title,pub_time,image)
