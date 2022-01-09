import python_weather
import json
import requests

api_key="1fb092a7559461516e72df89f34c1887"
url="http://api.openweathermap.org/data/2.5/weather?"
city=input("enter city name:")
final_url=url+"q="+city+"&appid="+api_key

response=requests.get(final_url)
data=response.json()
main=data['main']
temp="{:.2f}".format(main['temp']-273)
feels_like="{:.2f}".format(main['feels_like']-273)
temp_min="{:.2f}".format(main['temp_min']-273)
temp_max="{:.2f}".format(main['temp_max']-273)
pressure=main['pressure']
humidity=main['humidity']
weather=data['weather']
des=weather[0]['description']
wind=data['wind']
w_speed=wind['speed']

print(f"{city} weather data=>\n temp:{temp}C feels like:{feels_like}C temp min:{temp_min}C temp max:{temp_max}C")
print(f" pressure:{pressure} \t humidity:{humidity}\t wind speed:{w_speed}\t description:{des}")

print
                               
