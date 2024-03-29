import cv2
import matplotlib.pyplot as plt
import numpy as np

import util

img = util.readFile_gray()

# Blurring an image before Edge Detection is optional, but since it has a different task I have done that in Task2_3

# Laplacian Method
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

# Canny Method
canny = cv2.Canny(img, 100, 150)

# Sobel Method
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

## Plotting and Writing the Image

titles = ['2_ED_GreyOriginalImage','2_ED_Laplacian','2_ED_Canny','2_ED_SobelX','2_ED_SobelY','2_ED_SobelCombined']
images = [img, laplacian, canny, sobelX, sobelY, sobelCombined]

for title,image in zip(titles,images):
    util.writeImage(image, title)

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()