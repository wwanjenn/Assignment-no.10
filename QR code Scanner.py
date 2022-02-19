# Assignment 10

# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger.


import cv2
from pyzbar.pyzbar import decode
import numpy as np
from datetime import datetime

# Steps 

# 1 Scan QR code using Webcam.
cam = cv2.VideoCapture(0)
while True:
    _, qrCode = cam.read()

# 2 Decode QR code.
    for qrData in decode(qrCode):
        data = qrData.data.decode('utf-8')
        points = np.array([qrData.polygon], np.int32)
        points = points.reshape((1,-1,2))
        cv2.polylines(qrCode,points,True,(0,0,255),5,-1)
    cv2.imshow('QR Code Scanner', qrCode)
    key = cv2.waitKey(1)
    if key == ord('e'):
        break
    
# 3 Check for Date and Time.
dateNtime = datetime.now()
time = dateNtime.strftime("%I:%M %p")
date = dateNtime.strftime("%B %d, %Y")

# 4 Write data into a text file.
with open('Scanner Result.txt', 'w+') as txt:
    txt.write(data +  f'\n\nDate: {date}     Time: {time}')
