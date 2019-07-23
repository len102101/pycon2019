from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('링크')

result = driver.find_element_by_tag_name('h1').text
print("result:",result)

driver.close()