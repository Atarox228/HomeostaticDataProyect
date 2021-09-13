#https://tutorials-raspberrypi.com/log-raspberry-pi-sensor-data-with-thingspeak-and-analyze-it/
import thingspeak
import time
import Adafruit_DHT
 
channel_id = 1406926  # PUT CHANNEL ID HERE
write_key  = 'J9HMAYLVZ96ZNRHW' # PUT YOUR WRITE KEY HERE
read_key   = 'Q2ZP3AP8KLNN0VAY' # PUT YOUR READ KEY HERE
pin = 4
sensor = Adafruit_DHT.DHT22
 
def measure(channel):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # write
        response = channel.update({'field1': temperature, 'field2': humidity})
        
        # read
        read = channel.get({})
        print("Read:", read)
        
    except:
        print("connection failed")
 
 
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)
