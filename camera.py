from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = (180)


def camera_sensor():
    camera.start_preview()
    for i in range (3):
        sleep (1.5)
        camera.capture ('/home/pi/Desktop/image_folder/images_taken%s.jpg' % i)
    camera.stop_preview()
    

camera_sensor()
