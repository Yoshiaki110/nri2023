import qrcode
from PIL import Image

def make_qrcode(id):
    url = 'http://localhost:5000/spot/' + id
    img_name = 'static/img/'+'qr_' + id + '.jpg'

    img = qrcode.make(url)
    img.save(img_name)
    img = Image.open(img_name)

    img.save(img_name)

    return img_name
