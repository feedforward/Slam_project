import os
from PIL import Image
import cv2
import matplotlib.pyplot as plt

changed_from = './Inpainted/'
names_needed = './rgb/'
to = sorted(os.listdir(names_needed))
frm = os.listdir(changed_from)

org = cv2.imread(names_needed+'1341846647.834093.png')
img_shape = org.shape

for i in range(len(to)-1):

    # os.rename(r'./Inpainted/{}.png'.format(str(i+1).zfill(6)), r'./Inpainted/{}'.format(to[i]))
    # # im1 = Image.open(r'./seq_tum/{}.jpg'.format(str(i).zfill(6)))
    # im1.save(r'./seq_new/{}'.format(to[i]))
    name = './Inpainted/{}.png'.format(str(i+1).zfill(5))
    # print(name)
    img = cv2.imread(name, cv2.IMREAD_COLOR)
    print(img_shape, img.shape)
    resized = cv2.resize(img,(img_shape[1], img_shape[0]), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite('./new/{}'.format(to[i]), resized)
