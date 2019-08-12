from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('./chromedriver')
driver.get('https://book.naver.com/bestsell/bestseller_list.nhn')

BookList = driver.find_element_by_class_name('basic').find_elements_by_tag_name('li')
DataList = []

for i in BookList:
    title = i.find_element_by_tag_name('dt').text
    info = i.find_element_by_tag_name('dd').text.split('|')

    writer = info[0]
    publication = info[-2]
    date = info[-1]

    DataList.append([title, writer, publication, date])

driver.close()

data = pd.DataFrame(DataList)
data.columns = ['title', 'writer', 'publication', 'date']
data.to_excel('NaverBookRank.xlsx', encoding='cp949')

driver.find_xp