import requests
import datetime
import pyowm

class Forecast:

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=588409,ee&units=metric&appid=44b04c5c9801970e82bb155d508f5666')
    data = r.json()

    def get_temp(self):
        temp = self.data['main']['temp']
        result = int(temp)
        return result

    def icon(self):
        icon = self.data['weather'][0]['icon']
        result = int(icon)[1:-1]
        return result

    def get_time(self):
        time = self.data['dt']
        result = (datetime.datetime.fromtimestamp(int(time))).strftime('%H:%M:%S')
        return result

    def __str__(self):
        return "Weather data updated at " + self.get_time() + "\nTemperature is now {0}C°".format(self.get_temp())
#
# c = Forecast()
# owm = pyowm.OWM('44b04c5c9801970e82bb155d508f5666')
# d = owm.is_API_online()
# print(d)
# print(c.get_temp())
# print(c)
