import cv2
import serial
import numpy as np
ser = serial.Serial('/COM3')
def on_trackbar1(val):
    a=1
    b=int(500+2000*(val/180))
    ser.write(b's')
    ser.write(a.to_bytes(1, byteorder='big'))
    ser.write(b.to_bytes(2, byteorder='big'))
    
def on_trackbar2(val):
    a=2
    b=int(500+2000*(val/180))
    ser.write(b's')
    ser.write(a.to_bytes(1, byteorder='big'))
    ser.write(b.to_bytes(2, byteorder='big'))

def on_trackbar3(val):
    a=3
    b=int(500+2000*(val/180))
    ser.write(b's')
    ser.write(a.to_bytes(1, byteorder='big'))
    ser.write(b.to_bytes(2, byteorder='big'))

def on_trackbar4(val):
    a=4
    b=int(500+2000*(val/180))
    ser.write(b's')
    ser.write(a.to_bytes(1, byteorder='big'))
    ser.write(b.to_bytes(2, byteorder='big'))

def on_trackbar5(val):
    a=5
    b=int(500+2000*(val/180))
    ser.write(b's')
    ser.write(a.to_bytes(1, byteorder='big'))
    ser.write(b.to_bytes(2, byteorder='big'))
cv2.namedWindow('PANZERKAMPFAGEN XX')

cv2.createTrackbar('Servo1 angle' ,'PANZERKAMPFAGEN XX', 0, 180, on_trackbar1)
cv2.createTrackbar('Servo2 angle' ,'PANZERKAMPFAGEN XX', 0, 180, on_trackbar2)
cv2.createTrackbar('Servo3 angle' ,'PANZERKAMPFAGEN XX', 0, 180, on_trackbar3)
cv2.createTrackbar('Servo4 angle' ,'PANZERKAMPFAGEN XX', 0, 180, on_trackbar4)
cv2.createTrackbar('Servo5 angle' ,'PANZERKAMPFAGEN XX', 0, 180, on_trackbar5)


# Show some stuff

dst = np.zeros((500,500,3), np.uint8)
cv2.imshow('PANZERKAMPFAGEN XX',dst)
cv2.waitKey()
ser.close()