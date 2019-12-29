import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,1,1000)
y = 3*np.cos(2*np.pi*10*x+0.25*np.pi)
z = 4*np.cos(2*np.pi*10*x+0.75*np.pi)
w = y + z




plt.plot(x,y,'--',label='x1(t)')
plt.plot(x,z,'--',label='x2(t)')
plt.plot(x,w,'-',label='x3(t)')

plt.legend(loc='upper right')
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')

plt.show()