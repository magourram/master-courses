import serial, time
SERIAL_PORT = "/dev/ttyACM0"
ser = serial.Serial(SERIAL_PORT, 115200)
while True:
# for i in range(20):
    ser.write((0xFF,))
    time.sleep(1)
    ser.write((0x0,))
    time.sleep(0.5)
ser.close()
