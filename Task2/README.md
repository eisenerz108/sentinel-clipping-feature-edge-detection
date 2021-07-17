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
* Data - TIF File - Converted to JPG of the Task 1 Output.
* Magick - To Convert the images into GIF

### Steps Executed

#### Common Task 
1. I created a util class to read the file (Colour and Grey format) and to write the image on the disk. (Util class will be used in all 3 SubTasks)

CNN Module, but due to lack of time I couldn't look much into it. 
https://www.researchgate.net/publication/344298612_Object_Detection_and_Image_Segmentation_with_Deep_Learning_on_Earth_Observation_Data_A_Review-Part_II_Applications

#### SubTask 1

1. I used two algorithms for the Feature Detection. *SIFT* and *ORB*. 


### SubTask 2 
https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html




  https://www.youtube.com/watch?v=USl5BHFq2H4&t=315s  https://www.researchgate.net/publication/344298612_Object_Detection_and_Image_Segmentation_with_Deep_Learning_on_Earth_Observation_Data_A_Review-Part_II_Applications https://www.semanticscholar.org/paper/Satellite-Image-Segmentation-for-Building-Detection-Chhor-Aramburu/abb13964a435e1ac0c77b7dd68095e9da81b90aa extension://bfdogplmndidlpjfhoijckpakkdjkkil/pdf/viewer.html?file=http%3A%2F%2Fwww.diva-portal.org%2Fsmash%2Fget%2Fdiva2%3A1321511%2FFULLTEXT02.pdf -> FEATURE DETECTION FOR GEOSPATIAL REFERENCINGNiklas Nilsson

https://github.com/developmentseed/label-maker/tree/master/examples
https://medium.com/nattadet-c/image-filters-41c23f09c600



magick convert -delay 80 -loop 0 Task2_2_ED_GreyOriginalImage.jpg Task2_2_ED_Canny.jpg Task2_2_ED_SobelCombined.jpg Task2_2_ED_SobelX.jpg Task2_2_ED_SobelY.jpg Task2_2_ED_Laplacian.jpg Task2_2_ED_CombinedGIF.gif


To Blur the noise, high frequency commponenet, we use thelow pass filetering. uSED TO EXTRACT LARGE OBJECTS IN THE IMAGE. 

https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html
https://www.researchgate.net/publication/339457592_Image_Enhancement_on_OpenCV_based_on_the_Tools_Python_27 - Research Paper
https://medium.com/nattadet-c/image-filters-41c23f09c600


Archive Links 

https://github.com/sentinel-hub/eo-learn 
https://github.com/developmentseed/label-maker/tree/master/examples
https://medium.com/sentinel-hub/introducing-eo-learn-ab37f2869f5c 
https://github.com/robmarkcole/satellite-image-deep-learning 
https://towardsdatascience.com/the-best-earth-observation-data-science-toolkits-a51d867343a0
https://www.youtube.com/watch?v=Rv-yK7Vbk4o





File Name Legend : 
* FD  - Feature Detection
* ED  - Edge Detection
* LPF - Low Pass Filter

Util Class 
