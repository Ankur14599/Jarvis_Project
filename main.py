import webbrowser
import wikipedia
import os 
import random
import numpy as np
import cv2
import psutil

def avengersAssemble():
    return webbrowser.open("https://www.youtube.com/watch?v=FOabQZHT4qY?t=50")

def openGoogle():
    return webbrowser.open('google.com')

def openYoutube():
    return webbrowser.Chrome.open('https://www.youtube.com/channel/UCvt9t3pP0UPYdk-Nkyj5_0g')

def playMusic():
    music_dir = "D:\\Music"
    songs = os.listdir(music_dir)
    num =random.randint(0,len(songs)-1)

    os.startfile(os.path.join(music_dir,songs[num]))
    

def faceReveal():
    img = cv2.imread('images.png',0)
    cv2.imshow('jarvis',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def tellMe():
    answer = ''' my name is jarvis and you have created me. i can help you in a lot of tasks.
            in case of any emergency , just say kill all and see the destruction '''
    return answer



def batteryCheckup():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    status = ""
    if(plugged is True):
        status = "I am Charging"
    else:
        status = "I am Not charging"

    final_output = "{} and i have {} percent power left .".format(status,percent)
    return final_output

    

def openChannelJsFilms():
    return webbrowser.open('https://www.youtube.com/watch?v=5fjmM1dX8oQ')
