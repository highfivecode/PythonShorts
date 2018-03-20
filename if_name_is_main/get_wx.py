"""
Requires requests library. install it via pip:
$ pip install requests
HFC YouTube Channel here: https://www.youtube.com/channel/UCOmiui0ghT5OoVdD1wi4mFA
Ask for requests here: https://highfivecode.com/suggestions/
"""
import os
import requests

# try:
#     APIKEY = os.environ['WXAPI']
# except KeyError as error:
#     print("KeyError: Unable to find environment variable: {}".format(error))
#     print("Please set this variable in .bashrc (export WXAPI=some_api_key)")
#     print("Exiting")
#     exit()

API_KEY = "PUT YOUR API KEY HERE, GET IT FROM: http://api.openweathermap.org"

def get_weather_for_zip(zip_code, units="imperial"):
    """
    Gets weather from Open Weather Map for a given zip code
    @param zip_code: string => the zip code to query for
    @returns json
    """
    query = "http://api.openweathermap.org/data/2.5/"
    query += "weather?zip={},us".format(zip_code)
    query += "&units={}".format(units)
    query += "&APPID={}".format(APIKEY)
    r = requests.get(query)
    data = r.json()
    return data

if __name__ == "__main__":
    print("message from get_wx: My Name Is Main")
    current_wx = get_weather_for_zip("90210")
    print(current_wx)
else:
    print("message from get_wx: My Name Is Not Main, it is {}".format(__name__))
