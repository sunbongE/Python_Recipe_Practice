from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
import requests
from time import sleep
from selenium.webdriver.common.by import By

# import pandas as pd
# 웹페이지를 열고 소스코드를 읽어오는 작업
URL = "https://comic.naver.com/webtoon?tab=mon"
# html = requests.get(URL).text
# print(requests.get(URL).status_code) 200
# soup = BeautifulSoup(html, "html.parser")

driver = webdriver.Chrome("C:/chromedriver.exe")  # 크롬 사용하니까
driver.get(URL)
sleep(5)
data1 = driver.find_element(By.CLASS_NAME, "블로그")
print(data1)
