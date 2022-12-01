import requests
from datetime import datetime, timedelta
import os
from bs4 import BeautifulSoup

# init
os.remove('content.txt')


url = "https://astro.click108.com.tw/daily_8.php?iAstro=8"
today = datetime.now()


for i in range(7):
    dayX = (today+timedelta(days=i))
    dateString = dayX.strftime("%Y-%m-%d")
    print(dateString)
    response = requests.get(f'{url}&iAcDay={dateString}')
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())  # 輸出排版後的HTML內容
    today_content = soup.find("div", class_="TODAY_CONTENT")
    with open('content.txt', "a") as f:
        f.write(f'{dateString} {dayX.strftime("%A")}')
        f.write(today_content.get_text())

