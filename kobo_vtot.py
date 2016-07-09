#!/usr/bin/env python3

#!/usr/bin/env python3

import os
import speech_recognition as sr
import time
#import pyttsx
from gtts import gTTS
import subprocess



"""
DEPENDENCIES:

- ALSA DEV KIT (sudo apt-get install libasound-dev)
- portaudio (Makefiles in directory)
- pyaudio (sudo pip3 install pyaudio)
- jackd2 (apt-get)
- pyttsx
- tts

"""

ALWAYS_ON = -1

kobo_voice = os.path.join(os.path.abspath(os.curdir),"kobo_voice.mp3")

op_initializers = set(("Cocoa","Coco","hello","qubool","comaeux","hobo","Kopo","Gobo","Como","go","Kobo"))

r = sr.Recognizer()


def sys_checks(my_text):
    if "always" in my_text and "on" in my_text:
        playback("Initializing Always On Mode")
        ALWAYS_ON *= -1

    return my_text

def process_time():
    date_time = time.ctime()
    cur_time = date_time[-13:-1].replace(":", " ")
    date = date_time[0:-13]
    print (cur_time, date)
    return (cur_time,date) 

def playback(my_text):
    tts = gTTS(text = my_text, lang = "en")
    tts.save(kobo_voice)
    subprocess.call(["cvlc","--play-and-exit", kobo_voice])
    del tts
    return

t = process_time()
print("T is %s" % str(t))
playback("Hello, I am Kobo, your KorEstate home assistant. the date is %s.  I am ready to take any requests." %  (t[1]))

while True:


    with sr.Microphone(sample_rate = 44100, device_index =3) as source:
        #print("Speak Now")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source) 

    try:
        input_audio = r.recognize_google(audio)
        print(input_audio.split(' '))
          
        if ALWAYS_ON == 1:
            my_text = ("You said %s" % input_audio)
            playback(sys_checks(my_text))     
 
        elif ALWAYS_ON == -1 and op_initializers.intersection(input_audio.split()): #Checks for Kobo
            #print("You said: %s" % input_audio[5:])                 
            my_text = ("You said %s" % input_audio[5:])
            playback(sys_checks(my_text))


        else:
            pass


    except sr.UnknownValueError:
        if ALWAYS_ON == True:
            playback("I'm Sorry I could not understand")

        else:
            pass

    except sr.RequestError as e:
        playback("Could you say that again?")










