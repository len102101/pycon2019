from selenium import webdriver
#from news.models import News

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get('https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105')

newsbox = driver.find_elements_by_class_name('cluster_item')

#for news in newsbox:
#    News.objects.create(title=news.find_element_by_class_name('cluster_text_headline').text)