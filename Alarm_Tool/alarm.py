from pygame import mixer
import time

def sound():
    mixer.init()
    mixer.music.load('C:\\Users\\FatemahSarah\\Desktop\\New folder\\Alarm_Tool\\alarm.mp3')

def alarm():
    hour = int(raw_input('Enter the hour:'))
    min = int(raw_input('Enter the minute:'))  
    sec = int(raw_input('Enter the second:'))

    numOfSoundPlays = 5

    alarmTime = str(hour) + str(min) + str(sec)
    print ('The alarm is set for' + alarmTime.strftime("%H:%M:%S"))


