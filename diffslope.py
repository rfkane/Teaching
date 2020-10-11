#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,10,1000)
b = [10,15]
for bi in b:
    y1 = -2*x+bi
    y2 = np.ones(1000)*0
    u = str(bi)
    innerlabel = str('Line 1 where B is ') + u
    plt.plot(x,y1,label = innerlabel )
plt.plot(x,y2,label="Line 2")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# In[ ]:




