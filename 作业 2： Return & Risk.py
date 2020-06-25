# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:45:34 2020

@author: tang shiyu
"""
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
ts.set_token('ecbe404d5a15079f2467a21d1c34b12fdabde0fcdbca0cd346424681')
pro = ts.pro_api('ecbe404d5a15079f2467a21d1c34b12fdabde0fcdbca0cd346424681')

pro = ts.pro_api()

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#读取股票代码，名称，行业
df01=data[["ts_code","name","industry"]]

#第二题，按行业取4组股票，每组随机取5只,按日期读取行情数据
df_yinhang=df01[df01.industry=="银行"]
df_por1=df_yinhang.sample(n=5, frac=None, replace=False, weights=None, random_state=None, axis=0)
yinhang_01_code=str(df_por1.iat[0,0])
yinhang_02_code=str(df_por1.iat[1,0])
yinhang_03_code=str(df_por1.iat[2,0])
yinhang_04_code=str(df_por1.iat[3,0])
yinhang_05_code=str(df_por1.iat[4,0])
hq_yinhang_01 = pro.daily(ts_code=yinhang_01_code, start_date='20180623', end_date='20200623')
hq_yinhang_02 = pro.daily(ts_code=yinhang_02_code, start_date='20180623', end_date='20200623')
hq_yinhang_03 = pro.daily(ts_code=yinhang_03_code, start_date='20180623', end_date='20200623')
hq_yinhang_04 = pro.daily(ts_code=yinhang_04_code, start_date='20180623', end_date='20200623')
hq_yinhang_05 = pro.daily(ts_code=yinhang_05_code, start_date='20180623', end_date='20200623')

df_dichan=df01[df01.industry=="全国地产"]
df_por2=df_dichan.sample(n=5, frac=None, replace=False, weights=None, random_state=None, axis=0)
dichan_01_code=str(df_por2.iat[0,0])
dichan_02_code=str(df_por2.iat[1,0])
dichan_03_code=str(df_por2.iat[2,0])
dichan_04_code=str(df_por2.iat[3,0])
dichan_05_code=str(df_por2.iat[4,0])
hq_dichan_01 = pro.daily(ts_code=dichan_01_code, start_date='20180623', end_date='20200623')
hq_dichan_02 = pro.daily(ts_code=dichan_02_code, start_date='20180623', end_date='20200623')
hq_dichan_03 = pro.daily(ts_code=dichan_03_code, start_date='20180623', end_date='20200623')
hq_dichan_04 = pro.daily(ts_code=dichan_04_code, start_date='20180623', end_date='20200623')
hq_dichan_05 = pro.daily(ts_code=dichan_05_code, start_date='20180623', end_date='20200623')

df_swzy=df01[df01.industry=="生物制药"]
df_por3=df_swzy.sample(n=5, frac=None, replace=False, weights=None, random_state=None, axis=0)
swzy_01_code=str(df_por3.iat[0,0])
swzy_02_code=str(df_por3.iat[1,0])
swzy_03_code=str(df_por3.iat[2,0])
swzy_04_code=str(df_por3.iat[3,0])
swzy_05_code=str(df_por3.iat[4,0])
hq_swzy_01 = pro.daily(ts_code=swzy_01_code, start_date='20180623', end_date='20200623')
hq_swzy_02 = pro.daily(ts_code=swzy_02_code, start_date='20180623', end_date='20200623')
hq_swzy_03 = pro.daily(ts_code=swzy_03_code, start_date='20180623', end_date='20200623')
hq_swzy_04 = pro.daily(ts_code=swzy_04_code, start_date='20180623', end_date='20200623')
hq_swzy_05 = pro.daily(ts_code=swzy_05_code, start_date='20180623', end_date='20200623')


df_jiudian=df01[df01.industry=="酒店餐饮"]
df_por4=df_jiudian.sample(n=5, frac=None, replace=False, weights=None, random_state=None, axis=0)
jiudian_01_code=str(df_por4.iat[0,0])
jiudian_02_code=str(df_por4.iat[1,0])
jiudian_03_code=str(df_por4.iat[2,0])
jiudian_04_code=str(df_por4.iat[3,0])
jiudian_05_code=str(df_por4.iat[4,0])
hq_jiudian_01 = pro.daily(ts_code=jiudian_01_code, start_date='20180623', end_date='20200623')
hq_jiudian_02 = pro.daily(ts_code=jiudian_02_code, start_date='20180623', end_date='20200623')
hq_jiudian_03 = pro.daily(ts_code=jiudian_03_code, start_date='20180623', end_date='20200623')
hq_jiudian_04 = pro.daily(ts_code=jiudian_04_code, start_date='20180623', end_date='20200623')
hq_jiudian_05 = pro.daily(ts_code=jiudian_05_code, start_date='20180623', end_date='20200623')

'''
组合构建的方法如下，每个组合含有5只股票，组合为每个股票等权重，组合的价格为各个股价格的四分之一加权得到
'''
#提取交易日，收盘价
ge_gu_yinhang_1=hq_yinhang_01[["trade_date","close"]]
ge_gu_yinhang_1.rename(columns = {"close": "close1"},  inplace=True)
ge_gu_yinhang_2=hq_yinhang_02[["trade_date","close"]]
ge_gu_yinhang_2.rename(columns = {"close": "close2"},  inplace=True)
ge_gu_yinhang_3=hq_yinhang_03[["trade_date","close"]]
ge_gu_yinhang_3.rename(columns = {"close": "close3"},  inplace=True)
ge_gu_yinhang_4=hq_yinhang_04[["trade_date","close"]]
ge_gu_yinhang_4.rename(columns = {"close": "close4"},  inplace=True)
ge_gu_yinhang_5=hq_yinhang_05[["trade_date","close"]]
ge_gu_yinhang_5.rename(columns = {"close": "close5"},  inplace=True)

ge_gu_dichan_1=hq_dichan_01[["trade_date","close"]]
ge_gu_dichan_1.rename(columns = {"close": "close1"},  inplace=True)
ge_gu_dichan_2=hq_dichan_02[["trade_date","close"]]
ge_gu_dichan_2.rename(columns = {"close": "close2"},  inplace=True)
ge_gu_dichan_3=hq_dichan_03[["trade_date","close"]]
ge_gu_dichan_3.rename(columns = {"close": "close3"},  inplace=True)
ge_gu_dichan_4=hq_dichan_04[["trade_date","close"]]
ge_gu_dichan_4.rename(columns = {"close": "close4"},  inplace=True)
ge_gu_dichan_5=hq_dichan_05[["trade_date","close"]]
ge_gu_dichan_5.rename(columns = {"close": "close5"},  inplace=True)

ge_gu_swzy_1=hq_swzy_01[["trade_date","close"]]
ge_gu_swzy_1.rename(columns = {"close": "close1"},  inplace=True)
ge_gu_swzy_2=hq_swzy_02[["trade_date","close"]]
ge_gu_swzy_2.rename(columns = {"close": "close2"},  inplace=True)
ge_gu_swzy_3=hq_swzy_03[["trade_date","close"]]
ge_gu_swzy_3.rename(columns = {"close": "close3"},  inplace=True)
ge_gu_swzy_4=hq_swzy_04[["trade_date","close"]]
ge_gu_swzy_4.rename(columns = {"close": "close4"},  inplace=True)
ge_gu_swzy_5=hq_swzy_05[["trade_date","close"]]
ge_gu_swzy_5.rename(columns = {"close": "close5"},  inplace=True)

ge_gu_jiudian_1=hq_jiudian_01[["trade_date","close"]]
ge_gu_jiudian_1.rename(columns = {"close": "close1"},  inplace=True)
ge_gu_jiudian_2=hq_jiudian_02[["trade_date","close"]]
ge_gu_jiudian_2.rename(columns = {"close": "close2"},  inplace=True)
ge_gu_jiudian_3=hq_jiudian_03[["trade_date","close"]]
ge_gu_jiudian_3.rename(columns = {"close": "close3"},  inplace=True)
ge_gu_jiudian_4=hq_jiudian_04[["trade_date","close"]]
ge_gu_jiudian_4.rename(columns = {"close": "close4"},  inplace=True)
ge_gu_jiudian_5=hq_jiudian_05[["trade_date","close"]]
ge_gu_jiudian_5.rename(columns = {"close": "close5"},  inplace=True)

#组合成资产组合
por1 = pd.merge(ge_gu_yinhang_1, ge_gu_yinhang_2,on='trade_date')
por1 = pd.merge(por1, ge_gu_yinhang_3,on='trade_date')
por1 = pd.merge(por1, ge_gu_yinhang_4,on='trade_date')
por1 = pd.merge(por1, ge_gu_yinhang_5,on='trade_date')

por2 = pd.merge(ge_gu_dichan_1, ge_gu_dichan_2,on='trade_date')
por2 = pd.merge(por2, ge_gu_dichan_3,on='trade_date')
por2 = pd.merge(por2, ge_gu_dichan_4,on='trade_date')
por2 = pd.merge(por2, ge_gu_dichan_5,on='trade_date')

por3 = pd.merge(ge_gu_swzy_1, ge_gu_swzy_2,on='trade_date')
por3 = pd.merge(por3, ge_gu_swzy_3,on='trade_date')
por3 = pd.merge(por3, ge_gu_swzy_4,on='trade_date')
por3 = pd.merge(por3, ge_gu_swzy_5,on='trade_date')

por4 = pd.merge(ge_gu_jiudian_1, ge_gu_jiudian_2,on='trade_date')
por4 = pd.merge(por4, ge_gu_jiudian_3,on='trade_date')
por4 = pd.merge(por4, ge_gu_jiudian_4,on='trade_date')
por4 = pd.merge(por4, ge_gu_jiudian_5,on='trade_date')

#按日期排序
por1 = por1.sort_values('trade_date')
por2 = por2.sort_values('trade_date')
por3 = por3.sort_values('trade_date')
por4 = por4.sort_values('trade_date')
#数据处理
por1["price_por"] = por1["close1"]*0.25+por1["close2"]*0.25+por1["close3"]*0.25+por1["close4"]*0.25+por1["close5"]*0.25
por2["price_por"] = por2["close1"]*0.25+por2["close2"]*0.25+por2["close3"]*0.25+por2["close4"]*0.25+por2["close5"]*0.25
por3["price_por"] = por3["close1"]*0.25+por3["close2"]*0.25+por3["close3"]*0.25+por3["close4"]*0.25+por3["close5"]*0.25
por4["price_por"] = por4["close1"]*0.25+por4["close2"]*0.25+por4["close3"]*0.25+por4["close4"]*0.25+por4["close5"]*0.25

#计算对数收益率
por1["r_log_1"]=np.log(por1["price_por"])-np.log(por1["price_por"].shift(1))#底数是e
por2["r_log_2"]=np.log(por2["price_por"])-np.log(por2["price_por"].shift(1))#底数是e
por3["r_log_3"]=np.log(por3["price_por"])-np.log(por3["price_por"].shift(1))#底数是e
por4["r_log_4"]=np.log(por4["price_por"])-np.log(por4["price_por"].shift(1))#底数是e
#绘制收益的分布图
pic01=por1.plot("trade_date","r_log_1")
pic02=por2.plot("trade_date","r_log_2")
pic03=por3.plot("trade_date","r_log_3")
pic04=por4.plot("trade_date","r_log_4")

#计算日均收益
r_mean_por1=por1[["r_log_1"]].mean(0)
r_mean_por2=por2[["r_log_2"]].mean(0)
r_mean_por3=por3[["r_log_3"]].mean(0)
r_mean_por4=por4[["r_log_4"]].mean(0)
#绘制密度图
lan_zi=por1[["trade_date","r_log_1"]]
lan_zi = pd.merge(lan_zi, por2[["trade_date","r_log_2"]],on='trade_date')
lan_zi = pd.merge(lan_zi, por3[["trade_date","r_log_3"]],on='trade_date')
lan_zi = pd.merge(lan_zi, por4[["trade_date","r_log_4"]],on='trade_date')

pic01=lan_zi.plot(kind="kde")
 
