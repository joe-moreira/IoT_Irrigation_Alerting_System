# IoT_Irrigation_Alerting_System
Real-time monitoring in a rural area to control irrigation.

Main goal: define more efficient irrigation systems that meet crops water requirements.
The data is collected in real-time by the sensors.

Data pipelining:
PRODUCER:
1.	Process starts when data is manually generated using the IoT simulator code (iotsimulator.py script)
2.	Having modified the script in order to generate the following variables in JSON format:
 temperature
 soil_temperature
 humidity
 wind_speed
 rain_fall

3.	Executed the script in order to generate 100 documents. The weather_farm_conditions.log file was created for better analysis. JSON format compliance was validated on JSONLint website
A brief output follows:

https://user-images.githubusercontent.com/17622709/27093962-689bf334-501d-11e7-83a2-a23e85c37716.png
