from time import sleep
from gpiozero import LED


led = LED(18)

while True:
  led.on()
  sleep(1)
