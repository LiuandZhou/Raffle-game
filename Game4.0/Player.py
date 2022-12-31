# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/23 13:37
from play import Game
import pandas as pd
from Painter import Painter
from play import Game
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,QMessageBox
#玩家类

class Player():
    def __init__(self):
        self.root = './/Userinfo//userinfo1.csv'
        df = pd.read_csv(self.root)
        self.money = list(df[0:1]['money'])#使用列表主要是可以传递地址让money可以改变自身
    def start(self):
        g = Game(self.money)
        p = Painter()
        QMessageBox.about(p.ui,'提示','money='+str(self.money[0]))
        p.paint(g)
        #保存
        data = {'money': self.money[0], 'num': g.num, 'chance': g.chance, 'purple_chance': g.purple_chance,
                'odds': g.odds, 'purple_odds': g.purple_odds, 'y': g.y, 'isup': g.isup,
                'purple_isup': g.purple_isup}
        df1 = pd.DataFrame(data, index=[i for i in range(0, len(g.y))])
        df1.to_csv(g.root, index=False)
