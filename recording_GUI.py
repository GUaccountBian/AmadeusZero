import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import Tk, Button
import threading
import numpy as np

class Recorder:
    def __init__(self, max_duration=120, fs=44100):
        self.fs = fs  # Sample rate
        self.max_duration = max_duration  # Maximum recording duration in seconds
        self.recording = False
        self.current_duration = 0  # Actual duration of recording
        self.myrecording = np.zeros((self.max_duration*self.fs, 2))  # 2-channel recording

    def start_recording(self):
        self.recording = True
        threading.Thread(target=self._update_recording).start()

    def stop_recording(self):
        self.recording = False

        # Keep only recorded data
        self.myrecording = self.myrecording[:self.current_duration*self.fs, :]

        # Convert to 16-bit data
        self.myrecording = np.int16(self.myrecording * 32767)

        # Write as .wav file
        write('./test_audio/output.wav', self.fs, self.myrecording)
        print("The audio file was created successfully!")

    def _update_recording(self):
        for _ in range(self.max_duration):
            if self.recording:
                self.myrecording[_*self.fs:(_+1)*self.fs, :] = sd.rec(int(self.fs), samplerate=self.fs, channels=2, blocking=True)
                self.current_duration += 1
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


