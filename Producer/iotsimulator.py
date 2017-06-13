#!/usr/bin/python

import sys
import datetime
import random
import string

# Set number of simulated messages to generate
if len(sys.argv) > 1:
  numMsgs = int(sys.argv[1])
else:
  numMsgs = 1

# Fixed values
guidStr = "0-ZZZ12345678"
destinationStr = "0-AAA12345678"
formatStr = "urn:harvesting:sensors:weather_farm_conditions"

# Choice for random letter
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

iotmsg_header = """\
{
  "guid": "%s",
  "destination": "%s", """

iotmsg_eventTime = """\
  "eventTime": "%sZ", """

iotmsg_payload ="""\
  "payload": {
     "format": "%s", """

iotmsg_data ="""\
      {
       "temperature": %.1f,
       "soil_temperature": %.1f,
       "humidity": %d,
       "wind_speed": %d,
       "rain_fall": %.1f
     }
"""

##### Generate JSON output:

print "["

dataElementDelimiter = ","
for counter in range(0, numMsgs):

  randInt = random.randrange(0, 9)
  randLetter = random.choice(letters)

  today = datetime.datetime.today()
  datestr = today.isoformat()

  # Generate a random floating point number
  randTemp1 = random.uniform(0.0, 40.0) + 60.0
  randTemp2 = random.uniform(0.0, 20.0) + 20.0
  randTemp3 = random.uniform(0, 100)
  randTemp4 = random.uniform(0, 130)
  randTemp5 = random.uniform(0.0, 12.0)
  if counter == numMsgs - 1:
    dataElementDelimiter = ""
  print iotmsg_data % (randTemp1,randTemp2,randTemp3,randTemp4,randTemp5)+ dataElementDelimiter 
print "]"
