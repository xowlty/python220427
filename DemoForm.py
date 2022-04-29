# DemoForm.py
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인한 화면을 로딩
form_class = uic.loadUiType('c:\\work2\\DemoForm.ui')[0]

#윈도우 클래스를 정의
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText('첫번째 화면')

#실행프로세스를 만들어 보여주기
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec_()
