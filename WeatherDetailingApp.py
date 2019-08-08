import requests

url_for_city='http://api.openweathermap.org/data/2.5/weather?appid=b89f8f9b052ef9a2f623f5ee4924c11e&q='
city=input('Enter the City Name: ')

final_url=url_for_city+city
json_var=requests.get(final_url).json()
print('The current Weather details of the city',city,'are as follows: ')
weather_detail=json_var['weather'][0]['main']
temp_detail=json_var['main']['temp']
humid_detail=json_var['main']['humidity']
#print(json_var)
print('WEATHER:',weather_detail)
print('TEMPERATURE:',temp_detail-273.15,'Celcius')
print('HUMIDITY:',str(humid_detail)+'%')
