import serial # Serial
from time import sleep #time
from datetime import datetime
from picamera import PiCamera # camera
import sys 
import Adafruit_DHT #DHT 11
import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
camera = PiCamera()
camera.rotation = (180)
bytes = 1
inpin = 17
outpin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
ser = serial.Serial(port='/dev/ttyACM0',baudrate = 9600)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
GPIO.setup(inpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(outpin,GPIO.OUT)
GPIO.output(outpin, True)

bin_open = False

def capture_image():
    #camera.start_preview()
    for i in range (3):
        sleep (1)
        camera.capture ('/home/pi/Desktop/image_folder/bin_image%s.jpg' % i)
    camera.close()
    #camera.stop_preview()

def DHT11():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
    
def fill():
    
    #time.sleep (2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output (TRIG, False)

    while GPIO.input (ECHO) == 0:
            pulse_start = time.time()
    
    while GPIO.input (ECHO) == 1:
            pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round (distance ,2)
    print ("Distance:", distance , "cm")
    
def serial_com():
    ser.write(str(bytes).encode())
    sleep (1)
    read_serial= ser.readline()
    print (read_serial)

def check_bin_open():
    if GPIO.input (inpin) == 1:
        print("Bin Closes")
        return False
    else :
        print("Bin Opens")
        return True

while True:
    print(datetime.now())
    DHT11()
    fill()
    sleep(1)
    serial_com()
    current_bin_state = check_bin_open()
    if bin_open and current_bin_state==False:
        print("Capturing")
        capture_image()
    bin_open = current_bin_state
