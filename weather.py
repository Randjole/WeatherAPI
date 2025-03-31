import requests
import pprint

base_url ="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"


def get_function():
    
    key_api = 'EX7HPKDCC86NKU4SFN68AU22H'
    city_name = input('Enter city name: ')
    date1 = input('Enter date like this ~ 2020-10-19: ')
    
    url = f'{base_url}/{city_name}/{date1}?key={key_api}'
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        pprint.pp(weather_data)
    
    else:
        print(f'Failed to retrive data {response.status_code}')    

    

get_function()    


    

  