from picamera import PiCamera
import time

camera = PiCamera()

camera.resolution = (1024, 768)
camera.start_preview()
time.sleep(2)
camera.stop_preview()
camera.capture('./P1/P1_016_18.jpg')
