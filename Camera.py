from picamera import PiCamera
import datetime,os

os.makedirs('/home/pi/images',exist_ok=True)
camera=PiCamera()
camera.resolution=(1024,768)
camera.capture("{}/image_{}.jpg".format('/home/pi/images',datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
