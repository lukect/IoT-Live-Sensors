# IoT Live Sensors

FastAPI backend serving live results to Web frontend over HTTP.

## Requirements

* PowerShell (Windows) or Bash (Linux)
* Python 3.7+
* Pip 21.2+

### Setup DHT sensor on Debian-based systems

Install GCC and Python headers: ```sudo apt-get install build-essential manpages-dev python3-dev```

Switch to the branch for your sensor: ```git checkout DHT11``` / ```git checkout DHT22```

#### Data Pin Connections

| Sensor | Pin |
|:------:|-----|
| DHT11  | 11  |
| DHT22  | 22  |

## Start

Before first-time start: *Run ```setup``` script as root/admin*

Start: *Run ```start``` script as root/admin*