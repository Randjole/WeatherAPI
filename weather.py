import requests
import pprint
from ratelimit import limits, sleep_and_retry

base_url ="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"



class weather():
    

    time_period = 300
    @sleep_and_retry
    @limits(calls=5, period=time_period )
    def get_function(self):
        
        city_name = input('Enter city name: ')
        date1 = input('Enter date: ')
        date2 = input('Enter another date: ')
        key_api = input('Enter you key/token: ')
        
        url = f'{base_url}/{city_name}/{date1}/{date2}?key={key_api}'
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            pprint.pp(weather_data)

        
        else:
            print(f'Failed to retrive data {response.status_code}')    


        
    def main(self):
        resp = weather()
        print('****Weather API****')
        while True:
            resp.get_function()

  


if __name__=='__main__':
    activate = weather()
    work = activate.main()
    





# key = EX7HPKDCC86NKU4SFN68AU22H


    

  