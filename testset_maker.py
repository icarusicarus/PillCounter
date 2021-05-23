import os
import keyboard
# import time
from time import sleep
from picamera import PiCamera
# import RPi.GPIO as GPIO

camera = PiCamera()

# def setup_mortor():

def p1():
    cut_num = 50
    dir_name = "./P1"
    if os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)

    pill = input("Enter the number of pills: ")
    zpill = str(pill).zfill(3) + "_"
    count = 0
    while count < cut_num:
        print("Press 's' to take a picture.\nIf you want to terminate, press 'q')")
        if keyboard.read_key() == 'q':
            break
        elif keyboard.read_key() == 's':
            file_name = "P1_" + zpill + str(count+1).zfill(2) + ".jpg"
            camera.capture(dir_name + "/" + file_name)
            print("[O] " + file_name)
            count += 1
        else:
            print("Wrong key :(")
    

def s1():
    # setup_mortor()
    cut_num = 10
    dir_name = "./S1"
    if os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)

    pill = input("Enter the number of pills: ")
    zpill = str(pill).zfill(3) + "_"
    count = 0

if __name__ == "__main__":
    p1()
    # s1()
