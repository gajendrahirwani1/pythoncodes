from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ =='__main__':
    # music_on_loop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 10
    eyesec = 20
    exsec = 30

    while True:
        if time() - init_water > watersec:
            print("water drinking time, enter 'drank' to stop the alarm")
            musiconloop('water.mp3','drank')
            init_water = time()
            log_now("drank water at ")

        if time() - init_eyes > eyesec:
            print("eyes exercise  time, enter 'done' to stop the alarm")
            musiconloop('eyes.mp3','done')
            init_eyes = time()
            log_now("eyes exercise done at ")

        if time() - init_exercise > exsec:
            print("physical exercise time, enter 'donephy' to stop the alarm")
            musiconloop('physical.mp3','donephy')
            init_exercise = time()
            log_now("physical exercise done at ")


