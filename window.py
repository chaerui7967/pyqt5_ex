import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My App')
        self.setWindowIcon(QIcon('/Users/chaegilho/Desktop/panda.jpg')) # 어플리케이션 아이콘 설정
        # self.move(300,300) # 현재 스크린 기준 위치
        # self.resize(400, 200) # window 크기 resize
        self.setGeometry(300,300,300,200) # 위 두함수를 한번에 묶어둠 기준위치 x,y resize 너비, 높이 
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())