#右下に画像を合成させる

import cv2

def connect_qr(qr, id):
    src_img = 'static/img/' + id + '.jpg'
    stamp_img = cv2.imread(src_img)
    qr_img = cv2.imread(qr)


    img1 =cv2.resize(stamp_img,(300,200))
    img2 =cv2.resize(qr_img,(50,50))

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    large_img = stamp_img
    small_img = img2
    vertical = stamp_img.shape[0]
    horizontal= stamp_img.shape[1]

    x_offset=250
    y_offset=150

    large_img = img1
    small_img = img2

    x_offset=250
    y_offset=150

    large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img
    #res_name = 'static/res/' + 'res' + id + '.jpg'
    res_name = 'static/res/res.jpg'
    large_img = cv2.cvtColor(large_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(res_name,large_img)

    return
