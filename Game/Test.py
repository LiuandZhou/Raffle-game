# 学校：湖南第一师范学院
# 作者：刘浩铃
# 时间：2022/12/23 17:13
import pandas as pd
import os.path
import csv
root = './/Userinfo//userinfo.csv'
if(os.path.exists(root)):
    a=pd.read_csv(root)
else:
    a=1400
    df = pd.DataFrame({'money':a})
    df.to_csv('userinfo.csv')