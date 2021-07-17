import cv2


def readFile_coloured():
    # Taking the Input of the Image File, and returns Image in the form of numpy.ndarray - Coloured
    image_file = r'data\Task2_Image.jpg'
    return cv2.imread(image_file, cv2.IMREAD_COLOR)


def readFile_gray():
    # Taking the Input of the Image File, and returns Image in the form of numpy.ndarray - Gray
    image_file = r'data\Task2_Image.jpg'
    return cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)


def writeImage(image, filename):
    # Writing the output to an image file.
    file_name = r'images\Task2_{}.jpg'.format(filename)
    cv2.imwrite(file_name, image)
