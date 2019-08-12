from selenium import webdriver
import urllib.request as urllib

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.cjlogistics.com/ko/tool/parcel/tracking')

input = driver.find_element_by_name('paramInvcNo')
input.send_keys("433917723655")
button = driver.find_element_by_id('btnSubmit').click()

img = driver.find_element_by_id('statusImage')
src = img.get_attribute('src')

urllib.urlretrieve(src, "result.png")
driver.close()