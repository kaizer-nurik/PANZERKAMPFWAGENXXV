import serial 

ser = serial.Serial('/COM3')
while(True):
	ser.write(b's')
	a=1
	b=int(input())
	ser.write(a.to_bytes(1, byteorder='big'))
	ser.write(b.to_bytes(2, byteorder='big'))
	answer = ser.read().decode('utf-8') 
