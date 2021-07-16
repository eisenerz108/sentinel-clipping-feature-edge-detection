"""
Created Date : 16-Jul-21
@author : Aman Jain
"""
import cv2


# Taking the Input of the Image File, and returns Image in the form of numpy.ndarray - Coloured
def readFile_coloured():
    image_file = r'data\Task2_Image.jpg'
    return cv2.imread(image_file, cv2.IMREAD_COLOR)


# Taking the Input of the Image File, and returns Image in the form of numpy.ndarray - Gray
def readFile_gray():
    image_file = r'data\Task2_Image.jpg'
    return cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)


# Writing the output to an image file.
def writeImage(image, filename):
    file_name = r'images\Task2_{}.jpg'.format(filename)
    cv2.imwrite(file_name, image)
