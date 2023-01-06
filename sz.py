from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
capa= webdriver.DesiredCapabilities().FIREFOX
caps["marionette"]=False
binary= FirefoxBinary(r'D:\Program Files\MozillaFirefox\firefox.exe')
driver= webdriver.Firefox(firefox_binary= binary,capabilities= caps)
for i in range(1,21):
  driver.get("https://zh.airbnb.com/s/Shenzhen--China?page="+str(i))
rent_list= driver.find_elements_by_css_selector('div.infoContainer_v72lrv')
for eachhouse in rent_list:
    comment= eachhouse.find_element_by_css_selector('span.text_5mbkop-o_O-size_micro_16wifzf-o_O-inline_gb6r3e')
    comment= comment.text
    price= eachhouse.find_element_by_css_selector('div.priceContainer_4ml1ll')
    price= price.text[4:]
    name= eachhouse.find_element_by_css_selector('div.listingNameContainer_kq7ac0-o_O-ellipsized_1iurgbx')
    name= name.text
    details= eachhouse.find_elements_by_css_selector('span.detailWithoutWrap_j1kt73')
    detail_list= [i.text for i in details]
    house_type= detail_list[0]
    no_bed= detail_list[1]
    no_visitor= detail_liat[2]
    print(comment,price,name,jouse_tye,no_bed,no_visitor)
    
    