import time
import thingspeak
import adafruit_dht
import RPi.GPIO as GPIO


channel_id = 1406926 
write_key = "J9HMAYLVZ96ZNRHW"
read_key = "Q2ZP3AP8KLNN0VAY"

GPIO.setmode(GPIO.BOARD) #toma las entrandas del GPIO segundo su ubicacion fisica
pinh = 21 #GPIO 22, sensor humedad suelo
pint = 4 #GPIO 4, senor dht11
sensor1 = adafruit_dht.DHT11(pint)
pink = 17 #GPIO 17, sensor ky 017
GPIO.setup(pinh, GPIO.OUT)
GPIO.setup(pink, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def dht11(channel):
  while True:
    try:
      humedad = sensor1.humidity
      temperatura = sensor1.temperature

      #escritura en la pagina
      response = channel.update({'field1': temperatura, 'field2': humedad})

      #lectura de lo escrito en la pagina
      read = channel.get({})
      print("Read:", read)

    except RuntimeError as error:
      print(error.args[0])
    

def medir_humedad(channel, pin):
  try:
        if GPIO.input(pinh):
          humedad = 1;
        else:
          humedad = 0;

        # escritura de la lectura del sensor en la pagina
        response = channel.update({'field2': humedad})
        
        # lectura de lo escrito en pagina
        read = channel.get({})
        print("Read:", read)
        
  except:
    print("connection failed")

GPIO.add_event_detect(pinh, GPIO.Both,callback= medir_humedad, bouncetime=15000 )

def ky_017(channel):

  if GPIO.input(pink):

    activo = 0; # Mientras el pulso de entrada sea alto(high), este mostrara que esta todo OK
  else:

    activo = 1;# Cuando el pulso de entrada sea bajo(low), este mostrara que se cayo

  response = channel.update({'field3': activo})

  read = channel.get({})
  print("Read:", read)
  
      
GPIO.add_event_detect(pink, GPIO.both, callback=ky_017, bouncetime=15000) # cuando se detecte el cambio de valor, este llamara a la funcion ky_017

    
if __name__ == "__main__":
  channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
  while True:
    dht11(channel)
    medir_humedad(channel)
    ky_017(channel)
    # cada 15 segundos se actualiza
    time.sleep(15)
