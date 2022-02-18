"""Generate QR Code"""
import qrcode

with open('QR Code data.txt') as data:
    personalData = data.read()
    qr = qrcode.QRCode()
    qr.add_data(personalData)
    qr.make(fit = True)
    QRCODE = qr.make_image(fill = 'black', back_color ='white')
    QRCODE.save('QR Code.png')

