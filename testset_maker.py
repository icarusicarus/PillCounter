import os
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
    zpill = pill.zfill(3) + "_"
    count = 0
    while count < cut_num:
        shutter = input("Press any key to take a picture.(If you want to terminate, press q)")
        if shutter == 'q':
            break
        file_name = "P1_" + zpill + str(count+1).zfill(2) + ".jpg"
        camera.capture(dir_name + "/" + file_name)
        print("[O] " + file_name)
        count += 1
    

def s2():
    # setup_mortor()
    camera.capture('bar.jpg')

if __name__ == "__main__":
    p1()
    # s2()