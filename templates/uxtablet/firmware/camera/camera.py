import picamera
import time

def take_picture(title):
    camera = picamera.PiCamera()
    camera.capture(title+'.png')


