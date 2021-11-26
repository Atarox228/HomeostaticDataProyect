import httplib, urllib  
import time  
import Adafruit_DHT  
sleep = 30 # how many seconds to sleep between posts to the channel  
key = 'J9HMAYLVZ96ZNRHW'  # Write API key 
  
humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)  
  
  
#Report Raspberry Pi internal temperature to Thingspeak Channel  
def thermometer():  
    while True:        
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}  
        conn = httplib.HTTPConnection("api.thingspeak.com:80")  
        try:  
            humidity, temperature = Adafruit_DHT.read_retry(11, 27)
            params = urllib.urlencode({'field1': temperature, 'key':key }) # channel name is field1 or field 2
            conn.request("POST", "/update", params, headers)  
            response = conn.getresponse()  
            print (temperature)  
            print (humidity)
            #print response.status, response.reason  
            data = response.read()  
            conn.close()  
            humidity, temperature = ""
        except:  
            print ("connection failed")  
        break  
#sleep for desired amount of time  
if __name__ == "__main__":  
        while True:  
                thermometer()  
                time.sleep(sleep)
