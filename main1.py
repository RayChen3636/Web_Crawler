from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

page = 51
while True:
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    print("處理url", url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("好像最後一頁了")
        break
    html = BeautifulSoup(response)

    # find(找第一個符合條件) find all(找所有符合條件)
    # find答案:一個 find_all:list
    # print(html.find_all('li',{"class":"list-rst"}))
    for r in html.find_all('li', class_="list-rst"):
        ja = r.find("small", class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        ratings = r.find_all("b", class_="c-rating__val")
        # print(ja)
        # 萃取紙條(.text) 萃取特別特徵([特徵])
        print(ratings[0].text,
              ja.text,
              en.text,
              en["href"])
        # 我個人喜歡 打開 -> 分析 -> 增加 page
    page = page + 1
