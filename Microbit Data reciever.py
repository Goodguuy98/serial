import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'com9'

ser.open()
while True:
    data = str(ser.readline())
    print(data)