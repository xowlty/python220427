# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import urllib.request
from bs4 import BeautifulSoup

#디자인한 화면을 로딩
form_class = uic.loadUiType('c:\\work2\\DemoForm2.ui')[0]

#윈도우 클래스를 정의(QMainWindow가 부모 클래스)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        f = open("c:\\work2\\webtoon.txt", "wt", encoding="utf-8")
        for i in range(1,6):
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print(url)
            data = urllib.request.urlopen(url)
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text
                print(title.strip())
                f.write(title.strip() + "\n")
        f.close()
        self.label.setText('네이버 웹툰 크롤링 종료')
    def secondClick(self):
        self.label.setText('두번째 버튼을 클릭')
    def thirdClick(self):
        self.label.setText('세번째 버튼을 클릭~~')

#실행프로세스를 만들어 보여주기
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec_()
