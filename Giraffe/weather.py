import requests

city=input("Enter your city name:")
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=4e4049498f5fd8ac61f8460d94449a3b'.format(city)
res=requests.get(url)
data=res.json()
print(res)
#print(data)

Temperature=data['main']['temp']
Latitude=data['coord']['lat']
Longitude=data['coord']['lon']
weather=data['weather'][0]['description']
wind_speed=data['wind']['speed']


print("Temperature: {} " .format(Temperature))
print("Latitude: {}" .format(Latitude))
print("Longitude:{}" .format(Longitude))
print("weather:{} " .format(weather))
print("wind_speed: {}" .format(wind_speed))
























