
# coding: utf-8

# In[ ]:

import pandas as pd
import nsepy as ns
from datetime import date
import math


# In[ ]:

stocks = pd.read_csv("stocklist.csv").head(2)


# In[ ]:

eqframe = []
for idx,name in stocks.iterrows():
    try :
        Symbol = name['SYMBOL']
        df = ns.get_history(symbol=Symbol,start=date(2017,12,1),end=date(2017,12,30))
        df['turnover_cr'] = df['Turnover']/1000000000000
        df['Var'] = ((df['High']- df['Low'])/df['VWAP'])*100
        df['Move'] = ((df['Close']- df['Open'])/df['VWAP'])*100
        df['Varbucket'] = df['Var'].map(lambda x: math.floor(x))
        eqframe.append(df)
    except:
        print ("error at symbol", name['SYMBOL'])


# In[ ]:

df = ns.get_history(symbol='SBIN',start=date(2017,12,1),end=date(2017,12,30))


# In[ ]:

eq = pd.concat(eqframe)
eq.to_csv('historydata.csv')


# In[ ]:




# In[ ]:



