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

""" Reads the QR Code through web camera then displays the data stored in it in a new text file. """

# import all libraries to be used
# the cv2 library for live webcams; the pyzbar library for decoding QR codes; and the datetime library for time and date stamping
import cv2; from pyzbar import pyzbar; from datetime import *

# define a function that stores all the codes needed to read the QR code
def readQR ():
    capture = cv2.VideoCapture(0)
    while True: # this loop is to prevent the web camera from closing unless it is intended to
        _, image = capture.read()
        image = decodeQR(cv2.resize(image, None, fx = 1.0, fy = 1.0, interpolation = cv2.INTER_AREA)) # the image that will be scanned on the web cam will be resized according to the parameters i set, and will also be decoded
        cv2.imshow("QR Code Scanner", image) # the live camera will run on the screen
        if cv2.waitKey(1) == ord('q'):
            break # the live camera will close if you press 'q'
    capture.release()
    cv2.destroyAllWindows() # this code will fully shut down the web camera

# define another function that contains all the codes needed to decode the QR code and to record the time and date stamp
def decodeQR (image):
    qrCode = pyzbar.decode(image) # the scanned QR code will be decoded here
    timeDate = datetime.now()
    date = timeDate.strftime("%B %d, %Y") # stores the exact date in this format: Month Day, Year 
    hour = timeDate.strftime("%I:%M %p") # stores the exact hour in this format: Hour(1-12): Minute AM/PM
    for details in qrCode:
        qrData = details.data.decode('utf-8')
        with open ("QR-Code-Result.txt", "w") as textfile: 
            textfile.write(qrData + (f"\n\nDate registered: {date}\nTime registered: {hour}")) # the decoded data will now be opened and written in a new text file together with the time and date stamp
    return image

# call the function to execute the reading of the QR code
readQR()