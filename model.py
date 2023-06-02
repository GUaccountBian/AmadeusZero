from whisper import Whisper
from funasr_onnx import Paraformer
from format_convert import convert_to_wav

class SpeechToTextModelWrapper:
    def init(self, english_model_path: str, chinese_model_path: str, , language: str='english'):
        # Load English model
        self.language = language.lower()
        if self.language == 'english':
            self.model = Whisper.load_model(english_model_path)
        elif self.language == 'chinese':
            self.model = Paraformer(chinese_model_path, batch_size=1, quantize=True)
        else:
            raise ValueError("Unsupported language. Choose either 'english' or 'chinese'.")
        self.model.to("cuda")

    def transcribe(self, wav_path: str, language: str='english'):
        convert_to_wav(wav_path)
        wav_path = wav_path[:-4] + ".wav"
        if language.lower() == 'english':
            result = self.model.transcribe(wav_path)
            return result['text']
        elif language.lower() == 'chinese':
            result = self.model(wav_path)
            return result
        else:
            raise ValueError("Unsupported language. Choose either 'english' or 'chinese'.")

# Now you can use the class like this:
# wrapper = SpeechToTextModelWrapper("medium.en", "../paraformer-large")
# print(wrapper.transcribe('./test_audio/output.wav', 'english')) # For English transcription
# print(wrapper.transcribe('./test_audio/output.wav', 'chinese')) # For Chinese transcription
