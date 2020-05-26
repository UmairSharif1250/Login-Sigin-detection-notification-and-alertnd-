import RPI.GPIO as GPIO
import  time

buzzer_pin= 12

GPIO.setmode(GPIO.BOARD)
GPIO.SETUP(buzzer_pin ,GPIO.OUT )

#MAKE BUZZER SOUND
GPIO.output(buzzer_pin ,GPIO.HIGH)
time.sleep(0.5)

#stop buzzer sound

GPIO.output(buzzer_pin ,GPIO.LOW)

GPIO.cleanup