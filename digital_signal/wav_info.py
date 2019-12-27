import wave
#from scipy.io.wavfile import read
#import matplotlib.pyplot as plt


wav = wave.open('D:\\python_venv\\practice-venv\\DSP python practice\\digital_signal\\handel.wav','rb')
#wave.open("欲開啟檔案位置") 重要

num_channels = wav.getnchannels()
sampwidth = wav.getsampwidth()
frame_rate = wav.getframerate()
num_frame = wav.getnframes()
comptype = wav.getcomptype()
compname = wav.getcompname()

print("NC=",num_channels)
print("SW=",sampwidth)
print("SR=",frame_rate)
print("NF=",num_frame)
print("comptype=",comptype)
print("compname=",compname)

wav.close()
