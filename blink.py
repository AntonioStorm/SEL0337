#Importações das bibliotecas
import time  
import RPi.GPIO as gpio
#Seta os pinos como numeração na placa e utiliza o pino 10
gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.OUT)
#Código de piscar o LED que estará ligado no pino 10
while True:
	gpio.output(10, True)
	time.sleep(1)
	gpio.output(10, False)
	time.sleep(1)
