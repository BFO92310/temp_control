import Adafruit_DHT
import GPi.GPIO as GPIO

GPIO.setwarnings(False)
sensor = Adafruit_DHT.DHT11
DHT11_pin = 12


humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
print(GPIO.input(DHT_pin))
if humidity is not None and temperature is not None:
  print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
elif humidity is not None and temperature is None:
  print('Pas de temperature and  Humidity={1:0.1f}%'.format(humidity))
elif humidity is None and temperature is not None:
  print('Temperature={0:0.1f}*C  No humidity'.format(temperature))
else:
  print('Failed to get reading from the sensor. Try again!')
