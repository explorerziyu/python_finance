# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:10:20 2020

@author: tang shiyu
"""
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
ts.set_token('ecbe404d5a15079f2467a21d1c34b12fdabde0fcdbca0cd346424681')
pro = ts.pro_api('ecbe404d5a15079f2467a21d1c34b12fdabde0fcdbca0cd346424681')
#读取所有上市股票代码，名称，行业
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#随机生成20只股票
df_por=data.sample(n=20, frac=None, replace=False, weights=None, random_state=None, axis=0)
#取得这20只股票地两年内地日行情数据
code1=str(df_por.iat[0,0])
code2=str(df_por.iat[1,0])
code3=str(df_por.iat[2,0])
code4=str(df_por.iat[3,0])
code5=str(df_por.iat[4,0])
code6=str(df_por.iat[5,0])
code7=str(df_por.iat[6,0])
code8=str(df_por.iat[7,0])
code9=str(df_por.iat[8,0])
code10=str(df_por.iat[9,0])
code11=str(df_por.iat[10,0])
code12=str(df_por.iat[11,0])
code13=str(df_por.iat[12,0])
code14=str(df_por.iat[13,0])
code15=str(df_por.iat[14,0])
code16=str(df_por.iat[15,0])
code17=str(df_por.iat[16,0])
code18=str(df_por.iat[17,0])
code19=str(df_por.iat[18,0])
code20=str(df_por.iat[19,0])

#先计算一个股票的收益的标准差
#不断地往组合中加入新的股票，计算组合收益地标准差
hq01 = pro.daily(ts_code=code1, start_date='20180623', end_date='20200623')
hq01=hq01[["trade_date","close"]]
hq01.rename(columns = {"close": "close1"},  inplace=True)
hq01 = hq01.sort_values('trade_date')
hq01["r_log_01"]=np.log(hq01["close1"])-np.log(hq01["close1"].shift(1))#底数是e
std=hq01[["r_log_01"]].std()

hq02 = pro.daily(ts_code=code2, start_date='20180623', end_date='20200623')
hq02.rename(columns = {"close": "close2"},  inplace=True)
hq02 = hq02.sort_values('trade_date')
hq01=pd.merge(hq01, hq02[["trade_date","close2"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*0.5+hq01["close2"]*0.5
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_2=hq01[["r_por_log"]].std()
row=std_2["r_por_log"]
std.loc[1]=row

hq03 = pro.daily(ts_code=code3, start_date='20180623', end_date='20200623')
hq03.rename(columns = {"close": "close3"},  inplace=True)
hq03 = hq03.sort_values('trade_date')
hq01=pd.merge(hq01, hq03[["trade_date","close3"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/3)+hq01["close2"]*(1/3)+hq01["close3"]*(1/3)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_3=hq01[["r_por_log"]].std()
row=std_3["r_por_log"]
std.loc[2]=row

hq04 = pro.daily(ts_code=code4, start_date='20180623', end_date='20200623')
hq04.rename(columns = {"close": "close4"},  inplace=True)
hq04 = hq04.sort_values('trade_date')
hq01=pd.merge(hq01, hq04[["trade_date","close4"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/4)+hq01["close2"]*(1/4)+hq01["close3"]*(1/4)+hq01["close4"]*(1/4)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_4=hq01[["r_por_log"]].std()
row=std_4["r_por_log"]
std.loc[3]=row

hq05 = pro.daily(ts_code=code5, start_date='20180623', end_date='20200623')
hq05 = pro.daily(ts_code=code5, start_date='20180623', end_date='20200623')
hq05.rename(columns = {"close": "close5"},  inplace=True)
hq05 = hq05.sort_values('trade_date')
hq01=pd.merge(hq01, hq05[["trade_date","close5"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/5)+hq01["close2"]*(1/5)+hq01["close3"]*(1/5)+hq01["close4"]*(1/5)+hq01["close5"]*(1/5)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_5=hq01[["r_por_log"]].std()
row=std_5["r_por_log"]
std.loc[4]=row

hq06 = pro.daily(ts_code=code6, start_date='20180623', end_date='20200623')
hq06 = pro.daily(ts_code=code6, start_date='20180623', end_date='20200623')
hq06.rename(columns = {"close": "close6"},  inplace=True)
hq06 = hq06.sort_values('trade_date')
hq01=pd.merge(hq01, hq06[["trade_date","close6"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/6)+hq01["close2"]*(1/6)+hq01["close3"]*(1/6)+hq01["close4"]*(1/6)+hq01["close5"]*(1/6)+hq01["close6"]*(1/6)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_6=hq01[["r_por_log"]].std()
row=std_6["r_por_log"]
std.loc[5]=row

hq07 = pro.daily(ts_code=code7, start_date='20180623', end_date='20200623')
hq07 = pro.daily(ts_code=code7, start_date='20180623', end_date='20200623')
hq07.rename(columns = {"close": "close7"},  inplace=True)
hq07 = hq07.sort_values('trade_date')
hq01=pd.merge(hq01, hq07[["trade_date","close7"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/7)+hq01["close2"]*(1/7)+hq01["close3"]*(1/7)+hq01["close4"]*(1/7)+hq01["close5"]*(1/7)+hq01["close6"]*(1/7)+hq01["close7"]*(1/7)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_7=hq01[["r_por_log"]].std()
row=std_7["r_por_log"]
std.loc[6]=row

hq08 = pro.daily(ts_code=code8, start_date='20180623', end_date='20200623')
hq08 = pro.daily(ts_code=code8, start_date='20180623', end_date='20200623')
hq08.rename(columns = {"close": "close8"},  inplace=True)
hq08 = hq08.sort_values('trade_date')
hq01=pd.merge(hq01, hq08[["trade_date","close8"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/8)+hq01["close2"]*(1/8)+hq01["close3"]*(1/8)+hq01["close4"]*(1/8)+hq01["close5"]*(1/8)+hq01["close6"]*(1/8)+hq01["close7"]*(1/8) +hq01["close8"]*(1/8)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_8=hq01[["r_por_log"]].std()
row=std_8["r_por_log"]
std.loc[7]=row

hq09 = pro.daily(ts_code=code9, start_date='20180623', end_date='20200623')
hq09 = pro.daily(ts_code=code9, start_date='20180623', end_date='20200623')
hq09.rename(columns = {"close": "close9"},  inplace=True)
hq09 = hq09.sort_values('trade_date')
hq01=pd.merge(hq01, hq09[["trade_date","close9"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/9)+hq01["close2"]*(1/9)+hq01["close3"]*(1/9)+hq01["close4"]*(1/9)+hq01["close5"]*(1/9)+hq01["close6"]*(1/9)+hq01["close7"]*(1/9) +hq01["close8"]*(1/9) +hq01["close9"]*(1/9)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_9=hq01[["r_por_log"]].std()
row=std_9["r_por_log"]
std.loc[8]=row

hq010 = pro.daily(ts_code=code10, start_date='20180623', end_date='20200623')
hq10 = pro.daily(ts_code=code10, start_date='20180623', end_date='20200623')
hq10.rename(columns = {"close": "close10"},  inplace=True)
hq10 = hq10.sort_values('trade_date')
hq01=pd.merge(hq01, hq10[["trade_date","close10"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/10)+hq01["close2"]*(1/10)+hq01["close3"]*(1/10)+hq01["close4"]*(1/10)+hq01["close5"]*(1/10)+hq01["close6"]*(1/10)+hq01["close7"]*(1/10) +hq01["close8"]*(1/10) +hq01["close9"]*(1/10) +hq01["close10"]*(1/10)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_10=hq01[["r_por_log"]].std()
row=std_10["r_por_log"]
std.loc[9]=row

hq011 = pro.daily(ts_code=code11, start_date='20180623', end_date='20200623')
hq11 = pro.daily(ts_code=code11, start_date='20180623', end_date='20200623')
hq11.rename(columns = {"close": "close11"},  inplace=True)
hq11 = hq11.sort_values('trade_date')
hq01=pd.merge(hq01, hq11[["trade_date","close11"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/11)+hq01["close2"]*(1/11)+hq01["close3"]*(1/11)+hq01["close4"]*(1/11)+hq01["close5"]*(1/11)+hq01["close6"]*(1/11)+hq01["close7"]*(1/11) +hq01["close8"]*(1/11) +hq01["close9"]*(1/11) +hq01["close10"]*(1/11) +hq01["close11"]*(1/11)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_11=hq01[["r_por_log"]].std()
row=std_11["r_por_log"]
std.loc[10]=row

hq012 = pro.daily(ts_code=code12, start_date='20180623', end_date='20200623')
hq12 = pro.daily(ts_code=code12, start_date='20180623', end_date='20200623')
hq12.rename(columns = {"close": "close12"},  inplace=True)
hq12 = hq12.sort_values('trade_date')
hq01=pd.merge(hq01, hq12[["trade_date","close12"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/12)+hq01["close2"]*(1/12)+hq01["close3"]*(1/12)+hq01["close4"]*(1/12)+hq01["close5"]*(1/12)+hq01["close6"]*(1/12)+hq01["close7"]*(1/12) +hq01["close8"]*(1/12) +hq01["close9"]*(1/12) +hq01["close10"]*(1/12) +hq01["close11"]*(1/12) +hq01["close12"]*(1/12)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_12=hq01[["r_por_log"]].std()
row=std_12["r_por_log"]
std.loc[11]=row

hq013 = pro.daily(ts_code=code13, start_date='20180623', end_date='20200623')
hq13 = pro.daily(ts_code=code13, start_date='20180623', end_date='20200623')
hq13.rename(columns = {"close": "close13"},  inplace=True)
hq13 = hq13.sort_values('trade_date')
hq01=pd.merge(hq01, hq13[["trade_date","close13"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/13)+hq01["close2"]*(1/13)+hq01["close3"]*(1/13)+hq01["close4"]*(1/13)+hq01["close5"]*(1/13)+hq01["close6"]*(1/13)+hq01["close7"]*(1/13) +hq01["close8"]*(1/13) +hq01["close9"]*(1/13) +hq01["close10"]*(1/13) +hq01["close11"]*(1/13) +hq01["close12"]*(1/13) +hq01["close13"]*(1/13)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_13=hq01[["r_por_log"]].std()
row=std_13["r_por_log"]
std.loc[12]=row

hq014 = pro.daily(ts_code=code14, start_date='20180623', end_date='20200623')
hq14 = pro.daily(ts_code=code14, start_date='20180623', end_date='20200623')
hq14.rename(columns = {"close": "close14"},  inplace=True)
hq14 = hq14.sort_values('trade_date')
hq01=pd.merge(hq01, hq14[["trade_date","close14"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/14)+hq01["close2"]*(1/14)+hq01["close3"]*(1/14)+hq01["close4"]*(1/14)+hq01["close5"]*(1/14)+hq01["close6"]*(1/14)+hq01["close7"]*(1/14) +hq01["close8"]*(1/14) +hq01["close9"]*(1/14) +hq01["close10"]*(1/14) +hq01["close11"]*(1/14) +hq01["close12"]*(1/14) +hq01["close13"]*(1/14) +hq01["close14"]*(1/14)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_14=hq01[["r_por_log"]].std()
row=std_14["r_por_log"]
std.loc[13]=row

hq015 = pro.daily(ts_code=code15, start_date='20180623', end_date='20200623')
hq15 = pro.daily(ts_code=code15, start_date='20180623', end_date='20200623')
hq15.rename(columns = {"close": "close15"},  inplace=True)
hq15 = hq15.sort_values('trade_date')
hq01=pd.merge(hq01, hq15[["trade_date","close15"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/15)+hq01["close2"]*(1/15)+hq01["close3"]*(1/15)+hq01["close4"]*(1/15)+hq01["close5"]*(1/15)+hq01["close6"]*(1/15)+hq01["close7"]*(1/15) +hq01["close8"]*(1/15) +hq01["close9"]*(1/15) +hq01["close10"]*(1/15) +hq01["close11"]*(1/15) +hq01["close12"]*(1/15) +hq01["close13"]*(1/15) +hq01["close14"]*(1/15) +hq01["close15"]*(1/15)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_15=hq01[["r_por_log"]].std()
row=std_15["r_por_log"]
std.loc[14]=row

hq016 = pro.daily(ts_code=code16, start_date='20180623', end_date='20200623')
hq16 = pro.daily(ts_code=code16, start_date='20180623', end_date='20200623')
hq16.rename(columns = {"close": "close16"},  inplace=True)
hq16 = hq16.sort_values('trade_date')
hq01=pd.merge(hq01, hq16[["trade_date","close16"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/16)+hq01["close2"]*(1/16)+hq01["close3"]*(1/16)+hq01["close4"]*(1/16)+hq01["close5"]*(1/16)+hq01["close6"]*(1/16)+hq01["close7"]*(1/16) +hq01["close8"]*(1/16) +hq01["close9"]*(1/16) +hq01["close10"]*(1/16) +hq01["close11"]*(1/16) +hq01["close12"]*(1/16) +hq01["close13"]*(1/16) +hq01["close14"]*(1/16) +hq01["close15"]*(1/16) +hq01["close16"]*(1/16)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_16=hq01[["r_por_log"]].std()
row=std_16["r_por_log"]
std.loc[15]=row

hq017 = pro.daily(ts_code=code17, start_date='20180623', end_date='20200623')
hq17 = pro.daily(ts_code=code17, start_date='20180623', end_date='20200623')
hq17.rename(columns = {"close": "close17"},  inplace=True)
hq17 = hq17.sort_values('trade_date')
hq01=pd.merge(hq01, hq17[["trade_date","close17"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/17)+hq01["close2"]*(1/17)+hq01["close3"]*(1/17)+hq01["close4"]*(1/17)+hq01["close5"]*(1/17)+hq01["close6"]*(1/17)+hq01["close7"]*(1/17) +hq01["close8"]*(1/17) +hq01["close9"]*(1/17) +hq01["close10"]*(1/17) +hq01["close11"]*(1/17) +hq01["close12"]*(1/17) +hq01["close13"]*(1/17) +hq01["close14"]*(1/17) +hq01["close15"]*(1/17) +hq01["close16"]*(1/17) +hq01["close17"]*(1/17)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_17=hq01[["r_por_log"]].std()
row=std_17["r_por_log"]
std.loc[16]=row

hq018 = pro.daily(ts_code=code18, start_date='20180623', end_date='20200623')
hq18 = pro.daily(ts_code=code18, start_date='20180623', end_date='20200623')
hq18.rename(columns = {"close": "close18"},  inplace=True)
hq18 = hq18.sort_values('trade_date')
hq01=pd.merge(hq01, hq18[["trade_date","close18"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/18)+hq01["close2"]*(1/18)+hq01["close3"]*(1/18)+hq01["close4"]*(1/18)+hq01["close5"]*(1/18)+hq01["close6"]*(1/18)+hq01["close7"]*(1/18) +hq01["close8"]*(1/18) +hq01["close9"]*(1/18) +hq01["close10"]*(1/18) +hq01["close11"]*(1/18) +hq01["close12"]*(1/18) +hq01["close13"]*(1/18) +hq01["close14"]*(1/18) +hq01["close15"]*(1/18) +hq01["close16"]*(1/18) +hq01["close17"]*(1/18) +hq01["close18"]*(1/18)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_18=hq01[["r_por_log"]].std()
row=std_18["r_por_log"]
std.loc[17]=row

hq019 = pro.daily(ts_code=code19, start_date='20180623', end_date='20200623')
hq19 = pro.daily(ts_code=code19, start_date='20180623', end_date='20200623')
hq19.rename(columns = {"close": "close19"},  inplace=True)
hq19 = hq19.sort_values('trade_date')
hq01=pd.merge(hq01, hq19[["trade_date","close19"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/19)+hq01["close2"]*(1/19)+hq01["close3"]*(1/19)+hq01["close4"]*(1/19)+hq01["close5"]*(1/19)+hq01["close6"]*(1/19)+hq01["close7"]*(1/19) +hq01["close8"]*(1/19) +hq01["close9"]*(1/19) +hq01["close10"]*(1/19) +hq01["close11"]*(1/19) +hq01["close12"]*(1/19) +hq01["close13"]*(1/19) +hq01["close14"]*(1/19) +hq01["close15"]*(1/19) +hq01["close16"]*(1/19) +hq01["close17"]*(1/19) +hq01["close18"]*(1/19) +hq01["close19"]*(1/19)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_19=hq01[["r_por_log"]].std()
row=std_19["r_por_log"]
std.loc[18]=row

hq020 = pro.daily(ts_code=code20, start_date='20180623', end_date='20200623')
hq20 = pro.daily(ts_code=code20, start_date='20180623', end_date='20200623')
hq20.rename(columns = {"close": "close20"},  inplace=True)
hq20 = hq20.sort_values('trade_date')
hq01=pd.merge(hq01, hq20[["trade_date","close20"]],on='trade_date')
hq01["r_por"]=hq01["close1"]*(1/20)+hq01["close2"]*(1/20)+hq01["close3"]*(1/20)+hq01["close4"]*(1/20)+hq01["close5"]*(1/20)+hq01["close6"]*(1/20)+hq01["close7"]*(1/20) +hq01["close8"]*(1/20) +hq01["close9"]*(1/20) +hq01["close10"]*(1/20) +hq01["close11"]*(1/20) +hq01["close12"]*(1/20) +hq01["close13"]*(1/20) +hq01["close14"]*(1/20) +hq01["close15"]*(1/20) +hq01["close16"]*(1/20) +hq01["close17"]*(1/20) +hq01["close18"]*(1/20) +hq01["close19"]*(1/20) +hq01["close20"]*(1/20)
hq01["r_por_log"]=np.log(hq01["r_por"])-np.log(hq01["r_por"].shift(1))#底数是e
std_20=hq01[["r_por_log"]].std()
row=std_20["r_por_log"]
std.loc[19]=row

#绘制折线图
pict=std.plot(kind="line")