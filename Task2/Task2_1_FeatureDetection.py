import cv2

import util
from matplotlib import pyplot as plt

## SIFT Algorithm

# Fetching the Coloured Image using the Util Class
image_sift = util.readFile_coloured()

# Fetching the Grayscale Image using the Util Class
gray = util.readFile_gray()

# Creating an Object of the SIFT Detection Algorithm
sift = cv2.SIFT_create(nfeatures=5000)
keyPoints, descriptors = sift.detectAndCompute(image_sift, None)
output_featuredet_sift = cv2.drawKeypoints(gray, keyPoints, image_sift,
                                           flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

## ORB Algorithm

# Fetching the Coloured Image using the Util Class
image_orb = util.readFile_coloured()

# Fetching the Grayscale Image using the Util Class
gray = util.readFile_gray()

# Creating an Object of the ORB Detection Algorithm
orb = cv2.ORB_create(nfeatures=100)
keyPoints, descriptors = orb.detectAndCompute(image_orb, None)
output_featuredet_orb = cv2.drawKeypoints(gray, keyPoints, image_orb, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


## Plotting and Writing the Image

titles = ['1_FD_GreyOriginalImage', '1_FD_SIFT', '1_FD_ORB']
images = [gray, output_featuredet_orb, output_featuredet_sift]

for title, image in zip(titles, images):
    util.writeImage(image, title)

for i in range(len(titles)):
    plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
