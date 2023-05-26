import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import Tk, Button
import threading

class Recorder:
    def __init__(self, fs=44100):
        self.fs = fs  # Sample rate
        self.recording = False
        self.myrecording = None

    def start_recording(self):
        self.recording = True
        self.myrecording = sd.rec(int(10 * self.fs), samplerate=self.fs, channels=2)
        threading.Thread(target=self._update_recording).start()

    def stop_recording(self):
        self.recording = False
        sd.wait()  # Wait until recording is finished

        # Write as .wav file
        write('./test_audio/output.wav', self.fs, self.myrecording)
        print("The audio file was created successfully!")

    def _update_recording(self):
        while self.recording:
            sd.wait()

# GUI window
root = Tk()
root.title('Audio Recorder')

recorder = Recorder()

start_button = Button(root, text="Start Recording", command=recorder.start_recording)
start_button.pack()

stop_button = Button(root, text="Stop Recording", command=recorder.stop_recording)
stop_button.pack()

root.mainloop()
