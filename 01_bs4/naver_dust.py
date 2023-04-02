from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
)
# pprint(html.text)
soup = bs(html.text, "html.parser")
# print(soup)
data1 = soup.find("ul", {"class": "today_chart_list"})
# pprint(data1)

# 한번 작업한 data1에서 li인 요소들 가져온다.
data2 = data1.findAll("li")  # 여러 요소 가져오기 findAll(), 인덱스로 접근가능
# print("미세먼지")
# pprint(data2[0])
# print("초미세먼지")
# pprint(data2[1])
# print("자외선")
# pprint(data2[2])
# print("일출")
# pprint(data2[3])

find_dust = data2[0].find("span", {"class": "txt"}).text
print(find_dust)
