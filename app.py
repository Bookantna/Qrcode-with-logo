import qrcode 
from PIL import Image

logo_path = 'logo.png'

logo = Image.open(logo_path)
logo = logo.resize((100, 100))

qrimg = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

url = 'https://github.com/Bookantna/AMP'
qrimg.add_data(url)
qrimg.make()

Qrimg = qrimg.make_image(fill_color='#f16322', back_color="#414141").convert('RGB')
pos = ((Qrimg.size[0] - logo.size[0]) // 2,
       (Qrimg.size[1] - logo.size[1]) // 2)
print(pos)
print(Qrimg.size[0],Qrimg.size[1])
Qrimg.paste(logo,pos)
Qrimg.save('Logo_qr.png')