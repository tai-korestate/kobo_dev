#!/usr/bin/python3

from gtts import gTTS
import os
import sys
import speech_recognition as sr
import subprocess
import requests
import time
import traceback
import random

ACTIVE = True
ENDPOINT = "http://www.korestate.com/cloud/api/beta/koFuncs.php?q={target}"
kobo_voice = os.path.join(os.path.abspath(os.curdir), "kobo_voice.flac")
DEBUG = True

GOOGLE_SPEECH_KEY = "AlzaSyAQsZ8EA5IWYn09g09TPqVkQxlbU5QxH4l"

#######################################################################
#######################################################################
#######################################################################

def processtime():
    date_time = time.ctime()
    cur_time = date_time[-13:-1].replace(":"," ")
    date = date_time[0:-13]
    return (cur_time,date)

def playback(my_text):
    if ACTIVE == False:
        #print("NOT LISTENING")
        return 

    else:
        print("START SAVE")
        tts = gTTS(text = my_text, lang = "en", debug = DEBUG)
        print("RECEIVED.  SAVING FILE")
        
        tts.save(kobo_voice)
        
        print("FILE SAVED.  LOADING VLC")
        #subprocess.call(["cvlc", "--play-and-exit",kobo_voice])
        #subprocess.Popen(["omxplayer", "-o","local","--vol","100","--amp","15","--no-osd", kobo_voice])
        
        return



"""
def flip_switch(test_bool):
    print("Running flip")
    if test_bool == False:
        playback("Beginning Listening")
        return True
            

    elif test_bool == True:
        playback("Stopping Listening")
        return False
    else:
        return test_bool



def system_process(string,my_active = ACTIVE):
    string = string.lower()
    try:
        
        for test_it in prompts:
            if test_it + " st" in string:
                print("testing  %s ::: %s" % (test_it, string))
                my_active = flip_switch(my_active)
                return (string,my_active)
            else:
                pass
        return (string,my_active)
 
    except:
        traceback.print_exc()
        return (string,my_active)     

def write_audio_to_file():
    
    with open("test_file.wav", "wb") as f:
        print("Writing Audio...")
        f.write(audio.get_wav_data())

"""

##############################################################################
##############################################################################
##############################################################################

prompts = ("kobo","hobo","cobo","coco","como","comeaux","Google")
stop_prompts = ("shut", "stop","quiet","don't listen")
#time.sleep(2)
r = sr.Recognizer()
t = processtime()
#playback("Hello, I am Kobo, your home assistant.  The date is %s.  Say something when you are ready to begin." % t[1])

with sr.Microphone(sample_rate = 48000,device_index = 2, chunk_size = 2048) as source:
    while True:    
        PB = True
        #print("Say Something...",str(ACTIVE))
        
        #r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source)
        #print("Done Listening") 
        #print(audio.get_flac_data())

        ###BEEP###
        #subprocess.Popen(["vlc","--play-and-exit","beep.wav"])
        #subprocess.Popen(["omxplayer","-o","local","beep.wav"])
        
        try:
            #print("Sending cap to google")
            send_txt = r.recognize_google(audio)
            #print("got back from google")
            #print(str(send_txt)) 
           #if PB == True:
            #print("getting response")
            response = requests.get(ENDPOINT.format(target = send_txt))
            #print(response)
            #print("Response received")
            playback(response.text) 


        except sr.UnknownValueError:
            playback("I'm sorry I could not understand, could you repeat that?")


        except sr.RequestError:
            playback("There has been a connection error, please wait while I re establish a connection")













""" 
            if send_txt.lower() in ("hello","hi","hey") + prompts:
                greetings = ("hi!",
                             "Hello to you too!",
                             "Hi, I hope you're having a good day", 
                             "Hello. What's up?")

                PB = False
                playback(random.choice(greetings))
            
            elif set(stop_prompts).intersection(send_txt.lower().split()):

                playback("Stopping Listening")

                ACTIVE = False    
       
            elif set(prompts).intersection(send_txt.lower().split()):
                ACTIVE = True
                PB = True
            
"""
           

