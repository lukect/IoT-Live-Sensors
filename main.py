from random import randrange
from threading import Thread
from time import sleep

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


def read_sensors():
    global temperature
    global humidity
    while True:
        temperature = randrange(100, 400) / 10
        humidity = randrange(0, 1000) / 10
        sleep(1)


sensor_thread = Thread(name='read_sensors', target=read_sensors)
sensor_thread.start()
