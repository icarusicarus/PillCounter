import os
import keyboard
import time
from time import sleep
from picamera import PiCamera
# import RPi.GPIO as GPIO

# camera = PiCamera()

# def setup_mortor():

def p3():
    cut_num = 50
    dir_name = "./P3"
    if os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)

    pill = input("Enter the number of pills: ")
    zpill = str(pill).zfill(3) + "_"
    camera.resolution = (1024, 768)
    count = 0
    while count < cut_num:
        camera.start_preview()
        print("Press 's' to take a picture.\nIf you want to terminate, press 'q')")
        if keyboard.read_key() == 'q':
            camera.stop_preview()
            break
        elif keyboard.read_key() == 's':
            file_name = "P3_" + zpill + str(count+1).zfill(2) + ".jpg"
            camera.capture(dir_name + "/" + file_name)
            print("[O] " + file_name)
            camera.stop_preview()
            count += 1
        else:
            print("Wrong key :(")
    

def s3():
    camera = PiCamera()

    cycle_num = 5
    cut_num = 10
    dir_name = "./S3"
    if os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)

    pill = input("Enter the number of pills: ")
    zpill = str(pill).zfill(3) + "_"
    camera.resolution = (1024, 768)
    count = 0
    print("..")


    for i in range(0, 5):
        while count < cut_num:
            camera.start_preview()
            if keyboard.read_key() == 'q':
                camera.stop_preview()
                break
            elif keyboard.read_key() == 's':
                file_name = "S3_" + zpill + str(i+1).zfill(2) + "_" +  str(count+1).zfill(2) + ".jpg"
                camera.capture(dir_name + "/" + file_name)
                print("[O] " + file_name)
                camera.stop_preview()
                count += 1
            else:
                print("Wrong key :<")
        print("Please rearrange pills")
        count = 0


if __name__ == "__main__":
    #p3()
    s3()
