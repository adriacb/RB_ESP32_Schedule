# RB_ESP32_Schedule

Measuring electricity consumption with our ESP32 and our RaspberryPi. 

<p align="center">
  <img width="550" height="300" src="/images/Summ.PNG">
</p>


Basically we read data from our ESP32 through MQTT (Message Queue Telemetry Transport) protocol with the help of our RaspberryPi. We use VCN viewer to connect to our RaspberryPi and to control Node-Red server. In this way we can read data using Node-Red and push it into our DDBB with the help of Python libraries.


## Requirements

- VNC Viewer (Local PC)
- VCN Server (RB)
- Node-Red (RB)
- Python (RB)
    - Pandas
    - schedule
    - colorama
    - pymysql
    - sqlalchemy
- MySQL (DDBB)


