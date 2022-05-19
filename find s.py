#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
data=pd.read_csv("play.csv")
print(data,"n")


# In[5]:


d=np.array(data)[:,:-1]
print("n the attributes are: ",d)


# In[6]:


tar=np.array(data)[:,-1]
print("n the target is:", tar)


# In[27]:





# In[40]:


def train(con, tar):
    for i, val in enumerate(tar):
        if val == 'yes':
            specific_h = con[i].copy()
            break
            
    for i, val in enumerate(con):
        if tar[i] == 'yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
            print(specific_h)


# In[41]:


print(train(d,tar))


# In[ ]:




