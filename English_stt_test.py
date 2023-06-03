import whisper
import time
from format_convert import convert_to_wav

model = whisper.load_model("medium.en")
model.to("cuda")

print("Start Transcribe")
start_time = time.time()
convert_to_wav("./test_audio/test_5.m4a")
result = model.transcribe("./test_audio/test_5.wav")
end_time = time.time()

elapsed_time = end_time - start_time

print(f"The trascribe process took {elapsed_time} seconds to complete!")
print(result["text"])
