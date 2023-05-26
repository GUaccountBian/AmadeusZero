from funasr_onnx import Paraformer

model_dir = "../paraformer-large"

model = Paraformer(model_dir,batch_size =1, quantize=True)
wav_path = ['./test_audio/output.wav']
result = model(wav_path)
print(result)

