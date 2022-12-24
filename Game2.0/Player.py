# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/23 13:37
from play import Game
import pandas as pd
root='.//Userinfo//userinfo.csv'
class Player():
    df = pd.read_csv(root)
    money = int(df[0:1]['money'])
    def start(self):
        game = Game()
        self.money=game.prize_draw(money=self.money)
