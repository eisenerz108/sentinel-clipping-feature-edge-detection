"""
Created Date : 16-Jul-21
@author : Aman Jain
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

import util

img = util.readFile_gray()
#img = cv2.GaussianBlur(img, (11,11), 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

canny = cv2.Canny(img, 100, 150)

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['2_ED_GreyOriginalImage','2_ED_Laplacian','2_ED_Canny','2_ED_SobelX','2_ED_SobelY','2_ED_SobelCombined']
images = [img, laplacian, canny, sobelX, sobelY, sobelCombined]

for title,image in zip(titles,images):
    util.writeImage(image, title)

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()