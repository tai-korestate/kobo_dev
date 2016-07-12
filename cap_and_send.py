from gtts import gTTS
import os
import sys
import speech_recognition as sr
import subprocess
import requests
import time


kobo_voice = os.path.join(os.path.abspath(os.curdir), "kobo_voice.mp3")

def processtime():
    date_time = time.ctime()
    cur_time = date_time[-13:-1].replace(":"," ")
    date = date_time[0:-13]
    return (cur_time,date)

def playback(my_text):
    tts = gTTS(text = my_text, lang = "en")
    tts.save(kobo_voice)
    subprocess.call(["cvlc", "--play-and-exit",kobo_voice])
    return


r = sr.Recognizer()
t = processtime()
playback("Hello, I am Kobo, your home assistant.  The date is %s.  Say something when you are ready to begin." % t[1])

with sr.Microphone(sample_rate = 48000,device_index = 2, chunk_size = 2048) as source:
    while True:    
        #print("Say Something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
       # subprocess.call(["cvlc","--play-and-exit","beep.wav"])
        try:
            send_txt = r.recognize_google(audio)
        
            """ 
            with open("test_file.wav", "wb") as f:
            print("Writing Audio...")
            f.write(audio.get_wav_data())
            """

            print(send_txt) 
 
            response = requests.get("http://www.korestate.com/cloud/api/beta/kobo.php?q=%s" % send_txt)
        
            playback(str(response.text))      
        
        except sr.UnknownValueError:
            playback("I'm sorry I could not understand, could you repeat that?")


        except sr.RequestError:
            playback("There has been a connection error, please wait while I re establish a connection")

