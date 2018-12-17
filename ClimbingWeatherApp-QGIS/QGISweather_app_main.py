#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:11:02 2018

@author: ep9k
"""

#This is the main module for my weather app
#I'm submitting an API request to Open Weather Map's API (https://openweathermap.org/api)

import QGISdaily_forecast_functions as dff


def main():
    """Weather app main module
    daily_forecast_functions and extended_forecast_functions contain individual descriptions of what each function does"""
    
    print("~~~~~~Erich's Weather~~~~~~~~")
    print("We will check the weather at various climbing destinations by state")

    user_state_choice = dff.state_choice(input("Enter state abbreviation (in caps) : "))    #gets user input for state abbreviation

    city_id_list = user_state_choice[0]     #list of city ids returned from state_choice
    climbing_area_alias = user_state_choice[1]  #list of climbing area aliases returned from state_choice
    zip_codes = user_state_choice[2]        #list of zip codes for each location returned from state_choice
    
    json_data = dff.single_dynamic_api_request(city_id_list)    #returns JSON data for each API request (city) in chosen state

    conditions = dff.display_conditions_today(json_data, climbing_area_alias, zip_codes)    #returns dictionary of cities with conditions score as a dictionary
        
    dff.output_for_QGIS(conditions, zip_codes)          #processes final output for QGIS in temp.csv file

    #Here is where the QGIS specific functions begin
    
main()

    