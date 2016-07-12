from gtts import gTTS
import os
import sys
import speech_recognition as sr
import subprocess
import requests

kobo_voice = os.path.join(os.path.abspath(os.curdir), "kobo_voice.mp3")

def playback(my_text):
    tts = gTTS(text = my_text, lang = "en")
    print("Beginning Writing")
    tts.save(kobo_voice)
    print("Finished Writing")
    subprocess.Popen(["cvlc","-I dummy", "--play-and-exit",kobo_voice])
    print("Finished opening VLC")
    return


r = sr.Recognizer()

with sr.Microphone(sample_rate = 48000, device_index = 2, chunk_size = 2048) as source:
    while True:
        print("Say Something...")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        send_txt = r.recognize_google(audio)

        
        with open("test_file.wav", "wb") as f:
            print("Writing Audio...")
            f.write(audio.get_wav_data())
        

        print(send_txt)
        print('sending req')
        response = requests.get("http://www.korestate.com/cloud/api/beta/kobo.php?q=%s" % send_txt)
        print(response.text)
        playback(str(response.text))
