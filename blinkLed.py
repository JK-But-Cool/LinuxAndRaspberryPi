#
from gpiozero import LED
import time

led = LED(3)
while True:
    led.off()
    print (led.value)
    time.sleep(1)
    led.on()
    print (led.value)
    time.sleep(1)

