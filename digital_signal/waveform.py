from scipy.io.wavfile import read
import matplotlib.pyplot as plt

#filename = input("D:\python_venv\practice-venv\DSP python practice\digital_signal\handel.wav")
sampling_rate,x = read("D:\\python_venv\\practice-venv\\DSP python practice\\digital_signal\\fart.wav")
#read("欲開啟檔案位置") 重要
print(sampling_rate)
plt.plot(x)
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.show()
