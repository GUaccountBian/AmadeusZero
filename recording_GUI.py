import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import Tk, Button
import threading
import numpy as np

class Recorder:
    def __init__(self, fs=44100, duration=60):
        self.fs = fs  # Sample rate
        self.duration = duration  # Recording duration in seconds
        self.recording = False
        self.myrecording = None

    def start_recording(self):
        self.recording = True
        self.myrecording = np.zeros((self.duration*self.fs, 2))  # 2-channel recording
        threading.Thread(target=self._update_recording).start()

    def stop_recording(self):
        self.recording = False

        # Write as .wav file
        write('./test_audio/output.wav', self.fs, self.myrecording)
        print("The audio file was created successfully!")

    def _update_recording(self):
        for _ in range(self.duration):
            if self.recording:
                self.myrecording[_*self.fs:(_+1)*self.fs, :] = sd.rec(int(self.fs), samplerate=self.fs, channels=2, blocking=True)
            else:
                break
        sd.wait()  # Just in case, wait until all recording is finished

# GUI window
root = Tk()
root.title('Audio Recorder')

recorder = Recorder()

start_button = Button(root, text="Start Recording", command=recorder.start_recording)
start_button.pack()

stop_button = Button(root, text="Stop Recording", command=recorder.stop_recording)
stop_button.pack()

root.mainloop()

