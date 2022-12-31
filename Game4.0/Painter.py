# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/26 12:31
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
#绘画器 主要用于画图
class Painter():
    def __init__(self):
        self.app = QApplication([])
        self.ui = QUiLoader().load('./UI/untitled.ui')
        self.ui.setWindowIcon(QIcon('./Picture/windowlogo.png'))

    def paint(self,g):

        self.ui.Button1.clicked.connect(lambda: g.single(self.ui))
        self.ui.Button1.setIcon(QIcon('./Picture/money.png'))
        self.ui.Button2.clicked.connect(lambda: g.ten(self.ui))
        self.ui.Button2.setIcon(QIcon('./Picture/money.png'))
        self.ui.Button3.clicked.connect(lambda: g.exit(self.ui))
        self.app.setWindowIcon(QIcon('./Picture/windowlogo.png'))
        self.ui.show()

        self.app.exec_()