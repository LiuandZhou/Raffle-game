# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/23 17:13
'''
import pandas as pd
root='.//Userinfo//userinfo1.csv'
money,num,chance,purple_chance,odds,purple_odds,y,isup,purple_isup = 1440,0,0.19,0.11,0.5,0.5,[0.19],0.6,0.6
data = {'money': money, 'num': num, 'chance': chance, 'purple_chance': purple_chance,
                'odds': odds, 'purple_odds': purple_odds, 'y': y, 'isup': isup,
                'purple_isup': purple_isup}
df1 = pd.DataFrame(data, index=[i for i in range(0, len(y))])
df1.to_csv(root, index=False)
print('\n')
print("抽奖完毕", end='')

'''
import random

'''
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit
from PySide2.QtGui import QPixmap
def be():
    num = 3
    print('出金了,总共抽了' + str(num) + '抽')

def paint():
    app = QApplication([])
    window = QMainWindow()
    window.resize(600, 500)
    window.move(300, 310)
    window.setWindowTitle('原神抽奖模拟器')
    window.setPixmap(QPixmap('.//Picture//Yasuo.png'))
    button1 = QPushButton('退出', window)
    button1.move(430, 430)
    button1.clicked.connect(be())

    button2 = QPushButton('十连', window)
    button2.move(250, 430)
    button2.clicked.connect(be)

    button3 = QPushButton('单抽', window)
    button3.move(70, 430)
    button3.clicked.connect(be)

    window.show()

    app.exec_()

if __name__ == '__main__':
    paint()
'''
