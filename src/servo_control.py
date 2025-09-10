import RPi.GPIO as GPIO
import time

class ServoControl:
    def __init__(self, servo_pin, frequency=50):
        """
        servo_pin: GPIO pin connected to the control wire of the servo
        frequency: PWM frequency (typically 50Hz for servos)
        """
        self.servo_pin = servo_pin
        self.frequency = frequency

        # Setup GPIO for servo control
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)

        # Initialize PWM on the servo pin
        self.pwm = GPIO.PWM(self.servo_pin, self.frequency)
        self.pwm.start(0)  # Initial duty cycle is 0 (servo off)

    def set_angle(self, angle):
        """
        Set the servo motor to a specific angle.
        angle: the desired angle between 0 and 180 degrees.
        """
        duty_cycle = self.angle_to_duty_cycle(angle)
        self.pwm.ChangeDutyCycle(duty_cycle)

    def angle_to_duty_cycle(self, angle):
        """
        Convert an angle to the corresponding PWM duty cycle.
        For most servos, 0° corresponds to a duty cycle of 2%, and 180° to about 12%.
        """
        return 2 + (angle / 18.0)  # Assuming 0° = 2% duty cycle, 180° = 12%

    def move_slowly(self, start_angle, end_angle, step=1, delay=0.05):
        """
        Move the servo slowly from start_angle to end_angle.
        start_angle: the starting angle.
        end_angle: the target angle.
        step: the increment in degrees for each step (default is 1°).
        delay: time delay between each step in seconds (default is 0.05 seconds).
        """
        if start_angle < end_angle:
            for angle in range(start_angle, end_angle + 1, step):
                self.set_angle(angle)
                time.sleep(delay)
        else:
            for angle in range(start_angle, end_angle - 1, -step):
                self.set_angle(angle)
                time.sleep(delay)

    def cleanup(self):
        """ Stop the PWM and clean up the GPIO. """
        self.pwm.stop()
        GPIO.cleanup()
