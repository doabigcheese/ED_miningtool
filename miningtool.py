import time
import re
import win32com.client 
import io
import glob
import os
from playsound import playsound


#Installation win32com: python -m pip install pywin32
#v1.0 doabigcheese
#Configuration:
filter = 14 #über dieser Prozentzahl gibt es eine Sprachausgabe
###################

#get latest log file of ED (so start the script only AFTER ED)
list_of_files = glob.glob('C:/Users/Stefan/Saved Games/Frontier Developments/Elite Dangerous/Journal*.log')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
fn=latest_file


def watch(fn, words):
    fp = open(fn, 'r')
    fp.seek(0, io.SEEK_END) #ans Ende vom Log springen und ab da überwachen
    while True:
        new = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if new:
            for word in words:
                if word in new:
                    yield (word, new)
        else:
            time.sleep(0.5)


words = ['ProspectedAsteroid']
speaker = win32com.client.Dispatch("SAPI.SpVoice")

#Beispiel Core: { "timestamp":"2020-09-14T18:07:42Z", "event":"ProspectedAsteroid", "Materials":[ { "Name":"Samarium", "Proportion":37.981560 } ], "MotherlodeMaterial":"Painite", "MotherlodeMaterial_Localised":"Painit", "Content":"$AsteroidMaterialContent_Low;", "Content_Localised":"Materialgehalt: Niedrig", "Remaining":100.000000 }

for hit_word, hit_sentence in watch(fn, words):
    try:
        start = 'Name_Localised":"Painit", "Proportion":'
        end = ' }'
        #{ "Name":"Painite", "Name_Localised":"Painit", "Proportion":19.810108 }
        result = re.search('%s(.*)%s' % (start, end), hit_sentence).group(1).split(' ')[0]
        print(result)
        if (round(float(result)) > filter):
            speaker.Speak(round(float(result)))
    except:
        print(".")
        playsound(os.getcwd() + '\\zonk.mp3')
    try:
    #Core gefunden?
        start2 = 'MotherlodeMaterial_Localised":"'
        end2 = '"'
        result2 = re.search('%s(.*)%s' % (start2, end2), hit_sentence).group(1).split(',')[0]
        print(result2)
        speaker.Speak("Kern gefunden " + result2)
    except:
        print("..")