import whisper
from funasr_onnx import Paraformer
from format_convert import convert_to_wav
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

class SpeechToTextModelWrapper:
    def __init__(self, english_model_path: str, chinese_model_path: str, language: str='english'):
        # Load English model
        self.language = language.lower()
        if self.language == 'english':
            whispermodel = whisper.load_model(english_model_path)
            whispermodel.to("cuda")
            self.model = whispermodel.transcribe     
        elif self.language == 'chinese':
            self.model = Paraformer(chinese_model_path, batch_size =1, quantize=True)
        else:
            raise ValueError("Unsupported language. Choose either 'english' or 'chinese'.")
        

    def transcribe(self, wav_path: str):
        convert_to_wav(wav_path)
        wav_path = wav_path[:-4] + ".wav"
        result = self.model(wav_path)
        return result

# Now you can use the class like this:
wrapper = SpeechToTextModelWrapper("medium.en", "./paraformer-large", 'english')
# print(wrapper.transcribe('./test_audio/output.wav', 'english')) # For English transcription
print(wrapper.transcribe('./test_audio/test_5.wav')) # For Chinese transcription
