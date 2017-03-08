import requests
import datetime

def forecast():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=588409,ee&units=metric&appid=44b04c5c9801970e82bb155d508f5666')
    data = r.json()
    temp = data['main']['temp']
    time_data = data['dt']
    result = int(temp)
    time = int(time_data)

    icon = data['weather'][0]['icon']
    iconstr = str(icon)
    print(iconstr)
    print(result)
    print((datetime.datetime.fromtimestamp(time)).strftime('%H:%M:%S'))

    if result < 0:
        print("TODAY IS FUCKING COLD!")
    else:
        print("UHH, IT MAY BE BETTER...")


if __name__ == '__main__':
    forecast()