# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/6/26 9:34
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
root = './/Userinfo//userinfo.csv'
df = pd.read_csv(root)
class Game():
    CHANCE=0.19
    PC=0.11
    CHANCE_GROW=0.0091
    PC_GROW=0.095
    '''以上为常量'''
    chance = float(df[0:1]['chance'])
    num = int(df[0:1]['num'])
    '''
    chance为抽奖概率
    num为抽奖次数
    isup用于判断是否抽歪
    odds为出金概率
    purple_chance为出紫概率
    '''
    isup = np.random.rand(1)
    choice = '1'
    odds = float(df[0:1]['odds'])
    purple_chance = float(df[0:1]['purple_chance'])
    purple_odds = float(df[0:1]['purple_odds'])
    purple_isup = np.random.rand(1)
    def draw_result(self,x,y):# 画图
        plt.plot(x,y, marker='*',label='chance')
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
    def prize_draw(self,money):
        y = list(df['y'])
        while (self.choice == '1' or self.choice == '2'):
            self.choice = input("money="+str(money)+"\n你选择十连还是单抽(1表示单抽，2表示十连,其他任意键表示退出):")
            if (self.choice == "1"):
                if(money>=16):
                    money-=16
                    if (self.chance > self.odds):  # 出金了
                        if self.isup > 0.5:  # 没歪
                            money+=880
                            self.show_picture(1)
                            self.num += 1
                            x = range(0, self.num + 1)
                            y.append(self.chance)
                            self.draw_result(x, y)
                            y = [self.CHANCE]
                            self.odds = np.random.rand(1)
                            print('\033[0;33;43 m出金了,总共抽了' + str(self.num) + '抽\033[0m',end='')
                            self.num = 0
                            self.chance = self.CHANCE
                            self.purple_chance += self.PC_GROW
                            self.isup = np.random.rand(1)
                        else:  # 歪了
                            money+=540
                            self.show_picture(0)
                            self.num += 1
                            x = range(0, self.num + 1)
                            y.append(self.chance)
                            self.draw_result(x, y)
                            y = [self.CHANCE]
                            self.odds = np.random.rand(1)
                            print('\033[0;33;43 m抽了' + str(self.num) + '抽出金,抽歪了！\033[0m',end='')
                            self.num = 0
                            self.chance = self.CHANCE
                            self.purple_chance += self.PC_GROW
                            self.isup = 1  # 大保底设置
                    elif self.purple_chance>self.purple_odds: # 出紫了
                        if self.purple_isup>0.5:
                            y.append(self.chance)
                            print('\033[0;35;45 m出紫了\033[0m',end='')
                            self.purple_odds = np.random.rand(1)
                            self.num += 1
                            self.purple_isup = np.random.rand(1)
                            self.purple_chance = self.PC
                            self.chance += self.CHANCE_GROW
                        else: # 紫歪了
                            y.append(self.chance)
                            print('\033[0;35;45 m出紫了,歪了\033[0m',end='')
                            self.purple_odds = np.random.rand(1)
                            self.purple_isup = 1
                            self.purple_chance = self.PC
                            self.chance += self.CHANCE_GROW
                            self.num += 1
                    else:
                        y.append(self.chance)
                        print("\033[0;34;44 m是蓝光\033[0m",end='')
                        self.num += 1
                        self.chance += self.CHANCE_GROW
                        self.purple_chance += self.PC_GROW
                else:
                    print("余额不足!")
            elif (self.choice == "2"):
                if(money>=160):
                    money -= 160
                    lis = []  # 结果列表
                    for x in range(10):
                        if (self.chance > self.odds):
                            if self.isup > 0.5:
                                money+=720
                                self.show_picture(1)
                                self.num += 1
                                x = range(0, self.num + 1)
                                y.append(self.chance)
                                self.draw_result(x, y)
                                y = [self.CHANCE]
                                self.odds = np.random.rand(1)
                                lis.append('\033[0;33;43 m'+str(self.num) + '抽出金\033[0m')
                                self.num = 0
                                self.chance = self.CHANCE
                                self.purple_chance += self.PC_GROW
                                self.isup = np.random.rand(1)
                            else:
                                money+=320
                                self.show_picture(0)
                                self.num += 1
                                x = range(0, self.num + 1)
                                y.append(self.chance)
                                self.draw_result(x, y)
                                y = [self.CHANCE]
                                self.odds = np.random.rand(1)
                                lis.append('\033[0;33;43 m'+str(self.num) + '抽出金,歪了\033[0m')
                                self.num = 0
                                self.chance = self.CHANCE
                                self.purple_chance += self.PC_GROW
                                self.isup = 1
                        elif self.purple_chance>self.purple_odds:
                            if self.purple_isup>0.5: # 判断紫色歪没
                                y.append(self.chance)
                                self.purple_odds = np.random.rand(1)
                                self.num += 1
                                lis.append('\033[0;35;45 m出紫了\033[0m')
                                self.chance += self.CHANCE_GROW
                                self.purple_isup = np.random.rand(1)
                                self.purple_chance = self.PC
                            else:
                                y.append(self.chance)
                                self.purple_odds = np.random.rand(1)
                                self.num += 1
                                lis.append('\033[0;35;45 m出紫了,歪了\033[0m')
                                self.chance += self.CHANCE_GROW
                                self.purple_isup = 1
                                self.purple_chance = self.PC
                        else:
                            y.append(self.chance)
                            lis.append("\033[0;34;44 m是蓝光\033[0m")
                            self.num += 1
                            self.chance += self.CHANCE_GROW
                            self.purple_chance += self.PC_GROW
                    for x in lis:
                        print(x+' ',end='')
                else:
                    print('余额不足!')
            else:
                '''
                lis1 = [money for _ in range(0,len(y))]
                lis2 = [self.num for _ in range(0,len(y))]
                lis3 = [self.chance for _ in range(0,len(y))]
                lis4 = [self.purple_chance for _ in range(0,len(y))]
                lis5 = [self.odds for _ in range(0,len(y))]
                lis6 = [self.purple_odds for _ in range(0,len(y))]
                data = {'money':lis1,'num':lis2,'chance':lis3,
                        'purple_chance':lis4,'odds':lis5,'purple_odds':lis6,'y':y}
                '''
                data = {'money': money, 'num': self.num, 'chance': self.chance,
                        'purple_chance': self.purple_chance, 'odds': self.odds, 'purple_odds': self.purple_odds, 'y': y}
                df1 = pd.DataFrame(data,index=[i for i in range(0,len(y))])
                df1.to_csv(root,index=False)
                break
            print('\n')
        print("抽奖完毕",end='')
        return money
