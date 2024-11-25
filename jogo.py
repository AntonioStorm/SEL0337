import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)



def button(pin):
	#if GPIO.input(17):
		print('Jogador 1 ganhou')
	#else  GPIO.input(27):
		#print('Jogador 2 ganhou')
def buttao(trem):
	print('Jogador 2 ganhou')



GPIO.add_event_detect(17,GPIO.BOTH,callback = button, bouncetime = 200)

GPIO.add_event_detect(27,GPIO.BOTH,callback = buttao, bouncetime = 200)



try:

	while True:
		pass
except KeyboardInterrupt:

 GPIO.cleanup
