# Aman_GIS_LiveEO_Task


Steps : 
1. I used Jupyter Notebook as I already had a gis virtual env setup in conda. 
2. I downloaded the Area Of Interest from the Google Drive, link [here](https://drive.google.com/file/d/1cYulst52qOsx1VOOtVQo5sRdUugYqEpl/view) :
3. Using Kepler GL, I found the AreaofInterest is North Eastern Part of Berlin, Germany (click [here](https://user-images.githubusercontent.com/75158219/125793336-f5376d2b-d7e4-422f-84db-51c812989205.png)), and with this I got to know, the satellite image needs to be downloaded for the part which has Berlin, Germany. 
4. First I thought of downloading the Satellite data from [USGS.gov website](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-sentinel-2?qt-science_center_objects=0#qt-science_center_objects), but the partnership between ESA and the USGS allows only for the distribution of Level-1C. As per the Task we need Level 2-A Data. 
5. Finally, I downloaded the data from https://scihub.copernicus.eu/dhus/#/home with the following properties :
   * Selected the Berlin Location
   * In the advanced search I selected Mission - Sentinel 2
   * Product Type as S2MSI2A
   * Year 2020 
   * (Through this I was able to download the correct data with the requirement - `Sentinel-2 level 2A tile from any practical TOI (2019 or 2020)`



