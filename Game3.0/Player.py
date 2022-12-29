# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/23 13:37
from play import Game
import pandas as pd
from Painter import Painter
from play import Game
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,QMessageBox

root='.//Userinfo//userinfo1.csv'
class Player():
    def __init__(self):
        df = pd.read_csv(root)
        self.money = list(df[0:1]['money'])
    def start(self):
        g = Game(self.money)
        p = Painter()
        QMessageBox.about(p.window,'提示','money='+str(self.money[0]))
        p.paint(g)
