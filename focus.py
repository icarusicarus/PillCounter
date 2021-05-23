from picamera import PiCamera
import keyboard

camera = PiCamera()

camera.start_preview()
if keyboard.read_key() == 'q':
    camera.stop_preview()