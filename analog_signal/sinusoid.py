import numpy as np
import matplotlib.pyplot as plt
a = np.pi
x = np.linspace(0, 1, 44100,endpoint=False)#(1)取樣點必須足夠多,否則弦波會失真
                                          #(2)endpoint=False表不包含1這個點
y = np.cos((2*a*20*x))
plt.plot(x, y)

plt.xlabel('t(sec)')
plt.ylabel('Amplitude')

plt.show()