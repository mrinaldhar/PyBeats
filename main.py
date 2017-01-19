import pyaudio
import numpy as np
from colorama import Fore, Back, Style
import random

RATE = 44100
CHUNK = int(RATE/20) # RATE / number of updates per second

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def soundplot(stream):
	data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
	print colors[random.randint(0, len(colors)-1)] + ':'*abs(int(np.median(data)))
	# print colors[random.randint(0, len(colors)-1)] + '|'*np.sqrt(np.mean(np.square(data)))
	#print colors[random.randint(0, len(colors)-1)] + '|'*30*np.log(abs(int(np.median(data)))+0.001)

if __name__=="__main__":
	p=pyaudio.PyAudio()
	stream=p.open(format=pyaudio.paInt16,channels=2,rate=RATE,input=True, frames_per_buffer=CHUNK)
	while 1:
		soundplot(stream)
	stream.stop_stream()
	stream.close()
	p.terminate()
