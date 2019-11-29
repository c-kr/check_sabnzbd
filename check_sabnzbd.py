#!/usr/bin/env python3

import argparse
import sys
import requests
from MonitoringPlugin import MonitoringPlugin

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--hostname', required=True, type=str, help='Hostaddress')
parser.add_argument('-a', '--apikey', required=True, type=str, help='API Key')
parser.add_argument('-u', '--url', type=str, help='URL', default="/sabnzbd/api")
parser.add_argument('-p', '--port',  type=str, help='Port', default=8080)

args = parser.parse_args()

host = args.hostname
port = args.port
url = args.url
apikey = args.apikey

np = MonitoringPlugin()

url = 'http://{}:{}{}'.format(host,port,url)
payload = {
          "output": "json",
           "apikey": apikey,
           "mode": "fullstatus",
          }

r = requests.get(url, params=payload)

status = r.json().get("status")

got_message = 0

for message in status.get("warnings"):
    got_message = 1
    if message["type"] == "WARNING":
        np.add_message(1,message["text"])
    elif message["type"] == "ERROR":
        np.add_message(2,message["text"])
    else:
        np.add_message(3,message["text"])

if got_message == 0:
    np.add_message(0,"no warnings")

rc,msg = np.check_messages()
print(msg)
sys.exit(rc)
