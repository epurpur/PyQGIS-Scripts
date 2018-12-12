#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:47:16 2018

@author: ep9k
"""
import json
import requests

def multiple_dynamic_api_requests(city_id_list):
    """Cannot submit a string of city_ids to API request, so I need to loop through and create each API request individually.
    Each loop takes the city ID and makes an API request with it.
    This goes into daily_forecast_functions.py and uses state_choice() function
    city_id_list is returned from state_choice and adds them into api request to return weather for city, based on its unique city_id."""

    json_data_list = []             #need to create a list to store json data, so we capture all data from each state (and locations within that state) per API request

    for city_id in city_id_list:

        request = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID=333de4e909a5ffe9bfa46f0f89cad105&units=imperial&')   #5 day forecast request format
        json_data = json.loads(request.text)
        json_data_list.append(json_data)

    return json_data_list


def calc_best_daily_conditions(json_data_list):
    """Calculates best conditions by day for each day of the 5 day forecast.
    I take daily conditions at 12 Noon for each city, for each day and put them in conditions_list.
    Then I make a  key, value pair in min_score_by_date dictionary by first looking if date is in dictionary or if conditions_score is less than the current conditions score for that date.
    If those conditions are true it creates a dict object for each day ex: {'2018-11-14': ('Boone', 2276.4356)}

    I will format output more in the future with more information about each place by day."""

    conditions_list = []

    for city in json_data_list:
        for daily_measurement in city['list']:
            if daily_measurement['dt_txt'][11:20] == '12:00:00':        #this is the time in the string. Looks for the time = Noon for each day. 
                city_name = city['city']['name']
                conditions_score = (daily_measurement['main']['temp']) * (daily_measurement['main']['humidity'])        #calculates conditions score for the day as temp x humidity. This logic has some flaws.
                date = daily_measurement['dt_txt'][:11]                 #this is the date in the string
                conditions_list.append((city_name, conditions_score, date))         #appends values as one tuple ex: ('Pickens', 4202.55, '2018-11-13 ')

    if len(conditions_list) == 0:         #this checks if conditions_list is empty, if so it is probably due to user choosing a state which is not in 'ClimbingAreasInfo.csv'. This is effectively error handling.
        print("***No Data to process. You probably chose a state that is not in the database. Choose another state.")

    min_score_by_date = {}
    for city_name, conditions_score, date in conditions_list:
        if date not in min_score_by_date or conditions_score < min_score_by_date.get(date)[1]:  #looks to see if data is not in dict yet. Or if conditions score is less than the min score for that individual date
            min_score_by_date[date] = (city_name, conditions_score)

    for key, value in min_score_by_date.items():
        print(f"Best conditions on {key}will be in {value[0]}")
