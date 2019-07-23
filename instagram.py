from selenium import webdriver

key = webdriver.common.keys.Keys
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.instagram.com/accounts/login/')

element_id = driver.find_element_by_name("username")
element_password = driver.find_element_by_name("password")

element_id.send_keys("len102101@gmail.com",key.TAB)
element_password.send_keys("dotori1021")
element_password.submit()

print(driver.title.encode('utf-8').split()[-1])
driver.close()