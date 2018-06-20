import pexif
import tkFileDialog
import pandas as pd

input_location = tkFileDialog.askdirectory(initialdir = "/",title = "Select input photos location");
output_location = tkFileDialog.askdirectory(initialdir = "/",title = "Select output photos location");

csv_file = tkFileDialog.askopenfilename(initialdir = "/",title = "Select geolocation csv file",filetypes = (("csv files","*.csv"),("all files","*.*")))

a= pd.read_csv(csv_file);
for i in range(len(a)):
    jpeg = pexif.JpegFile.fromFile(input_location + "/" + a['Images'][i]);
    (lat,lng,alt)=(a['Lat'][i], a['Long'][i],a['Elevation'][i]);
    jpeg.set_geo(lat, lng, alt);
    jpeg.writeFile(output_location + "/" + a['Images'][i]);
    print("Completed " + str(i) + " images, out of " + str(len(a)) + " images");
