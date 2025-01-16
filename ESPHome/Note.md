# ESPHome with ESP8266 
**Schematic:** 
1. D3 - LED
2. D5 - IR transmitter
3. D7 - IR receiver
- esp-ir.yaml  
ESP8266 transmit command via IR transmitter, and receive data from IR receiver.  
If the received data is the same as the transmitted data, change the LED status.
- capture-transmit-ir.yaml  
Read IR codes and retransmit IR codes (raw)
- IR-control-air-conditioner.yaml  
Using the button on the UI to send a command to the device/air conditioner
- climate-control-ac.yaml  
Use "climate" component to control AC (Air Conditioner) via IR 
