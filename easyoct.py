# written by basta scoza
# necessary imports

import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

# directory path
path_dir = './'
if not os.path.exists(path_dir):
    os.makedirs(path_dir)

#file name
file_name = "result.txt"

IMAGE_PATH = "images/hamza.jpg"
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)
print(result)

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])

text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX
print (text)
with open(os.path.join(path_dir, file_name), 'w+') as temp_file:
    temp_file.write(""+text)

img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
img = cv2.putText(img, text, top_left, font, .5, (255, 255, 255), 2, cv2.LINE_AA)
plt.imshow(img)
plt.show()
