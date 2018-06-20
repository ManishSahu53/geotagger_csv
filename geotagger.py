import pexif,os
import numpy as np
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import * 
import pandas as pd

input_location = tkFileDialog.askdirectory(initialdir = "/",title = "Select input photos location");
output_location = tkFileDialog.askdirectory(initialdir = "/",title = "Select output photos location");

csv_file = tkFileDialog.askopenfilename(initialdir = "/",title = "Select geolocation csv file",filetypes = (("csv files","*.csv"),("all files","*.*")))

a= pd.read_csv(csv_file)
for i in range(len(a)):
    jpeg = pexif.JpegFile.fromFile(input_location + "/" + a['Images'][i]);
    (lat,lng)=(a['Lat'][i], a['Long'][i]);
    jpeg.set_geo(lat, lng)
    new_file = jpeg.writeString()
    new = pexif.JpegFile.fromString(new_file)
    new_lat, new_lng = new.get_geo()
    jpeg.writeFile(output_location + "/" + "geo_"+ a['Images'][i])
    print("Completed " + str(i) + " images, out of " + str(len(a)) + " images");
