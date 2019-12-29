import numpy as np
import matplotlib.pyplot as plt

n = np.array([0,1,2,3,4])
x = np.array([1,9,4,3,1])# array資料結構
y = [2,4,8,2,6]# list資料結構


plt.plot(n,x,color='green')
plt.stem(n,x)
plt.stem(n,y)



plt.show()



