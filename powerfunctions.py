import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0.0, 2, 1000)
m = [.5,1,2]
for mi in m:
    y1 = x**mi
    u = str(mi)
    looplabel = str('x^m where m is ') + u
    plt.plot(x,y1,label =  looplabel )
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
