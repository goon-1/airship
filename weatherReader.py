#Reads raw weather data and calculates average wind speed and direction at Cape Campbell

totalWindspeed = 0
totalDirection = 0
Counter = 0
windcounter = 0
date = []
max = 0
for line in open("data.dat"):
   columns = line.split(",")
   Counter += 1
   wind = float(columns[4])
   print(columns[3])
   try:
       direction = int(columns[3])
       totalDirection+=direction
   except:
       pass


   totalWindspeed += wind
   if wind>max:
       max = wind
       maxdir = columns[3]
   if wind>12.8:


       windcounter += 1

   #print(columns[4])


avgWind = totalWindspeed/Counter
avgHeading = totalDirection/Counter
print("The Average wind speed is " + str(avgWind) + " m/s at a bearing of "+ str(avgHeading))
print("Max wind speed: " + str(max)+ " at " + maxdir)
print(windcounter)
print(Counter)
