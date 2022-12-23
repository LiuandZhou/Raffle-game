# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/23 13:37
from play import Game
#import pandas as pd
#import os.path
class Player():
    #root='.//Userinfo//userinfo.csv'
    money = 1440
    def start(self):
        '''
        if(os.path.exists(self.root)):
            money=pd.read_csv(self.root)
        else:
            pass
        '''
        game = Game()
        self.money=game.prize_draw(money=self.money)
