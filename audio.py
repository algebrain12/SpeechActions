from vosk import Model, KaldiRecognizer
import pyaudio
import json
import functions

def start_to_listen():
    
    model = Model("vosk-model-small-en-in-0.4")
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()
    while True:
        data = stream.read(2048)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            recos = result.get("text", "")
            for i in functions.function_associations:
                if i.lower() in recos.lower():
                    functions.true_associations[functions.function_associations[i]]()
                    print("success")
                    break