import requests
import datetime
from flask import Flask
from flask import json
from flask import render_template
from flask import request, redirect, url_for
'''Whether analyzer in Tallinn, which show it in browser(by flask)
some helpful information (decide what to wear for a walk)'''

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!!!!!!!!!!"


def intro(town="Tallinn"):
    srclink = 'http://api.openweathermap.org/data/2.5/weather?q=' + town +'&units=metric&appid=44b04c5c9801970e82bb155d508f5666'
    r = requests.get(srclink)
    data = r.json()
    return data


@app.route('/', methods=['POST', 'GET'])
def index(g="Tallinn"):

    if request.method == 'POST':
        g = request.form['town']
        if g == "":
            g = "Tallinn"
            print("That's OK " + g)
            forecast_data = {'temp': forecast(g), 'time': time(g), 'icon': icon(g), 'pic': pic(g),
                             'desc': weather_name(g), 'clouds': clouds(g), 'wind_speed': wind_speed(g), 'wind_deg': wind_deg(g),
                             'town': g, 'rain':umbrella(g)}
            return render_template("index.html", title='Get_Forecast', forecast=forecast_data)
        else:
            forecast_data = {'temp': forecast(g), 'time': time(g), 'icon': icon(g), 'pic': pic(g),
                             'desc': weather_name(g), 'clouds': clouds(g), 'wind_speed': wind_speed(g),
                             'wind_deg': wind_deg(g),
                             'town': g, 'rain': umbrella(g)}
            return render_template("index.html", title='Get_Forecast', forecast=forecast_data)
    else:
        forecast_data = {'temp': forecast(g), 'time': time(g), 'icon': icon(g), 'pic': pic(g),
                         'desc': weather_name(g), 'clouds': clouds(g), 'wind_speed': wind_speed(g), 'wind_deg': wind_deg(g),
                         'town': g, 'rain':umbrella(g)}
        return render_template("index.html", title='Get_Forecast', forecast=forecast_data)


@app.route("/tll")
def forecast(a="Tallinn"):
    # r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=588409,ee&units=metric&appid=44b04c5c9801970e82bb155d508f5666')
    # data = r.json()
    data = intro(a)
    temp = data['main']['temp']
    result = float(json.dumps(temp))
    return result


def weather_name(a="Tallinn"):
    data = intro(a)
    icon = data['weather'][0]['description']
    result = json.dumps(icon)[1:-1].capitalize()
    return result

def clouds(a="Tallinn"):
    data = intro(a)
    icon = data['clouds']['all']
    result = json.dumps(icon)
    return result

def wind_speed(a="Tallinn"):
    data = intro(a)
    icon = data['wind']['speed']
    result = float(json.dumps(icon))
    return result



def wind_deg(a="Tallinn"):
    data = intro(a)
    icon = data['wind']['deg']
    degree = float(json.dumps(icon))
    if (degree>337.5):
        return 'Northerly'
    elif (degree>292.5):
        return 'North Westerly'
    elif(degree>247.5):
        return 'Westerly'
    elif(degree>202.5):
        return 'South Westerly'
    elif(degree>157.5):
        return 'Southerly'
    elif(degree>122.5):
        return 'South Easterly'
    elif(degree>67.5):
        return 'Easterly'
    elif(degree>22.5):
        return 'North Easterly'
    else:
        return 'Northerly'


def icon(a="Tallinn"):
    data = intro(a)
    icon = data['weather'][0]['icon']
    result = json.dumps(icon)[1:-1]
    return result


def time(a="Tallinn"):
    data = intro(a)
    time_data = data['dt']
    time = int(json.dumps(time_data))
    return ((datetime.datetime.fromtimestamp(time)).strftime('%H:%M:%S'))



def umbrella(a="Tallinn"):
    data = intro(a)
    # d = data['main']['temp']
    name = data['weather'][0]['main']
    if name == "Thunderstorm" or name == "Drizzle" \
            or name == "Rain":
        return "rain.jpg"
    else:
        return "white.jpg"

@app.route("/pic")
def pic(a="Tallinn"):
    data = intro(a)
    # d = data['main']['temp']
    name = data['weather'][0]['main']
    d = forecast(a)
    # d = float(json.dumps(temp))
    # name = json.dumps(icon1)
    #name = weather_name(a)

    if d < -5: #colder -5 C°
        if name == "Snow" or name == "Atmosphere" or name == "Clear" \
                or name == "Clouds" or name == "Extreme" or name == "Additional" or name == "Mist" or name == "Haze":
            print(d, name)
            return "cold_dry.jpg"
        elif name == "Thunderstorm" or name == "Drizzle" \
            or name == "Rain":
            print(d, name)
            return "cold_rain.jpg"
    elif d >= -5 and d <= 5:  # -5 C° to 5 C° (forecast() < 0 and forecast() > -5)
        if name == "Snow" or name == "Atmosphere" or name == "Clear" \
                or name == "Clouds" or name == "Extreme" or name == "Additional" or name == "Mist" or name == "Haze":
            print(d, name)
            return "0_dry.jpg"
        elif name == "Thunderstorm" or name == "Drizzle" \
                or name == "Rain":
            print(d, name)
            return "0_rain.jpg"
    elif d > 5 and d <= 12: # 5 C° to 12 C°
        if name == "Snow" or name == "Atmosphere" or name == "Clear" \
                or name == "Clouds" or name == "Extreme" or name == "Additional" or name == "Mist" or name == "Haze":
            print(d, name)
            return "warm_dry.jpg"
        elif name == "Thunderstorm" or name == "Drizzle" \
                or name == "Rain":
            print(d, name)
            return "warm_rain.jpg"
    elif d > 12:  # 13 C° to HELL C°
        if name == "Snow" or name == "Atmosphere" or name == "Clear" \
                or name == "Clouds" or name == "Extreme" or name == "Additional" or name == "Mist" or name == "Haze":
            print(d, name)
            return "hot_dry.jpg"
        elif name == "Thunderstorm" or name == "Drizzle" \
                or name == "Rain":
            print(d, name)
            return "rain.jpg"


if __name__ == "__main__":
    app.run ()