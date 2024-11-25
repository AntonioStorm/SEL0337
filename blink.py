import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.OUT)

while True:
	gpio.output(10, True)
	time.sleep(1)
	gpio.output(10, False)
	time.sleep(1)
