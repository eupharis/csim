#!/usr/bin/env python3
""" download and parse telemetry for CSIM from the satnogs API
"""

import os
import json
import requests
from csim import Csim

API_KEY = os.environ.get('SATNOGS_API_KEY')
API_URL = 'http://db.satnogs.org/api/'
CSIM_ID = '43793'


def download_telemetry_to_file(filename):
    url = API_URL + 'telemetry/?satellite=' + CSIM_ID
    headers = {'Authorization': 'Token ' + API_KEY}

    content = []
    for _ in range(0, 10):
        print('getting ', url)
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        content.extend(resp.json())
        url = resp.links['next']['url']

    with open('tlm.json', 'w') as f:
        f.write(json.dumps(content))


def parse_telemetry_from_file(filename):
    content = None
    with open('tlm.json', 'r') as f:
        content = json.loads(f.read())

    frame = None
    for tlm in content:
        frame = bytearray.fromhex(tlm['frame'])
        parsed = Csim.from_bytes(frame)
        info = parsed.ax25_frame.payload.ax25_info
        if isinstance(info, Csim.BeaconLong):
            rpm3 = info.filtered_speed_rpm3
            print(tlm['timestamp'], ': ', rpm3)
        else:
            print('Skipping ', info.__class__.__name__)


if __name__ == '__main__':
    #download_telemetry_to_file('tlm.json')
    parse_telemetry_from_file('tlm.json')
