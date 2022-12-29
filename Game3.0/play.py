# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/6/26 9:34
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,QMessageBox

class Game():
    def __init__(self,money):
        self.CHANCE = 0.19
        self.PC = 0.11
        self.CHANCE_GROW = 0.0091
        self.PC_GROW = 0.095
        '''以上为常量'''
        self.root = './/Userinfo//userinfo1.csv'
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

    def draw_result(self,x,y):# 画图
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
    def show_picture(self,flag):
        if(flag==1):
            img = cv2.imread(".//Picture//Yasuo.png")
            img = cv2.resize(img,(700,400),interpolation=cv2.INTER_AREA)
            cv2.imshow("Yasuo",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            img = cv2.imread(".//Picture//Zed.jpg")
            img = cv2.resize(img, (700, 400), interpolation=cv2.INTER_AREA)
            cv2.imshow("Zed", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def single(self,window):
        if (self.money[0] >= 16):
            self.money[0] -= 16
            if (self.chance > self.odds):  # 出金了
                if self.isup > 0.5:  # 没歪
                    self.money[0] += 880
                    self.show_picture(1)
                    self.num += 1
                    x = range(0, self.num + 1)
                    self.y.append(self.chance)
                    self.draw_result(x, self.y)
                    self.y = [self.CHANCE]
                    self.odds = np.random.rand(1)
                    QMessageBox.about(window,'单抽结果','出金了,总共抽了' + str(self.num) + '抽\nmoney='+str(self.money[0]))
                    self.num = 0
                    self.chance = self.CHANCE
                    self.purple_chance += self.PC_GROW
                    self.isup = np.random.rand(1)
                else:  # 歪了
                    self.money[0] += 540
                    self.show_picture(0)
                    self.num += 1
                    x = range(0, self.num + 1)
                    self.y.append(self.chance)
                    self.draw_result(x, self.y)
                    self.y = [self.CHANCE]
                    self.odds = np.random.rand(1)
                    QMessageBox.about(window, '单抽结果', '抽了' + str(self.num) + '抽出金,抽歪了！\nmoney='+str(self.money[0]))
                    self.num = 0
                    self.chance = self.CHANCE
                    self.purple_chance += self.PC_GROW
                    self.isup = 1  # 大保底设置
            elif self.purple_chance > self.purple_odds:  # 出紫了
                if self.purple_isup > 0.5:
                    self.y.append(self.chance)
                    QMessageBox.about(window, '单抽结果', '出紫了\nmoney='+str(self.money[0]))
                    self.purple_odds = np.random.rand(1)
                    self.num += 1
                    self.purple_isup = np.random.rand(1)
                    self.purple_chance = self.PC
                    self.chance += self.CHANCE_GROW
                else:  # 紫歪了
                    self.y.append(self.chance)
                    QMessageBox.about(window, '单抽结果', '出紫了,歪了\nmoney='+str(self.money[0]))
                    self.purple_odds = np.random.rand(1)
                    self.purple_isup = 1
                    self.purple_chance = self.PC
                    self.chance += self.CHANCE_GROW
                    self.num += 1
            else:
                QMessageBox.about(window, '单抽结果', "是蓝光\nmoney="+str(self.money[0]))
                self.y.append(self.chance)
                self.num += 1
                self.chance += self.CHANCE_GROW
                self.purple_chance += self.PC_GROW
        else:
            QMessageBox.about(window, '单抽结果', "余额不足!\nmoney="+str(self.money[0]))

    def ten(self,window):
        if (self.money[0] >= 160):
            self.money[0] -= 160
            lis = []  # 结果列表
            for x in range(10):
                if (self.chance > self.odds):
                    if self.isup > 0.5:
                        self.money[0] += 720
                        self.show_picture(1)
                        self.num += 1
                        x = range(0, self.num + 1)
                        self.y.append(self.chance)
                        self.draw_result(x, self.y)
                        self.y = [self.CHANCE]
                        self.odds = np.random.rand(1)
                        lis.append(str(self.num) + '抽出金')
                        self.num = 0
                        self.chance = self.CHANCE
                        self.purple_chance += self.PC_GROW
                        self.isup = np.random.rand(1)
                    else:
                        self.money[0] += 320
                        self.show_picture(0)
                        self.num += 1
                        x = range(0, self.num + 1)
                        self.y.append(self.chance)
                        self.draw_result(x, self.y)
                        self.y = [self.CHANCE]
                        self.odds = np.random.rand(1)
                        lis.append(str(self.num) + '抽出金,歪了')
                        self.num = 0
                        self.chance = self.CHANCE
                        self.purple_chance += self.PC_GROW
                        self.isup = 1
                elif self.purple_chance > self.purple_odds:
                    if self.purple_isup > 0.5:  # 判断紫色歪没
                        self.y.append(self.chance)
                        self.purple_odds = np.random.rand(1)
                        self.num += 1
                        lis.append('出紫了')
                        self.chance += self.CHANCE_GROW
                        self.purple_isup = np.random.rand(1)
                        self.purple_chance = self.PC
                    else:
                        self.y.append(self.chance)
                        self.purple_odds = np.random.rand(1)
                        self.num += 1
                        lis.append('出紫了,歪了')
                        self.chance += self.CHANCE_GROW
                        self.purple_isup = 1
                        self.purple_chance = self.PC
                else:
                    self.y.append(self.chance)
                    lis.append("是蓝光")
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

    def save(self,window):
        data = {'money': self.money[0], 'num': self.num, 'chance': self.chance, 'purple_chance': self.purple_chance,
                'odds': self.odds, 'purple_odds': self.purple_odds, 'y': self.y, 'isup': self.isup,
                'purple_isup': self.purple_isup}
        df1 = pd.DataFrame(data, index=[i for i in range(0, len(self.y))])
        df1.to_csv(self.root, index=False)
        QMessageBox.about(window, '保存结果', "保存成功")

