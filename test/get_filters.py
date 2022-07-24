import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# def get_filters():
#     """
#     Asks user to specify a city, month, and day to analyze.

#     Returns:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     """
#     print('Hello! Let\'s explore some US bikeshare data!')
#     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#     city = input("Chose which city to extract data from (chicago, new york city, washington) and enter its name: ").lower()
#    while CITY_DATA.get(city) == None:
#     print("wrong answer")
#     city = input("chose a city from this list (chicago, new york city, washington)\n")
#     # TO DO: get user input for month (all, january, february, ... , june)
#     months = ['january', 'february', 'march', 'april', 'may', 'june']                 
#     month = input("Which month you want to view ? enter name of month from (january to june) or enter \"all\" for all months: ").lower()
#     while month not in months and month != 'all':
#         month = input("please chose a name of month or enter \"all\": ")             
#     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
#     days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']                 
#     day = input("Enter the day of week you want to view or enter \"all\" for all days: ").lower()
#     while day not in days and day != 'all':
#         day = input("Please Enter the day of week you want to view or enter \"all\" for all days: ")             
#     print('-'*40)
#     return city, month, day
# print(get_filters())
                     
print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
city = input("Chose which city to extract data from (chicago, new york city, washington) and enter its name: ").lower()
# print(CITY_DATA.get(city))
while CITY_DATA.get(city) == None:
    print("wrong answer")
    city = input("chose a city from this list (chicago, new york city, washington)\n")
#     city = input("please chose one city of (chicago, new york city, washington): "
# while CITY_DATA.get(city) == None:
#     print("wrong answer")
#     city = input("please chose one city of (chicago, new york city, washington): "
    #TO DO: get user input for month (all, january, february, ... , june)
months = ['january', 'february', 'march', 'april', 'may', 'june']                 
month = input("Which month you want to view ? enter name of month from (january to june) or enter \"all\" for all months: ").lower()
while month not in months and month != 'all':
      month = input("please chose a name of month or enter \"all\": ")             
#     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
#     days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']                 
#     day = input("Enter the day of week you want to view or enter \"all\" for all days: ").lower()
#     while day not in days and day != 'all':
#         day = input("Please Enter the day of week you want to view or enter \"all\" for all days: ")             
#     print('-'*40)