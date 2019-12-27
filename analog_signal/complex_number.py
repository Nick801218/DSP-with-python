import numpy as np
import matplotlib.pyplot as plt
x = 3
y = np.complex(4j)
z = x + y
print('z=',z)
Normz = abs(z)
print('Magnitude=',Normz)
Phase_rad = np.arctan(abs(y)/x)#反三角函數算出來都是弧度
Phase_deg = Phase_rad*180/np.pi#弧度轉角度
print('Phase_deg=',Phase_deg)

