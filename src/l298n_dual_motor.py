# l298n_dual_motor.py

import RPi.GPIO as GPIO
import time

class L298NDualMotor:
    def __init__(self, left_pins, right_pins):
        """
        Initialize the motor control with specified GPIO pins.
        
        left_pins and right_pins should be dictionaries with keys:
        'in1', 'in2', 'en' (enable pin for PWM)
        """
        self.left_pins = left_pins
        self.right_pins = right_pins
        
        # Setup GPIO mode
        GPIO.setmode(GPIO.BCM)
        
        # Setup left motor pins
        GPIO.setup(self.left_pins['in1'], GPIO.OUT)
        GPIO.setup(self.left_pins['in2'], GPIO.OUT)
        GPIO.setup(self.left_pins['en'], GPIO.OUT)
        self.left_pwm = GPIO.PWM(self.left_pins['en'], 1000)
        self.left_pwm.start(0)
        
        # Setup right motor pins
        GPIO.setup(self.right_pins['in1'], GPIO.OUT)
        GPIO.setup(self.right_pins['in2'], GPIO.OUT)
        GPIO.setup(self.right_pins['en'], GPIO.OUT)
        self.right_pwm = GPIO.PWM(self.right_pins['en'], 1000)
        self.right_pwm.start(0)

    def set_speed(self, motor, speed):
        """ Set motor speed (0 to 100%). 'motor' can be 'left' or 'right'. """
        if motor == 'left':
            self.left_pwm.ChangeDutyCycle(speed)
        elif motor == 'right':
            self.right_pwm.ChangeDutyCycle(speed)
        else:
            raise ValueError("Motor must be 'left' or 'right'")

    def move_forward(self, motor):
        """ Move specified motor forward """
        if motor == 'left':
            GPIO.output(self.left_pins['in1'], GPIO.HIGH)
            GPIO.output(self.left_pins['in2'], GPIO.LOW)
        elif motor == 'right':
            GPIO.output(self.right_pins['in1'], GPIO.HIGH)
            GPIO.output(self.right_pins['in2'], GPIO.LOW)

    def move_backward(self, motor):
        """ Move specified motor backward """
        if motor == 'left':
            GPIO.output(self.left_pins['in1'], GPIO.LOW)
            GPIO.output(self.left_pins['in2'], GPIO.HIGH)
        elif motor == 'right':
            GPIO.output(self.right_pins['in1'], GPIO.LOW)
            GPIO.output(self.right_pins['in2'], GPIO.HIGH)

    def stop_motor(self, motor):
        GPIO.setmode(GPIO.BCM)
        """ Stop the specified motor """
        if motor == 'left':
            GPIO.output(self.left_pins['in1'], GPIO.LOW)
            GPIO.output(self.left_pins['in2'], GPIO.LOW)
        elif motor == 'right':
            GPIO.output(self.right_pins['in1'], GPIO.LOW)
            GPIO.output(self.right_pins['in2'], GPIO.LOW)

    def cleanup(self):
        """ Clean up GPIO settings """
        self.left_pwm.stop()
        self.right_pwm.stop()
        GPIO.cleanup()

    # Additional methods to control both motors together
    def move_forward_both(self):
        self.move_forward('left')
        self.move_forward('right')

    def move_backward_both(self):
        self.move_backward('left')
        self.move_backward('right')

    def stop_all(self):
        self.stop_motor('left')
        self.stop_motor('right')

    def set_speed_both(self, left_speed, right_speed):
        self.set_speed('left', left_speed)
        self.set_speed('right', right_speed)
