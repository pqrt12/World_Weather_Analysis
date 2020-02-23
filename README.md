# World_Weather_Analysis

# Challenge
## Part 1, Get Each City's Weather Description and Precipitation
  Weather_Database.ipybt
- Generate 1500 random coordinates
- Found 623 cities near those coordinates.
- request openweathermap for weather info. 
- only 570 cities are supported.  
- retrieved whether info is saved in "data\WeatherPy_challenge.csv".
- There are 78 Cities have recorded rainfall or snow in the past 3 hours.

## Part 2, Narrow Travel Searches Based on Weather  
  Vacation_Search.ipynb
- Asking customer for temperature ranges, prefer raining, prefer snowing?
- Prefered Cities are selected, stored in hotel_df.
  as an example, temparature range chosen is (35.0, 60.0) Fahrenheit, no rain, no snow.
- One hotel per prefered city is chosen.
- Gmaps with a pop-up marker layer for the prefered cities.
  ![WeatherPy_vacation_map](https://github.com/pqrt12/World_Weather_Analysis/blob/master/image/WeatherPy_vacation_map.png)
- the DataFrame is saved to "data\WeatherPy_vacation.csv".

## Part 3, Travel Itinerary Map.
  Vacation_Itinerary.ipybt
- Choose four cities from "data\WeatherPy_vacation.csv"  
  as an example, these cities are chosen:  
  "Mayo", "Bethel", "Southbridge", "Yarmouth"
- Create a Gmap with a travel direction layer.
  ![WeatherPy_travel_map](https://github.com/pqrt12/World_Weather_Analysis/blob/master/image/WeatherPy_travel_map.png)  
- Create a Gmap with a pop-up marker layer.
  ![WeatherPy_travel_map_markers](https://github.com/pqrt12/World_Weather_Analysis/blob/master/image/WeatherPy_travel_map_markers.png) 
