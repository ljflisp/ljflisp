import requests
import json
def single_page_comment(link):
  headers= {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
  r= requests.get(link,headers= headers)
  json_data= json.loads(r.text)
  comment_list= json_data['data']['comments']
  for eachone in comment_list:
    message= comment_list[eachone]['content']
    print(message)
  for page in range(0,2):
    link1= "https://api.gentie.163.com/products/aace1d69a0924085b4fe15d19cb0378/threads/-8419873253791115244/comments/newList?offset="
    link2= "&limit=30&showLevelThreshold=72&headLimit=1&tailLimit=2&ibc=yunTie&_=1494427402001"
    page_str=str(page*30)
    link=link1+page_str+link2
    print(link)
    single_page_comment(link)