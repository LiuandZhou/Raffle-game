# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/6/26 9:34
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from Hero_pool import Hero
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,QMessageBox
import random

class Game():
    def __init__(self,money):
        self.CHANCE = 0.19
        self.PC = 0.11
        self.CHANCE_GROW = 0.0091
        self.PC_GROW = 0.095
        self.hero = Hero()
        '''以上为常量'''
        self.root = './Userinfo/userinfo1.csv'
        self.df = pd.read_csv(self.root)
        self.money = money
        self.y = list(self.df['y'])
        self.chance = float(self.df[0:1]['chance'])
        self.num = int(self.df[0:1]['num'])
        '''
        chance为抽奖概率
        num为抽奖次数
        isup用于判断是否抽歪
        odds为出金概率
        purple_chance为出紫概率
        '''
        self.isup = float(self.df[0:1]['isup'])
        self.choice = '1'
        self.odds = float(self.df[0:1]['odds'])
        self.purple_chance = float(self.df[0:1]['purple_chance'])
        self.purple_odds = float(self.df[0:1]['purple_odds'])
        self.purple_isup = float(self.df[0:1]['purple_isup'])

    def draw_result(self,x,y):# 画出金前结果图
        plt.plot(x,y,marker='o',label='chance')
        odds_list = [self.odds for _ in x]
        odds_list.append(self.odds)
        plt.plot(odds_list,label='odds')
        plt.title('Details',fontsize=20)
        plt.xlabel('Number of prize you draw',fontsize=15)
        plt.ylabel('Percentage of gold',fontsize=15)
        plt.grid()
        plt.legend()
        plt.show()
    def show_picture(self,prize):#展示图片
        img = cv2.imread(".//Picture//"+prize+".png")
        img = cv2.resize(img,(800,500),interpolation=cv2.INTER_AREA)
        cv2.imshow(prize ,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def single(self,window):#单抽
        if (self.money[0] >= 16):
            self.money[0] -= 16
            if (self.chance > self.odds):  # 出金了
                if self.isup > 0.5:  # 没歪
                    self.money[0] += 880
                    self.show_picture(self.hero.gold_pool[0])
                    self.num += 1
                    x = range(0, self.num + 1)
                    self.y.append(self.chance)
                    self.draw_result(x, self.y)
                    self.y = [self.CHANCE]
                    self.odds = np.random.rand(1)
                    QMessageBox.about(window,'单抽结果',str(self.num) + '抽出'+self.hero.gold_pool[0]
                                      +'\nmoney='+str(self.money[0]))
                    self.num = 0
                    self.chance = self.CHANCE
                    self.purple_chance += self.PC_GROW
                    self.isup = np.random.rand(1)
                else:  # 歪了
                    self.money[0] += 540
                    prize = random.choice(self.hero.gold_pool[1:] )
                    self.show_picture(prize)
                    self.num += 1
                    x = range(0, self.num + 1)
                    self.y.append(self.chance)
                    self.draw_result(x, self.y)
                    self.y = [self.CHANCE]
                    self.odds = np.random.rand(1)
                    QMessageBox.about(window, '单抽结果', str(self.num) + '抽出'+ prize+'歪了\nmoney='+str(self.money[0]))
                    self.num = 0
                    self.chance = self.CHANCE
                    self.purple_chance += self.PC_GROW
                    self.isup = 1  # 大保底设置
            elif self.purple_chance > self.purple_odds:  # 出紫了
                if self.purple_isup > 0.5:
                    self.y.append(self.chance)
                    QMessageBox.about(window, '单抽结果', '出紫了,抽出'+random.choice(self.hero.purple_pool[0:2])
                                      +'\nmoney='+str(self.money[0]))
                    self.purple_odds = np.random.rand(1)
                    self.num += 1
                    self.purple_isup = np.random.rand(1)
                    self.purple_chance = self.PC
                    self.chance += self.CHANCE_GROW
                else:  # 紫歪了
                    self.y.append(self.chance)
                    QMessageBox.about(window, '单抽结果', '紫歪了,抽出'+random.choice(self.hero.purple_pool[3:])
                                      +'\nmoney='+str(self.money[0]))
                    self.purple_odds = np.random.rand(1)
                    self.purple_isup = 1
                    self.purple_chance = self.PC
                    self.chance += self.CHANCE_GROW
                    self.num += 1
            else:
                QMessageBox.about(window, '单抽结果', random.choice(self.hero.blue_pool[0:])+"\nmoney="+str(self.money[0]))
                self.y.append(self.chance)
                self.num += 1
                self.chance += self.CHANCE_GROW
                self.purple_chance += self.PC_GROW
        else:
            QMessageBox.about(window, '单抽结果', "余额不足!\nmoney="+str(self.money[0]))

    def ten(self,window):#十连
        if (self.money[0] >= 160):
            self.money[0] -= 160
            lis = []  # 结果列表
            for x in range(10):
                if (self.chance > self.odds):
                    if self.isup > 0.5:
                        self.money[0] += 720
                        self.show_picture(self.hero.gold_pool[0])
                        self.num += 1
                        x = range(0, self.num + 1)
                        self.y.append(self.chance)
                        self.draw_result(x, self.y)
                        self.y = [self.CHANCE]
                        self.odds = np.random.rand(1)
                        lis.append(str(self.num) + '抽出'+self.hero.gold_pool[0])
                        self.num = 0
                        self.chance = self.CHANCE
                        self.purple_chance += self.PC_GROW
                        self.isup = np.random.rand(1)
                    else:
                        self.money[0] += 320
                        prize = random.choice(self.hero.gold_pool[1:])
                        self.show_picture(prize)
                        self.num += 1
                        x = range(0, self.num + 1)
                        self.y.append(self.chance)
                        self.draw_result(x, self.y)
                        self.y = [self.CHANCE]
                        self.odds = np.random.rand(1)
                        lis.append(str(self.num) + '抽出'+prize+',歪了')
                        self.num = 0
                        self.chance = self.CHANCE
                        self.purple_chance += self.PC_GROW
                        self.isup = 1
                elif self.purple_chance > self.purple_odds:
                    if self.purple_isup > 0.5:  # 判断紫色歪没
                        self.y.append(self.chance)
                        self.purple_odds = np.random.rand(1)
                        self.num += 1
                        lis.append('出紫了,抽出'+random.choice(self.hero.purple_pool[0:2]))
                        self.chance += self.CHANCE_GROW
                        self.purple_isup = np.random.rand(1)
                        self.purple_chance = self.PC
                    else:
                        self.y.append(self.chance)
                        self.purple_odds = np.random.rand(1)
                        self.num += 1
                        lis.append('紫歪了,抽出'+random.choice(self.hero.purple_pool[3:]))
                        self.chance += self.CHANCE_GROW
                        self.purple_isup = 1
                        self.purple_chance = self.PC
                else:
                    self.y.append(self.chance)
                    lis.append(random.choice(self.hero.blue_pool[0:]))
                    self.num += 1
                    self.chance += self.CHANCE_GROW
                    self.purple_chance += self.PC_GROW
            information=''
            for x in lis:
                information+=(x + '\n')
            information+='\nmoney='+str(self.money[0])
            QMessageBox.about(window, '十连结果', information)
        else:
            QMessageBox.about(window, '十连结果', '余额不足!\nmoney='+str(self.money[0]))

    def exit(self,window):#退出
        window.close()

