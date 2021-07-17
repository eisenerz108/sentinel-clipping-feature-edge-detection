# Aman_GIS_LiveEO_Task_2

## Contents :
1. [Tools Used And Data](#tools-used-and-data)
2. [Steps Executed](#steps-executed)
   * [Common Task](#common-task)
   * [Sub - Task 1](#subtask-1)
   * [Sub - Task 2](#subtask-2)
   * [Sub - Task 3](#subtask-3)
5. [References](#references)



### Tools Used And Data
* PyCharm IDE - As this task has less of interim image displays, I worked on PyCharm as I am more comfortable in that. 
* GitHub - Version Control
* Data - TIF File - Converted to JPG of the Task 1 Output. `data\Task2_Image.jpg`
* Magick - To Convert the images into GIF

### Steps Executed

#### Common Task 
1. I created a util class to read the file (Colour and Grey format) and to write the image on the disk. (Util class will be used in all 3 SubTasks)


#### SubTask 1

1. I used two algorithms for the Feature Detection. *SIFT* and *ORB*. 
2. Feature Detection using Convolutional neural network would really be beneficial [[1]](#1), but due to lack of time I have used the Computer Vision module CV2. 
3. I read about SIRF [[2]](#2) and all the Feature Detection of CV module [[3]](#3)
4. I used the SIFT and ORB Feature Detection Algorithms on the Image, and saved the output. `images\Task2_1_FB_GreyOriginialImage.jpg`, `images\Task2_1_FB_SIFT.jpg` and `images\Task2_1_FB_ORB.jpg`. I had overridden the nfeatures for both the algorithms and set the flag as `DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS`, which will draw a circle with size of keypoint and even show its orientation. A combined image of all three is also stored in `images\Task2_1_FB_CombinedImage.jpeg`. 
5. In future we can also use a label marker. [[4]](#4)

![image](https://user-images.githubusercontent.com/75158219/126021598-1c5bc4b5-ba32-415c-b91e-bf0ba49f45c3.png)




### SubTask 2 
https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html


### SubTask 3 
https://medium.com/nattadet-c/image-filters-41c23f09c600 
https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html

**Description** - To Blur the noise, high frequency commponenet, we use thelow pass filetering. uSED TO EXTRACT LARGE OBJECTS IN THE IMAGE. 




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

Archive Links 

https://github.com/sentinel-hub/eo-learn 
https://github.com/developmentseed/label-maker/tree/master/examples
https://medium.com/sentinel-hub/introducing-eo-learn-ab37f2869f5c 
https://github.com/robmarkcole/satellite-image-deep-learning 
https://towardsdatascience.com/the-best-earth-observation-data-science-toolkits-a51d867343a0
https://www.youtube.com/watch?v=Rv-yK7Vbk4o
 https://www.researchgate.net/publication/344298612_Object_Detection_and_Image_Segmentation_with_Deep_Learning_on_Earth_Observation_Data_A_Review-Part_II_Applications 





File Name Legend : 
* FD  - Feature Detection
* ED  - Edge Detection
* LPF - Low Pass Filter

Util Class 
