"""
Created Date : 16-Jul-21
@author : Aman Jain
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

import util

img = util.readFile_gray()
img = cv2.GaussianBlur(img, (11,11), 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

canny = cv2.Canny(img, 100, 150)

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

util.writeImage(img,'2_ED_GreyOriginalImage')
util.writeImage(laplacian,'2_ED_Laplacian')
util.writeImage(canny,'2_ED_Canny')
util.writeImage(sobelX,'2_ED_SobelX')
util.writeImage(sobelY,'2_ED_SobelY')
util.writeImage(sobelCombined,'2_ED_SobelCombined')

titles = ['Original Greyed Image','Laplacian','Canny','Sobel X','Sobel Y','Sobel Combined']
images = [img, laplacian, canny, sobelX, sobelY, sobelCombined]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()