import utm
import csv
from math import sqrt


file_path = '/Users/ep9k/Desktop/Distance calculation for track (corrected).csv'    #change this to where your input file is


with open(file_path) as csv_file:
#    headers = ['Nam', 'Altitud', 'Lon', 'Lat']
    reader = csv.DictReader(csv_file)
    
    lat_coords = []
    lon_coords = []
    alt_coords = []     #altitude coordinates
    
    for row in reader:
        lat_coords.append(float(row['Lat']))        #need to make these floats for utm.from_latlon
        lon_coords.append(float(row['Lon']))
        alt_coords.append(float(row['Altitud']))
        
        
coordinate_pairs = zip(lat_coords, lon_coords)      
#for coordinate in coordinate_pairs:
#    print(coordinate)                               #run this print statement to make sure coordinate pairs look right


converted_coordinates = []                          #this is a list of coordinate pairs
    
    
for lon, lat in coordinate_pairs:
    conversion = utm.from_latlon(lat, lon)
    converted_coordinates.append(conversion)        #does the math to convert coordinates from decimal degrees to meters using utm.from_latlon and then append them to converted_coordinates list
    
       
eastings = []                                       #easier to write to .csv if I separated the eastings and northings
northings = []
 
for lon, lat, zone_number, zone_letter in converted_coordinates:
    eastings.append(str(lon))                              #need to convert back to string to write to csv file
    northings.append(str(lat))
#    print(lon, lat)                                         #use this to verify output looks right

     
output_path = '/Users/ep9k/Desktop/csvexample.csv'         #change this to where you want to write the file to on your computer
output_file = open(output_path, 'w')
with output_file:
    writer = csv.writer(output_file)
    writer.writerows(zip(eastings, northings))              #writes eastings in one column, northings in next
    
    
#code for getting final answer?

#from math import sqrt
#
#a = [696263.035, 4381837.828, 1420.7]
#b = [696276.2649, 4381858.49, 1417.5]
#c = [696288.6723, 4381877.687, 1414.2]
#
#
#
#distance1 = (sqrt(sum( (a-b)**2 for a, b in zip(a, b))))
#distance2 = (sqrt(sum( (b-c)**2 for b, c in zip(b, c))))
#
#print(distance1)
#print(distance2)
    
    
        
    
    
    
    
    
    


#print(utm.from_latlon(39.078891, -79.018371))



