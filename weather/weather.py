import requests

api_address='https://api.openweathermap.org/data/2.5/weather?appid=4e4049498f5fd8ac61f8460d94449a3b&q='
city=input("City Name:")
url=api_address + city
json_data=requests.get(url).json()
print(json_data)
