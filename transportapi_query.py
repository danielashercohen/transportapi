#!/usr/bin/python3

import config
import requests
import json

url = ("https://transportapi.com"
       "/v3/uk/train/station/SAC/live.json?app_id=%s"
       "&app_key=%s"
       "&calling_at=hpd"
       "&darwin=false"
       "&train_status=passenger"
       % (config.app_id, config.app_key))
response = json.loads(requests.get(url).text)

# print (response['departures'])
for departure in response['departures']['all']:
  if departure['expected_departure_time'] != None:
    print (departure['expected_departure_time'] + ' ' + departure['platform'] )
