import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

DHT11_pin = 12
GPIO.setup(DHT11_pin, GPIO.IN)

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT11_pin)
print(GPIO.input(DHT11_pin))
if humidity is not None and temperature is not None:
  print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
elif humidity is not None and temperature is None:
  print('Pas de temperature and  Humidity={1:0.1f}%'.format(humidity))
elif humidity is None and temperature is not None:
  print('Temperature={0:0.1f}*C  No humidity'.format(temperature))
else:
  print('Failed to get reading from the sensor. Try again!')
