Plant monitor
=============

Stand-alone (optional aws logging) plant monitoring system built with raspberry pi module and some sensors.

## About

This project is about loging some enviroment data from sensors and monitoring plants growth.
Sensors are hooked up to raspberry pi module. Node-red process the sensors readings and can control LED plant light and water pump.

---

## Hardware

Raspberry Pi CM4


## Installation
Install [DietPi](https://dietpi.com) with other bits of software (instruction below), repositorium files should go to your user folder under .node-red/projects They can be git cloned in terminal or via node-red project interface.

### System
Install DietPi from [https://dietpi.com](https://dietpi.com)

All installation and configuration below is done in terminal remotly over SSH.
```bash
dietpi-update
```
other useful commands:
```bash
dietpi-update   : Run now to update DietPi from v8.25.1 to v9.1.1
dietpi-launcher : All the DietPi programs in one place
dietpi-config   : Feature rich configuration tool for your device
dietpi-software : Select optimised software for installation
htop            : Resource monitor
cpu             : Shows CPU information and stats
```
change ssh server to openssh
install: avahi for mDNS broadcasting
change hostname for easy ssh access to plant.local
- [ ] install ssh keys for quick and easy access


### Applications
1. Node-Red
install node-red with the 
```bash
dietpi-software
```

2. Install node-red nodes:
  * [node-red-node-pi-gpio](https://flows.nodered.org/node/node-red-node-pi-gpio) this is not installed by default

3. Git
```bash
dietpi-software
git config --global user.name 'your user name here'
git config --global user.email 'your email here'
```

enable node-red project git integration:
[https://nodered.org/docs/user-guide/projects/](https://nodered.org/docs/user-guide/projects/)

[DietPi Node-RED](https://dietpi.com/docs/software/hardware_projects/#__tabbed_6_3), all configs and data is stored in the following location:
/mnt/dietpi_userdata/node-red


## License
This project is licensed under [MIT license](http://opensource.org/licenses/mit-license.php)

