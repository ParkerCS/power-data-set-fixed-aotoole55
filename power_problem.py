'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format. (i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big dataset.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).  This rate includes transmission fees and grid fees that are part of the true rate.
'''
import csv
from operator import itemgetter

file = open('power_data.csv', 'r')

rate_list = []

reader = csv.reader(file, delimiter = ',')
##delimiter separates each piece of data

for row in reader:
    rate_list.append(row)

print(rate_list)

#1  What is the average residential rate for YOUR zipcode? You will need to read the power_data into your program to answer this.  (7pts)

residential_rate = []
zip_code = []
for i in range(len(rate_list)):
    zip_code.append(rate_list[i][0])
    residential_rate.append(rate_list[i][8])

zip_number = residential_rate[zip_code.index('60614')] #finds 60614
print('The average residential rate in 60614 is:', zip_number)



#2 What is the MEDIAN rate for all BUNDLED RESIDENTIAL rates in Illinois? Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)

median_rate = []

for i in range(len(rate_list)):
    if rate_list[i][3] == 'IL' and rate_list[i][4] == 'Bundled':
        median_rate.append(rate_list[i][8])
median_number = median_rate[(len(median_rate))//2]
print('The median residential rate is: ', median_number)


#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one. Then you will need to reference the zipcode dataset to get the city.  (15pts)
ill_list = []
zip_list = []
zip_low_list = []
zip_high_list = []

file2 = open('free-zipcode-database-Primary.csv', 'r')

city_list = []

reader2 = csv.reader(file2, delimiter = ',')
##delimiter separates each piece of data

for row in reader2:
    city_list.append(row)


#Highest and lowest values
for i in range(len(rate_list)):
    if rate_list[i][3] == 'IL' and rate_list[i][4] == 'Bundled':
        ill_list.append(rate_list[i][8])
        zip_list.append(rate_list[i][0])

ill_list = sorted(ill_list)


lowest = ill_list[0]
highest = ill_list[len(ill_list)-1]


#zipcode for highest and lowest values
for i in range(len(rate_list)):
    if rate_list[i][8] == lowest and rate_list[i][3] == 'IL' and rate_list[i][4] == 'Bundled':
        zip_low_list.append(rate_list[i][0])
    if rate_list[i][8] == highest and rate_list[i][3] == 'IL' and rate_list[i][4] == 'Bundled':
        zip_high_list.append(rate_list[i][0])


city_high_name = []
city_low_name = []


for i in range(len(city_list)):
    if city_list[i][0] == zip_low_list[0]:
        city_low_name.append(str(city_list[i][2]))
    if city_list[i][0] == zip_high_list[0]:
        city_high_name.append(str(city_list[i][2]))

print('The city with the lowest residential rate is:', city_low_name[0])
print('The city with the highest residential rate is: ', city_high_name[0])



#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.  Make the marker size vary depending on the population contained in that zip code.  Add an alpha value to the marker so that you can see overlapping markers.
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

data = []
size = []
zip_code = []
longitude = []
latitude = []

for i in range(len(rate_list)):
    if rate_list[i][3] == 'IL' and rate_list[i][4] == 'Bundled':
        data.append(rate_list[i])

data = sorted(data, key = lambda x: x[8])

for i in range(len(city_list)):
    if city_list[i][3] == "IL":
        zip_code.append(city_list[i][0])
        longitude.append(city_list[i][6])
        latitude.append(city_list[i][5])
        if city_list[i][10] == '':
            size.append('0')
        else:
            size.append(city_list[i][10])

for j in range(len(size)):
    size[j] = int(size[j]) / 100

plt.figure(figsize = [9, 7], tight_layout=True)
plt.subplot(1,2,1)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title('Population by Zipcode')

plt.scatter(longitude, latitude, s = size, alpha = 0.18)


plt.show()

#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.  Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay a rate in the bottom 50% of residential power cost.  This one is very challenging.  You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)





#Made an attempt. I don't think I color coordinated it correctly, though.



'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

ill_rates = []
top25 = []
middle = []
bottom50 = []
latitude =[]
longitude = []
zip_color = []
color = []
zip_ill_list = []


file2 = open('free-zipcode-database-Primary.csv', 'r')

city_list = []

reader2 = csv.reader(file2, delimiter = ',')
##delimiter separates each piece of data

for row in reader2:
    city_list.append(row)
print(rate_list)

for i in range(len(rate_list)):
    if rate_list[i][3] == 'IL' and rate_list[i][4] == 'Bundled':
        ill_rates.append(rate_list[i])

ill_rates = sorted(ill_rates, key = lambda x: x[8])

print(ill_rates)

#Grouping into percentile
for i in range(len(ill_rates)):
    if i >= int(0.75*len(ill_rates)):
        top25.append(ill_rates[i])
    elif i >= int(0.25 * len(ill_rates)) and i < int(0.75*len(ill_rates)):
        middle.append(ill_rates[i])
    else:
        bottom50.append(ill_rates[i])

city_list = sorted(city_list, key = lambda x: x[0])

#latitude and longitude
for i in range(len(city_list)):
    if city_list[i][3] == 'IL':
        latitude.append(city_list[i][5])
        longitude.append(city_list[i][6])


for val in top25:
    zip_color.append([int(val[0]), 'red'])
for val in middle:
    zip_color.append([int(val[0]), 'yellow'])
for val in bottom50:
    zip_color.append([int(val[0]), 'green'])

for i in range(len(zip_color)):
    color.append(zip_color[i][1])

print(longitude)
print(latitude)
print(color)


plt.figure(figsize = [9, 7], tight_layout=True)

plt.subplot(1,2,1)

plt.xlabel('Longitude')

plt.ylabel('Latitude')

plt.title('Residential Power Rate by Zip Code')

plt.scatter(longitude, latitude, color = color, s = 15)

plt.show()
'''