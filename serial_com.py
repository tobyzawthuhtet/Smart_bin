import serial
from time import sleep

ser = serial.Serial(port='/dev/ttyACM0',baudrate = 9600)
bytes = 1
while True:
    ser.write(str(bytes).encode())
    sleep (1)
    read_serial= ser.readline()
    print (read_serial)
