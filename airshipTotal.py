import math
def calculate_trips(W, theta):
   # Constants
   distance_nm = 35  # Distance in nautical miles
   airspeed_kt = 65  # Aircraft's true airspeed in knots
   total_hours_per_day = 24  # Total hours in a day


   # Convert theta to radians for the two angles used in the formula
   theta_rad_1 = math.radians(90.8-theta)
   theta_rad_2 = math.radians(270.8-theta)


   # Calculate the wind correction
   wind_correction_1 = W * math.cos(theta_rad_1)
   wind_correction_2 = W * math.cos(theta_rad_2)


   # Calculate the times for going and return trips
   time_outbound = distance_nm / (airspeed_kt - wind_correction_1)
   time_return = distance_nm / (airspeed_kt - wind_correction_2)


   # Calculate the total time per trip (adding 1 hour for turnaround, 30 min each side)
   total_time_per_trip = time_outbound + time_return + 1


   # Calculate the number of trips
   T = total_hours_per_day / total_time_per_trip


   return T

#wind parameters
W = float(input("Wind speed in knots: "))  # Wind speed in knots
theta = float(input("Wind direction in degrees: "))  # Wind direction in degrees

# Calculate trips
trips = calculate_trips(W, theta)
print(f"The maximum number of trips that can be made in a day is: {trips}")


# function to find number of airships
def findAirships():
    thingsperDay = float(input("Things per day: "))
    tripsperDay = trips # float(input("Trips per day: "))
    thingspertimetabledSlot = thingsperDay/tripsperDay
    thingaverageWeight = float(input("Average weight of thing: "))
    airshipweightLimit = float(input("Airship weight limit: "))

    """
    n is rounded up because if we need 1.4 
    airships, 1 is not enough and we cannot have 1.4
    therefore the lowest number of airships to match
    the demand is 2.
    """
    n = round(thingspertimetabledSlot*thingaverageWeight/airshipweightLimit + 0.5, 0)
    # leftoverSpace = round((thingspertimetabledSlot*thingaverageWeight/(2*airshipweightLimit)*airshipweightLim  it), 0)
    return n#, leftoverSpace)


while True:
    n = findAirships()
    print("You need", int(n), "airships")# and would have", leftoverSpace, "kilograms of spare space.")

