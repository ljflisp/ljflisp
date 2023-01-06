from selenium import webdriver
driver= webdriver.Firefox()
user= driver.find_element_by_name("username")
user.clear()
user.send_keys("1234567")
pwd= driver.find_element_by_name("password")
pwd.clear()
pwd.send_keys("******")
driver.find_element_by_id("loginBtn").click()