import struct
import numpy as np
import wave
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

file='sinusiod.wav'

A = 30000
f = 100
duration = 3
fs = 44100
num_samples = duration*fs

num_channel = 1
sampwidth = 2
num_frames = num_samples
comptype = 'NONE'
compname = 'not compressed'

t = np.linspace(0,duration,num_samples,endpoint=False)
x = A*np.cos(2*np.pi*f*t)

wav_file = wave.open(file,'w')
wav_file.setparams((num_channel,sampwidth,fs,num_frames,comptype,compname))



for s in x:
    wav_file.writeframes(struct.pack('h',int(s)))



wav_file.close()