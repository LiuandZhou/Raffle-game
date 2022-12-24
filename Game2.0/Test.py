# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/23 17:13
import pandas as pd
import numpy as np

money =1440
root = './/Userinfo//userinfo.csv'
'''
num,chance,purple_chance,odds,purple_odds = 0,0.19,0.11,0.50,0.50
y = [0.19,2,3,4,5,6]
lis = [money for _ in range(0,len(y))]
lis1 = [num for _ in range(0,len(y))]
data = {'money':lis,'num':lis1,'chance':chance,
        'purple_chance':purple_chance,'odds':odds,'purple_odds':purple_odds,'y':y}
df = pd.DataFrame(data)
df.to_csv(root,index=True)
'''
df = pd.read_csv(root)
purple_odds = df[0:1]['purple_odds']

print(purple_odds)




