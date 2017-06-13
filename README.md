# IoT_Irrigation_Alerting_System
Real-time monitoring in a rural area to control irrigation.

Main goal: define more efficient irrigation systems that meet crops water requirements.
The data is collected in real-time by the sensors:

https://user-images.githubusercontent.com/17622709/27093991-845a41ac-501d-11e7-904b-d62a501286b5.png

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

4.	The script execution consists on generating data and injecting it into a Kafka producer broker using a defined topic (here iotmsgs).
This is the entire execution commands:
/home/ec2-user/iotsimulator.py 10 | /home/ec2-user/kafka_2.11-0.10.1.0/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic iotmsgs

CONSUMER:

5.	The Kafka’s message originated at previous stage it’s here analyzed by Apache Spark for analytics process. To do so, we need the Python script required by Spark for direct streaming processing (kafka-direct-iotmsg.py). 
The original script was modified in order to be able to analyzing the incoming data brought by Kafka publishing system and trigger some alerts in case of reaching low levels of water.
The script analyses three values: temperature, soil temperature and humidity and an “Alert” message is displayed in case of need. 

The commands execution follows:
spark-submit --jars /home/ec2-user/spark-streaming-kafka-0-8-assembly_2.11-2.0.0-preview.jar /home/ec2-user/kafka-direct-iotmsg.py localhost:9092 iotmsgs

It’s important to highlight the need for using the same topic name between Producer-Consumer and the correct Kafka port (9092) for the process. 

Below is General data pipeline and process: 

https://user-images.githubusercontent.com/17622709/27093980-77e416f0-501d-11e7-804d-06f576125530.png

CONCLUSION:

On this Final Project we covered all data process from its proper generation, passing through a log messaging system and finally the later analysis and triggering actions according to the values received. All these process could have been implemented via Internet or any other medium.
