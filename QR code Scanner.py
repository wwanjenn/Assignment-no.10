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
from pyzbar import pyzbar
import numpy as np
import datetime

# Steps 

# 1 Scan QR code using Webcam.
cam = cv2.VideoCapture(0)
while True:
    _, qrCode = cam.read()
    qrData = pyzbar.decode(qrCode)
    cv2.imshow('QR Code Scanner', qrCode)
    key = cv2.waitKey(1)
    if key == ord('e'):
        break
cam.release()
cv2.destroyAllWindows()

# 2 Decode QR code.
data = pyzbar.decode(qrData)

# 3 Check for Date and Time.

# 4 Write data into a text file.