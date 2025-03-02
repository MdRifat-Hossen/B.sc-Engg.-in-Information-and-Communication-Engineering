import numpy as np
import matplotlib.pyplot as plt

def unit(n,k):
    return np.where(n>=k,1,0);



n=np.arange(-5,6)

x=2*unit(n,-2)-unit(n,4)

plt.subplot(1,3,1)
plt.stem(n,x)

plt.show()