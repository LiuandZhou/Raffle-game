# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/26 12:31
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class Painter():
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.button1 = QPushButton('保存', self.window)
        self.button2 = QPushButton('十连 160', self.window)
        self.button3 = QPushButton('单抽 16', self.window)

    def paint(self,g):
        self.window.resize(600, 500)
        self.window.move(600, 210)
        self.window.setWindowTitle('原神抽奖模拟器')

        self.button1.move(430, 430)
        self.button1.clicked.connect(lambda: g.save(self.window))

        self.button2.move(250, 430)
        self.button2.clicked.connect(lambda: g.ten(self.window))

        self.button3.move(70, 430)
        self.button3.clicked.connect(lambda: g.single(self.window))

        self.window.show()

        self.app.exec_()