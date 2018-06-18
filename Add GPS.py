import pexif,csv,os,sys,numpy as np
os.getcwd()
gps=np.zeros((1000,2));
with open('log.csv', mode='r') as f:
    reader = csv.reader(f)
    count=0;
    for row in reader:
        if row[0] in ['CAM']:
           # np.array(gps(count,:))=row;
           gps[count,0]=row[4];
           gps[count,1]=row[5];
           count=count+1;
           # print(row)

jpeg = pexif.JpegFile.fromFile("2.jpg")
(lat,lng)=(90.312312, 45.412321)
jpeg.set_geo(lat, lng)
new_file = jpeg.writeString()
new = pexif.JpegFile.fromString(new_file)
new_lat, new_lng = new.get_geo()
jpeg.writeFile("2_new.jpg")

with open('GeoIPCountryWhois.csv', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] in ['66.35.205.88']:
            print row