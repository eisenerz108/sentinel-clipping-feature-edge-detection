import cv2
from matplotlib import pyplot as plt
import numpy as np
import util

img = util.readFile_coloured()
kernel_5 = np.ones((5,5), np.float32)/25
kernel_3 = np.ones((3,3), np.float32)/9

con_image_5 = cv2.filter2D(img, -1, kernel_5)
con_image_3 = cv2.filter2D(img, -1, kernel_3)
blurImg = cv2.blur(img, (5,5))
gaussian_blur = cv2.GaussianBlur(img, (5,5), 0)

titles = ['3_LPF_OriginalImage','3_LPF_Convolved_3','3_LPF_Convolved_5','3_LPF_Blur','3_LPF_Gaussian_Blur']
images = [img, con_image_3, con_image_5, blurImg, gaussian_blur]

for title,image in zip(titles,images):
    util.writeImage(image, title)

for i in range(len(titles)):
    plt.subplot(1, 5, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
