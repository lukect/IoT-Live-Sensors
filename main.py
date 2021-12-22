import subprocess
from threading import Thread
from time import sleep

import Adafruit_DHT
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

html = Jinja2Templates(directory="html")

temperature = 0
humidity = 0


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    global temperature
    global humidity
    return html.TemplateResponse("main.html",
                                 {"request": request, "temp": format1dp(temperature), "humid": format1dp(humidity)})


@app.get("/sensor/data")
async def sensor_data():
    global temperature
    global humidity
    return {"temp": format1dp(temperature),
            "humid": format1dp(humidity)}


def format1dp(num):
    if num is not None:
        return "{0:.1f}".format(num)
    else:
        return None


@app.get("/shutdown")
async def shutdown():
    subprocess.Popen("sleep 1 ; sudo shutdown -h now", shell=True)
    return {"shutdown": 1}


@app.get("/reboot")
async def reboot():
    subprocess.Popen("sleep 1 ; sudo shutdown -r now", shell=True)
    return {"reboot": 1}


sensor = Adafruit_DHT.DHT11
sensor_pin = 11


def read_sensors():
    global temperature
    global humidity
    while True:
        humidity, temperature = Adafruit_DHT.read(sensor, sensor_pin)
        sleep(2)


sensor_thread = Thread(name='read_sensors', target=read_sensors)
sensor_thread.start()
