# Aman_GIS_LiveEO_Task

## Tools Used and Data 

* Jupter Notebook - GIS Virtual Env was already ready with me. 
* QGIS
* GitHub
* Data downloaded from [[1]](#1)

## References
<a id="1">[1]</a> 
https://drive.google.com/file/d/1cYulst52qOsx1VOOtVQo5sRdUugYqEpl/view



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
6. I selected the 12 (Total 13, but removed 10 - cirrus band that gives no ground information) specific bands which are needed which I refered from [here](https://en.wikipedia.org/wiki/Sentinel-2)
7. I selected the SCL Layer (20m), and opened it in SQIS to make the are `NO_DATA`,`SATURATED_OR_DEFECTIVE`, `CLOUD_HIGH_PROBABILITY` as NOVALUE. The label for each classification I found from here (https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-2a/algorithm)
8. I opened those 13 Bands (12 + 1 SCL) in the QGIS as created a Virtual Layer using all the raster files. I read the description about the Blue, Green and Red bands from https://www.satimagingcorp.com/satellite-sensors/other-satellite-sensors/sentinel-2a/
9. I created a virtual Layer of the BGR Bands (2,3,4), but there was a color mismatch, so I edited the virtual layer and set the BGR (Specific to each band), and I was able to see an observable satellite map of Berlin (And surroundings). 
10. I could see the Satellite images have an EPSG of 32633, hence I created a new aoi with EPSG 32633 with the name as remote_sensing_challenge_AOI32633.geojson
11. Just to validate the Correct data has been downloaded, I verified by adding the AOI on top of the layer, and here is the output. ![image](https://user-images.githubusercontent.com/75158219/125833711-6d6af508-8483-416e-ad5d-85e8f72b7954.png)
12. For Sentinel Data information, click [here](https://user-images.githubusercontent.com/75158219/125817870-a203715b-a81d-4f8b-936e-ca3fc8ca1f9b.png)
Reference taken from https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l2a/
SCL - Scene Classification Data
11. Converting the SCL Layers to NoValue. https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-2a/algorithm
12. 





