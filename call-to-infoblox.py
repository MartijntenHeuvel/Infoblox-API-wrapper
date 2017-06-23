#!/usr/bin/env python
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import argparse
sys.path.insert(0, 'Infoblox-API-Python/')
import infoblox

parser = argparse.ArgumentParser()

infobloxishere="192.168.0.1"

parser.add_argument('-u', '--username',
    help='name of user'
)
parser.add_argument('-p', '--password',
    help='password'
)
parser.add_argument('-b', '--infobloxip',
    help='ipadress of the infoblox device',
    default=infobloxishere
)

parser.add_argument('-n', '--hostname',
    help='new hostname'
)
parser.add_argument('-i', '--ipaddress',
    help='new ipaddress'
)
parser.add_argument('-m', '--mode', 
    help='mode: create or delete',
    default='create'
)

args = parser.parse_args()


iba_api = infoblox.Infoblox(args.infobloxip, args.username, args.password, '1.6', 'default', 'default')

if args.mode == 'create':
    print("Trying to create {host} with {ip}".format(
        host=args.hostname,
        ip=args.ipaddress)
    )
    call = iba_api.create_host_record(args.ipaddress, args.hostname)
    print call
else:
    print("trying to delete {host}".format(host=args.hostname))
    call = iba_api.delete_host_record(args.hostname)
    print call
