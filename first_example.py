import requests 
from bs4 import BeautifulSoup as bs

mon = 10
day = 4
time = 2

url = "http://www.gsm.hs.kr/xboard/board.php?mode=list&tbnum=8&sCat=0&page=1&keyset=&searchword=&sYear=2018&sMonth=" + str(mon)

response = requests.get(url)
soup = bs(response.text, 'html.parser')   
area = soup.find_all("div", {"class": "food_list_box"})

content = area[day-1].find_all("div",{"class":"content_info"})
data = content[time-1].find("span").text

print(data)