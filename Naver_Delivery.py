from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd

driver = webdriver.Chrome('./chromedriver')
driver.get('https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=1&acq=xorqo&qdt=0&ie=utf8&query=%ED%83%9D%EB%B0%B0%EC%A1%B0%ED%9A%8C')

Select(driver.find_element_by_class_name('_select')).select_by_visible_text('CJ대한통운')

driver.find_element_by_id('numb').send_keys("433917723655")
driver.find_element_by_xpath('//*[@id="_doorToDoor"]/div[1]/div[2]/input[2]').click()
driver.implicitly_wait(3)

table = driver.find_element_by_xpath('//*[@id="_doorToDoor"]/div[2]/div[3]/table')
labels = table.find_elements_by_tag_name('tr')
datas = []

for i in labels:
    datas.append(i.text.split()[:3])

column = datas.pop(0)
frame = pd.DataFrame(datas)
frame.columns = column
frame.to_excel('NaverDelivery.xlsx', encoding='cp949')
