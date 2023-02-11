from selenium import webdriver
driver=webdriver.FireFox()
driver.get("https://www.dianping.com/search/category/7/10/p1/")
comment= driver.find_element_by_css_selector('div.bdy-inner')
content= comment.find_element_by_tag_name('p')
print(content.text)