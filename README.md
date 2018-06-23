#Geo Tagger

This is geotagging program which takes images folder, output folder and csv as input.

The CSV format should be contain only 4 columns. Example is given below
    
Images, Lat, Long, Elevation

DSC124.JPG , 23.34354 , 78.3254543 , 235.34

Inputs require
1. Input Folder containing Images
2. Output Folder after geotagging
3. CSV File containing geotag information

Dependencies

1. pandas - pip install pandas
2. Tkinter - pip install Tkinter
3. pexif - https://github.com/mcbridejc/pexif.git