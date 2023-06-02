from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

p = pipeline('auto-speech-recognition', 'damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch')
output = p('https://xingchen-data.oss-cn-zhangjiakou.aliyuncs.com/maas/speech/asr_example_ofa.wav',)
print(output)