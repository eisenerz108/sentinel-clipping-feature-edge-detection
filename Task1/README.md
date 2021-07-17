# Aman_GIS_LiveEO_Task_1

## Contents :
1. [Tools Used And Data](#tools-used-and-data)
2. [Steps Executed](#steps-executed-data-preprocessing)
3. [Uses](#uses)
4. [References](#references)


### Tools Used and Data 

* **Jupyter Notebook** - I mostly work on PyCharm but packages like Shapely and KeplerGL works better on Jupyter Notebook. The GIS Virtual Env was already ready with me. 
* **QGIS** - For viewing the Data
* **GitHub** - Version Control
* **Data** - Area of Interest Data was downloaded from the Google Driver [[1]](#1) in GeoJSON format 


### Steps Executed Data Preprocessing

1. I processed the GeoJSON data in Jupyter Notebook. 

2. Using Kepler GL, I found the AreaofInterest is North Eastern Part of Berlin, Germany. Picture can be found [here](https://user-images.githubusercontent.com/75158219/125793336-f5376d2b-d7e4-422f-84db-51c812989205.png) or from `images\Task1_KeplerGLLocationDetection.png`

3. I was downloading the data from USGS Gov Website [[2]](#2), but the partnership between ESA and the USGS allows only for the distribution of Level-1C. As per the Task we need Level 2-A Data. 

4. Finally, I downloaded the data from Copernicus Open Access Hub [[3]](#3) with the following properties :
   * Selected the Berlin Location
   * In the advanced search I selected Mission - Sentinel 2
   * Product Type as S2MSI2A
   * Year 2020 
   * (Through this I was able to download the correct data with the requirement - `Sentinel-2 level 2A tile from any practical TOI (2019 or 2020)`

5. I selected the 12 (Total 13, but removed 10 - cirrus band which gives no ground information) specific bands which are needed and put them in the folder `13bands` from the .SAFE folder data structure downloaded from Copernicus Access Hub. I refered the information of the Sentinel 2 bands from Wikipedia [[4]](#4)

6. I selected the SCL Layer (20m), and opened it in SQIS to make the `NO_DATA`,`SATURATED_OR_DEFECTIVE`, `CLOUD_HIGH_PROBABILITY` as NOVALUE, (*In QGIS, we get an option to set the No Data Values when saving the Raster Layer*) and saved the new file as `data\13bands\scllayer_nodata_band.tif` . The label for each classification I found from the Sentinel Website [[5]](#5)

7.  I opened those 13 Bands (12 + 1 SCL) in the QGIS and created a Virtual Layer.

8.  There was a color mismatch so I edited the virtual layer and set the BGR (Bands 2,3,4 respectively), and I was able to see an observable satellite map of Berlin (And its surroundings). I got the information of the bands from SatimagingCorp website. [[6]](#6)

9.  I could see the Satellite images have an EPSG of 32633, hence I created a new AOI with EPSG 32633 with the name as `data\remote_sensing_challenge_AOI32633.geojson`

10. Just to validate the Correct data has been downloaded, I verified by adding the AOI on top of the layer, and the image can be seen [here](https://user-images.githubusercontent.com/75158219/125833711-6d6af508-8483-416e-ad5d-85e8f72b7954.png) or from `images\Task1_satellite_aoi_validate.png`

11. All the bands (12 + SCL with NOVALUE for 3 parameter) were merged into a GeoTIFF. (`data\mergedBandswithSCL.tif`), which will serve as the input for the clipping in the jupyer notebook. 

12. I clipped the input of the `mergedBandswithSCL.tif` which can be found in the `Task1_ClippingSentinel2Data.ipynb` file.

12. The Final Output can be seen below (With the AOI) or in the file `images\task1_clipped_output.png` and the final clipped GeoTIFF will be found in `data\clippedGeoTIFF.tif`

![image](https://user-images.githubusercontent.com/75158219/125858178-eb84d6a2-deb5-4ced-bedc-46dea4563f93.png)


### Uses 

**Data Clipping** - As the data from Satellite Hubs which gets downloaded are far enormous than the Area of Interest, thus clipping helps us to trim the map (data) which only contains the information of and around the Area of Interest. The clipped data is considerably less in size helps to process the data faster. 

### References

* <a id="1">[1]</a> 
https://drive.google.com/file/d/1cYulst52qOsx1VOOtVQo5sRdUugYqEpl/view
* <a id="2">[2]</a> 
https://www.usgs.gov/centers/eros/science/usgs-eros-archive-sentinel-2?qt-science_center_objects=0#qt-science_center_objects
* <a id="3">[3]</a> 
https://scihub.copernicus.eu/dhus/#/home
* <a id="4">[4]</a> 
https://en.wikipedia.org/wiki/Sentinel-2#Spectral_bands
* <a id="5">[5]</a> 
https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-2a/algorithm
* <a id="6">[6]</a> 
https://www.satimagingcorp.com/satellite-sensors/other-satellite-sensors/sentinel-2a/



