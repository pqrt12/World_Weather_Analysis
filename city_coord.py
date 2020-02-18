
# create 1500 random coordinates, and get the nearest city name.
# output to "Resources/city_coord.csv"


# Import the dependencies.
import pandas as pd
import numpy as np

# Use the citipy module to determine city based on latitude and longitude.
from citipy import citipy

# Create a list for holding the cities.
def get_city_coord(coordinates):
    cities = []
    city_coord = []
    # Identify the nearest city for each latitude and longitude combination.
    for coordinate in coordinates:
        city = citipy.nearest_city(coordinate[0], coordinate[1]).city_name
    
        # If the city is unique, then we will add it to the cities list.
        if city not in cities:
            cities.append(city)
            city_coord.append([city, coordinate[0], coordinate[1]])

    # Print the city count to confirm sufficient count.
    city_count = len(cities)
    print(f"valid city count is {city_count}")
    return city_coord


# return a list of coordinates.
def get_lat_lngs(size = 1500):
    # Create a set of random latitude and longitude combinations.
    lats = np.random.uniform(low=-90.000, high=90.000, size=size)
    lngs = np.random.uniform(low=-180.000, high=180.000, size=size)
    lat_lngs = zip(lats, lngs)

    # Add the latitudes and longitudes to a list.
    coordinates = list(lat_lngs)
    return coordinates

def create_city_list(size = 1500):
    coordinates = get_lat_lngs(size)
    city_coord = get_city_coord(coordinates)

    cities = [e[0] for e in city_coord]
    lats =   [e[1] for e in city_coord]
    lngs =   [e[2] for e in city_coord]

    df = pd.DataFrame({
        "City" : cities,
        "Lat" : lats,
        "Lng" : lngs})

    print(df.head(1))

    # dump to a csv file
    df.to_csv(r'Resources\city_coord.csv')

if __name__ == "__main__":
    create_city_list(4000)
