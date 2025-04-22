import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction= qrcode.ERROR_CORRECT_L,
    box_size=30,
    border=2,
)

qr.add_data('Gerador de QRCODE')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')