# web2.py
import urllib.request
from bs4 import BeautifulSoup

#파일에 쓰기 (wt: write text)
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#규칙이 있는 숫자의 열(수열)을 생성하는 코드
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    #웹사이트에 요청해서 문자열 받기
    data = urllib.request.urlopen(url)
    #검색이 용이한 객체 만들기
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")

    for item in cartoons:
        title = item.find("a").text
        print(title.strip())
        f.write(title.strip() + "\n")

f.close()
# data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

# #검색이 용이한 객체 만들기
# soup = BeautifulSoup(data, "html.parser")

# <td class="title">
# 				<a href="/webtoon/detail?titleId"> 마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>

# cartoons = soup.find_all("td", class_="title")
# title = cartoons[0].find("a").text
# link = cartoons[0].find("a")["href"]
# print("개수:", len(cartoons))
# print(title)
# print(link)

# #파일에 쓰기 (wt: write text)
# f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
# for item in cartoons:
#     title = item.find("a").text
#     print(title.strip())
#     f.write(title.strip() + "\n")

# f.close()

