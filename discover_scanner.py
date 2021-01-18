import time
import re
import win32com.client 
import io
import glob
import os
from playsound import playsound


#Installation win32com: python -m pip install pywin32
#v1.0 doabigcheese


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


words = ['AutoScan']
speaker = win32com.client.Dispatch("SAPI.SpVoice")
#{ "timestamp":"2021-01-04T11:23:17Z", "event":"Scan", "ScanType":"AutoScan", "BodyName":"HR 8037", "BodyID":0, "StarSystem":"HR 8037", "SystemAddress":1659728021875, "DistanceFromArrivalLS":0.000000, "StarType":"F", "Subclass":1, "StellarMass":1.519531, "Radius":902655680.000000, "AbsoluteMagnitude":3.402924, "Age_MY":1520, "SurfaceTemperature":7464.000000, "Luminosity":"V", "RotationPeriod":128717.123639, "AxialTilt":0.000000, "WasDiscovered":true, "WasMapped":false }

for hit_word, hit_sentence in watch(fn, words):
    try:
        start1 = 'WasDiscovered":'
        end1 = ','
        start2 = 'WasMapped":'
        end2 = ' }'
        #"WasDiscovered":true, "WasMapped":false }
        result1 = re.search('%s(.*)%s' % (start1, end1), hit_sentence).group(1).split(' ')[0]
        result2 = re.search('%s(.*)%s' % (start2, end2), hit_sentence).group(1).split(' ')[0]
        print(result1)
        print(result2)
        if (result1 == 'false'):
            speaker.Speak("System unentdeckt")
        if (result2 == 'false'):
            speaker.Speak("System nicht gemapped")           
    except:
        print(".")
        #playsound(os.getcwd() + '\\zonk.mp3')
