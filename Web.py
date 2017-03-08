import requests
import datetime
from flask import Flask
from flask import json
from flask import render_template

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!!!!!!!!!!"

@app.route('/')
@app.route('/index')
def index():
    forecast_data = {'temp': forecast(), 'answer':answer(), 'time':time(), 'icon':icon(), 'pic':pic()}
    return render_template("index.html", title = 'Get_Forecast', forecast=forecast_data)

@app.route("/tll")
def forecast():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=588409,ee&units=metric&appid=44b04c5c9801970e82bb155d508f5666')
    data = r.json()
    temp = data['main']['temp']
    result = int(json.dumps(temp))
    return result

def icon():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=588409,ee&units=metric&appid=44b04c5c9801970e82bb155d508f5666')
    data = r.json()
    icon = data['weather'][0]['icon']
    result = json.dumps(icon)[1:-1]
    return result

def time():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=588409,ee&units=metric&appid=44b04c5c9801970e82bb155d508f5666')
    data = r.json()
    time_data = data['dt']
    time = int(json.dumps(time_data))
    return ((datetime.datetime.fromtimestamp(time)).strftime('%H:%M:%S'))

def answer():
    if forecast() < 0:
        return "TODAY IS FUCKING COLD!"
    else:
        return "UHH, IT MAY BE BETTER..."

def pic():
    if 4 < 0:
        return "big.jpg"
    else:
        return "small.jpg"

if __name__ == "__main__":
    app.run ()