#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:11:02 2018

@author: ep9k
"""

#This is the main module for my weather app
#I'm submitting an API request to Open Weather Map's API (https://openweathermap.org/api)


import QGISdaily_forecast_functions as dff
import QGISextended_forecast_functions as eff

def main():
    """Weather app main module
    daily_forecast_functions and extended_forecast_functions contain individual descriptions of what each function does"""
    
    print("~~~~~~Erich's Weather~~~~~~~~")
    print("We will check the weather at various climbing destinations by state")

    forecast_time = input("Do you want today's forecast or 5 day forecast? (Enter [1] or [5]) : ")
    if forecast_time == '1':
        user_state_choice = dff.state_choice(input("Enter state abbreviation (in caps) : "))
    
        city_id_list = user_state_choice[0]     #list of city ids returned from state_choice
        climbing_area_alias = user_state_choice[1]  #list of climbing area aliases returned from state_choice
        zip_codes = user_state_choice[2]        #list of zip codes for each location returned from state_choice
    
        json_data = dff.single_dynamic_api_request(city_id_list)    #returns JSON data for each API request (city) in chosen state

        conditions = dff.display_conditions_today(json_data, climbing_area_alias, zip_codes)    #returns dictionary of cities with conditions score as a dictionary
        
        dff.output_for_QGIS(conditions, zip_codes)          #processes final output for QGIS in temp.csv file

    elif forecast_time == '5':

        user_state_choice = dff.state_choice(input("Enter state abbreviation (in caps) : "))      

        city_id_list = user_state_choice[0]     #list of city ids returned from state_choice
        
        json_data_list = eff.multiple_dynamic_api_requests(city_id_list)    #returns json_data for each time in 5 day forecast (at 3hr intervals) for each location
        eff.calc_best_daily_conditions(json_data_list)

        
    else:
        print("choose either 1 day or 5 day forecast")

    
if __name__ == '__main__':
    main()
    