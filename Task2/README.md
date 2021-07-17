# Aman_GIS_LiveEO_Task_2

## Contents :
1. [Tools Used And Data](#tools-used-and-data)
2. [FileNames Legend](#filenames-legend)
3. [Steps Executed](#steps-executed)
   * [Common Task](#common-task)
   * [Sub - Task 1](#subtask-1)
   * [Sub - Task 2](#subtask-2)
   * [Sub - Task 3](#subtask-3)
4. [Uses](#uses)
5. [References](#references)



### Tools Used And Data
* PyCharm IDE - As this task has less of interim image displays, I worked on PyCharm as I am more comfortable in that. 
* GitHub - Version Control
* Data - TIF File - Converted to JPG of the Task 1 Output. `data\Task2_Image.jpg`
* Magick - To Convert the images into GIF

### FileNames Legend 

* FD  - Feature Detection
* ED  - Edge Detection
* LPF - Low Pass Filter
* util - Utility Class

### Steps Executed

#### Common Task 
1. I created a util class to read the file (Colour and Grey format) and to write the image on the disk. (Util class will be used in all 3 SubTasks). Methods created are `readFile_coloured()`, `readFile_gray()` and `writeImage()`. 


#### SubTask 1
(Please open the file `Task2_1_FeatureDetection.py`)

1. I used two algorithms for the Feature Detection. *SIFT* and *ORB*. 

2. Feature Detection using Convolutional neural network would really be beneficial [[1]](#1), but due to lack of time I have used the Computer Vision module CV2. 

3. I read about SIRF [[2]](#2) and about the Feature Detection Algorithms of CV module [[3]](#3)

4. I used the SIFT and ORB Feature Detection Algorithms on the Image, and saved the output. `images\Task2_1_FB_GreyOriginialImage.jpg`, `images\Task2_1_FB_SIFT.jpg` and `images\Task2_1_FB_ORB.jpg`. I had overridden the nfeatures for both the algorithms and set the flag as `DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS`, which will draw a circle with size of keypoint and even show its orientation. A combined image of all three is also stored in `images\Task2_1_FB_CombinedImage.jpeg`, and also displayed below. 

5. In future we can also use a label marker. [[4]](#4)

![image](https://user-images.githubusercontent.com/75158219/126021598-1c5bc4b5-ba32-415c-b91e-bf0ba49f45c3.png)




#### SubTask 2 
(Please open the file `Task2_2_EdgeDetection.py`)

1. For Edge Detection, I used Canny [[5]](#5), Laplacian and Sobel Algorithms [[6]](#6)

2. I have stored all the images `images\Task2_2_ED_GreyOriginalImage.jpg`, `images\Task2_2_ED_Canny.jpg`, `images\Task2_2_ED_Laplacian.jpg`, `images\Task2_2_ED_SobelX.jpg`, `images\Task2_2_ED_SobelY.jpg`, `images\Task2_2_ED_SobelCombined.jpg`. A combined image can be seen below or in `images\Task2_2_ED_CombinedImage.jpeg`. In addition to these I have also create a gif to see all the Edge Pattern in one transition `images\Task2_2_ED_CombinedGIF`. 

**Note** : 2_ED_Laplacian is not being displayed correctly in the combined file, please open the individual file `image\Task2_2_ED_Laplacian.jpg` to see the correct Edge Pattern

![image](https://user-images.githubusercontent.com/75158219/126022062-3118ac3c-73d4-4b4d-b4ff-54ecc9e37c18.png)




#### SubTask 3 
(Please open the file `Task2_3_LowPassFilter.py`)
1. I first read about the filter from the medium article [[7]](#7), freeCodeCamp.org Youtube channel [[8]](#8) and the OpenCV API Documentation [[9]](#9)

2. I used, filter2D, blur and GaussianBlur Image blurring techniques, and for filter2D I created two Kernels -> (5,5) and (3,3)

3. The outputs of each Image blurring techniques are stored in the `images\Task2_3_LPF_Blur`, `images\Task2_3_LPF_Gassian_Blur`, `images\Task2_3_LPF_Convolved3`, `images\Task2_3_LPF_Convolved5`, and the combined image in the `images\Task2_3_LPF_AllFiltersCombined`, and can be seen below. 

![image](https://user-images.githubusercontent.com/75158219/126036302-88fbcf59-204d-4732-8baa-0a01e44f8487.png)




 

### Uses
1. **Feature Detection** - In the world of Geospatial, when we are dealing with a lot of Earth Observation Data, with feature detection we can detect Vehicles, Buildings, Vegetations, and a lot of strcutures which can be widely used in Military, Civil Engineering, Urban planning and more
2. **Edge Detection** -  I believe, Edge Detection can be used to detect the size of the structures like a huge Vegetation Land, a Lake, a huge mall and more. 
3. **Low Profile Filter** - To Blur the noise, high frequency commponenet, we use thelow pass filetering. uSED TO EXTRACT LARGE OBJECTS IN THE IMAGE. 


### References 
* <a id="1">[1]</a> TY  - JOUR
AU  - Hoeser, Thorsten
AU  - Bachofer, Felix
AU  - Kuenzer, Claudia
PY  - 2020/09/18
SP  - 3053
T1  - Object Detection and Image Segmentation with Deep Learning on Earth Observation Data: A Review-Part II: Applications
VL  - 12
DO  - 10.3390/rs12183053
JO  - Remote Sensing
ER  - 
https://www.researchgate.net/publication/344298612_Object_Detection_and_Image_Segmentation_with_Deep_Learning_on_Earth_Observation_Data_A_Review-Part_II_Applications

* <a id="2">[2]</a>
Author:Niklas NilssonSupervisors:Villiam Aspegren, Carmenta Geospatial TechnologiesHaidar Al-Naseri, Dep. of Physics, Umeå UniversityExaminer: Eddie Wadbro, Dep. of Computer Science, Umeå Univeristy - 
[extension://bfdogplmndidlpjfhoijckpakkdjkkil/pdf/viewer.html?file=http%3A%2F%2Fwww.diva-portal.org%2Fsmash%2Fget%2Fdiva2%3A1321511%2FFULLTEXT02.pdf](extension://bfdogplmndidlpjfhoijckpakkdjkkil/pdf/viewer.html?file=http%3A%2F%2Fwww.diva-portal.org%2Fsmash%2Fget%2Fdiva2%3A1321511%2FFULLTEXT02.pdf)

* <a id="3">[3]</a>
https://docs.opencv.org/3.4/db/d27/tutorial_py_table_of_contents_feature2d.html


* <a id="4">[4]</a>
 https://github.com/developmentseed/label-maker/tree/master/examples

* <a id="5">[5]</a>
https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

* <a id="6">[6]</a> https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php

* <a id="7">[7]</a> https://medium.com/nattadet-c/image-filters-41c23f09c600

* <a id="8">[8]</a> https://www.youtube.com/watch?v=oXlwWbU8l2o

* <a id="9">[9]</a> https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html




