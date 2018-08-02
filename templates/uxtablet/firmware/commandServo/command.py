import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 100)
add_angle = 5

def move_servo(angle, delay):
        chosen_angle = float(angle)/10 + add_angle
        pwm.ChangeDutyCycle(chosen_angle)
        time.sleep(delay)

def throw_waste():
        pwm.start(5)
        # Throw
        move_servo(170, 1)
        move_servo(0, 0.5)

        # Clean electronics
        pwm.stop()
