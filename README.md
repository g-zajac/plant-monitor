Plant monitor
=============

Stand-alone (optional aws logging) plant monitoring system built with raspberry pi, camera and some sensors.

## About

This project is about loging some enviroment data from sensors and monitoring a plant growth.
Sensors and camera are hooked up to raspberry pi. Node-red process the sensors readings and store them to influxdb.
For data visualisation Grafana is used.
The data is also send to aws with MQTT and pictures to S3 bucket.

---

## Hardware

Raspberry Pi Zero W (can be any other) plus:
- camera with 120deg lens
- TSL2561 digital luminosity light sesor
- BMP280 Pressure/temperature Sensors
- HC-SR04 ultrasonic distance sensor for water level
- Capacitive Soli Moisture Sensor
- ADS1015 AD converter for analog sensors
- CSS811 air quality sensor
- OLED display


## Installation
Install Raspbian with other bits of software (instruction below), repositorium files should go to your user folder under .node-red/projects They can be git cloned in terminal or via node-red project interface.

### System
Install minimal Raspbian from [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/)
*(create an empty ssh file on card in /boot folder for ssh access)*

All installation and configuration below is done in terminal remotly over SSH.
```bash
sudo apt-get update && sudo apt-get upgrade
```

```bash
sudo raspi-config
```
enable interfaces I2C, camera etc and
change hostname for easy ssh access


### Applications
1. Node-Red
Install node-red with script from: [https://nodered.org/docs/getting-started/raspberrypi](https://nodered.org/docs/getting-started/raspberrypi)
```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```
  Install node-red nodes:
  * [node-red-contrib-bme280](https://flows.nodered.org/node/node-red-contrib-bme280)
  * [node-red-contrib-camerapi](https://flows.nodered.org/node/node-red-contrib-camerapi) (*enable in raspi-conf and check for installed picamera module!*)
  * [node-red-contrib-influxdb](https://flows.nodered.org/node/node-red-contrib-influxdb)
  * [node-red-contrib-os](https://flows.nodered.org/node/node-red-contrib-os)
  * [node-red-contrib-pcf8574-lcd](https://flows.nodered.org/node/node-red-contrib-pcf8574-lcd)
  * [node-red-contrib-pythonshell](https://flows.nodered.org/node/node-red-contrib-pythonshell)


2. Install PM2
```bash
npm install pm2 -g
```
```bash
pm2 start node-red
```
for autostart
```bash
pm2 save
pm2 startup
```

3. Git
```bash
sudo apt-get install git
git config --global user.name 'your user name here'
git config --global user.email 'your email here'
```
enable node-red project git integration:
[https://nodered.org/docs/user-guide/projects/](https://nodered.org/docs/user-guide/projects/)

4. Influx database and Grafana
```bash
curl -sL https://packages.grafana.com/gpg.key | sudo apt-key add -
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install -y grafana influxdb
sudo systemctl enable influxdb grafana-server
sudo systemctl start influxdb grafana-server
```
run influx
```bash
influx
```
```sql
CREATE DATABASE plantdb
```
autostart
```bash
sudo systemctl enable grafana-server.service
```
Open grafana web interface   yourhostname.localhost:3000

6. Other bits
* Python package for TSL2561 script
```bash
sudo apt-get install python-pip
sudo apt install python-smbus
```

## License
This project is licensed under [MIT license](http://opensource.org/licenses/mit-license.php)

## Project status
- prototype built, under testing
- node-red flow under development
