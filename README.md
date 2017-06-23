# Infoblox wrapper script

## Introduction
The goal of this is to have a simple script to be included in the command line we use to actually create hosts using Satellite 6.
It does not expose all options of the Infoblox API python module, but might be a nice start of the script.

## How to use
First, clone https://github.com/Infoblox-Development/Infoblox-API-Python

In the directory you are running this from, ensure you simply softlink to that repository. 

$ python call-to-infoblox.py -h
usage: call-to-infoblox.py [-h] [-u USERNAME] [-p PASSWORD] [-b INFOBLOXIP]
                           [-n HOSTNAME] [-i IPADDRESS] [-m MODE]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        name of user
  -p PASSWORD, --password PASSWORD
                        password
  -b INFOBLOXIP, --infobloxip INFOBLOXIP
                        ipadress of the infoblox device
  -n HOSTNAME, --hostname HOSTNAME
                        new hostname
  -i IPADDRESS, --ipaddress IPADDRESS
                        new ipaddress
  -m MODE, --mode MODE  mode: create or delete

## To do
* Check if object exists before trying to manipulate that.
* Add other modes.
* Various other bits.
