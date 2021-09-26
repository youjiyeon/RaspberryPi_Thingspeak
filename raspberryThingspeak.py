import datetime 
import urllib2

import serial
from time import sleep

ser = serial.Serial("/dev/ttyANAB", 9600)

while True:
        received_data = ser.read()
        sleep(0.03)
        data_left += ser.inWaiting()
        received data += ser.read(data_left) 
        ser.write(received_data)
       
        hum = received_data[0:5]
        temp = received_data[5:9]
 
        wtime = datetime.datetime.now()

        print(wtime, 'Humidity = {}% Temperature = {}°C'.format(hum, temp)) 
        response = url11ib2.urlopen("https://api.thingspeak.com/update?api_key=*****="+(hum)+"field"+(temp)) 
        time.sleep(10)
