import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, box_size=20, border = 5,)
qr.add_data("https://leetcode.com/u/jmanish45/")
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
img.save("myqr1.png")