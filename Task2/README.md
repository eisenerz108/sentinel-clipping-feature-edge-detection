# Aman_GIS_LiveEO_Task_2

## Contents :
1. [Tools Used And Data](#tools-used-and-data)
2. [Steps Executed](#steps-executed)
3. [References](#references)



### Tools Used And Data
* PyCharm IDE - As this task has less of interim image displays, I worked on PyCharm as I am more comfortable in that. 
* GitHub - Version Control
* Data - I downloaded the Data from Google Maps as the Task1 Data was not very clear. 
* Magick - To Convert the images into GIF

### Steps Executed


https://github.com/sentinel-hub/eo-learn https://github.com/developmentseed/label-maker/tree/master/examples

https://medium.com/sentinel-hub/introducing-eo-learn-ab37f2869f5c https://github.com/robmarkcole/satellite-image-deep-learning https://towardsdatascience.com/the-best-earth-observation-data-science-toolkits-a51d867343a0 https://www.youtube.com/watch?v=Rv-yK7Vbk4o https://www.youtube.com/watch?v=USl5BHFq2H4&t=315s https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html https://pypi.org/project/opencv-python/ https://www.youtube.com/watch?v=DZtUt4bKtmY https://www.researchgate.net/publication/344298612_Object_Detection_and_Image_Segmentation_with_Deep_Learning_on_Earth_Observation_Data_A_Review-Part_II_Applications https://www.semanticscholar.org/paper/Satellite-Image-Segmentation-for-Building-Detection-Chhor-Aramburu/abb13964a435e1ac0c77b7dd68095e9da81b90aa extension://bfdogplmndidlpjfhoijckpakkdjkkil/pdf/viewer.html?file=http%3A%2F%2Fwww.diva-portal.org%2Fsmash%2Fget%2Fdiva2%3A1321511%2FFULLTEXT02.pdf -> FEATURE DETECTION FOR GEOSPATIAL REFERENCINGNiklas Nilsson

https://github.com/developmentseed/label-maker/tree/master/examples



magick convert -delay 80 -loop 0 Task2_2_ED_GreyOriginalImage.jpg Task2_2_ED_Canny.jpg Task2_2_ED_SobelCombined.jpg Task2_2_ED_SobelX.jpg Task2_2_ED_SobelY.jpg Task2_2_ED_Laplacian.jpg Task2_2_ED_CombinedGIF.gif


To Blur the noise, high frequency commponenet, we use thelow pass filetering. uSED TO EXTRACT LARGE OBJECTS IN THE IMAGE. 
