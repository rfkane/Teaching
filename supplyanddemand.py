import numpy as np
from matplotlib import pyplot as plt

B1 = 40
B2 = 0

Q=np.linspace(0,50,1000)
Demand = 100-2*Q
Supply1 = B1+3*Q
Supply2 = B2+3*Q

if B2 > B1:
    u = "Decreased Supply"
else:
    u = "Increased Supply"


plt.plot(Q,Demand,label = "Demand")
plt.plot(Q,Supply1,label= "Supply")
plt.plot(Q,Supply2,label= u)
plt.legend()
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.show()


