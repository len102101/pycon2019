from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get('https://www.instagram.com/accounts/login/')

element_id = driver.find_element_by_name("username")
element_password = driver.find_element_by_name("password")

element_id.send_keys("아이디")
element_password.send_keys("패스워드")
element_password.submit()
print(driver.title.encode('utf-8').split()[-1])

driver.close()