
# coding: utf-8

# In[1]:

import pandas as pd
import nsepy as ns
from datetime import date


# In[2]:

stocks = pd.read_csv("stocklist.csv")


# In[3]:

stocks


# In[4]:

expiry = date(2017,2,23),date(2017,3,30),date(2017,4,27),date(2017,5,25),date(2017,6,29),
date(2017,7,27),date(2017,8,31),date(2017,9,28),date(2017,10,26),date(2017,11,30),date(2017,12,28) ]


# In[5]:

futureframe = []
for dt in expiry :
    expiry_dt = dt
    for idx,name in stocks.iterrows():
            try :
                Symbol = name['SYMBOL']
                df = ns.get_history(symbol=Symbol,start=date(2016,11,1),end=date(2017,12,31),
                        futures= True,
                        expiry_date = expiry_dt
                         )
                df['turnover_cr'] = df['Turnover']/1000000000000
                futureframe.append(df)
            except:
                print ("error at symbol", name['SYMBOL'])


# In[6]:

futures = pd.concat(futureframe)
futures.to_csv('futuresdata.csv')


# In[ ]:




# In[7]:




# In[ ]:



