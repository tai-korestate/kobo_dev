import speech_recognition as sr
from urllib import request
import subprocess

r = sr.Recognizer()

with sr.Microphone(sample_rate = 48000, device_index = 2, chunk_size = 2048) as source:
    while True:
        print("Say Something...")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        print(r.recognize_google(audio))

        with open("test_file.wav", "wb") as f:
            print("Writing Audio...")
            f.write(audio.get_wav_data())
