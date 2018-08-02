import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 100)
add_angle = 5
def move_servo(angle, delay):
	pwm.start(5)
	chosen_angle = float(angle)/10 + add_angle
	pwm.ChangeDutyCycle(chosen_angle)
	time.sleep(delay)
