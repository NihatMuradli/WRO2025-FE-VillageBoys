import RPi.GPIO as GPIO
from condition_sensor import line_sensor 
import time

SENSOR_PIN = 20 

my_sensor = line_sensor(SENSOR_PIN)

class LineFollowerPID_dl:
    def __init__(self, sensor_pins, motor_controller, Kp, Ki, Kd):
        self.sensor_pins = sensor_pins
        self.motor_controller = motor_controller
        self.Kp_dl = Kp
        self.Ki_dl = Ki
        self.Kd_dl = Kd

        GPIO.setmode(GPIO.BCM)
        for pin in self.sensor_pins:
            GPIO.setup(pin, GPIO.IN)
        
        self.previous_error = 0
        self.integral = 0
    
    def read_sensors(self):
        """Read the values from the 5 sensors (1 for black, 0 for white)."""
        return [GPIO.input(pin) for pin in self.sensor_pins]
    
    def calculate_error(self, sensor_values):
        """
        Calculate the error based on the sensor readings.
        Weights are adjusted assuming the line is 2 cm wide.
        """
        # Error weights assuming 2 cm per sensor coverage, centered on 0
        weights = [-2, -1, 0, 1, 2]

        # Error calculation: weighted sum of sensor values (1=black, 0=white)
        error = sum([weights[i] * sensor_values[i] for i in range(5)])

        # Normalize the error, so that maximum deviation from center is considered
        if sum(sensor_values) == 0:
            # If no sensor detects the line, keep the previous error (could be off track)
            error = self.previous_error
        else:
            error = error / sum(sensor_values)  # Normalize by the number of active sensors
        
        return error
    
    def pid_control(self, error, dt):
        """PID control logic for adjusting motor speeds."""
        P = error
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        self.previous_error = error
        output = (self.Kp_dl * P) + (self.Ki_dl * self.integral) + (self.Kd_dl * derivative)
        return output
    
    def follow_line(self, base_speed=80):
        """Main loop for line following."""
        try:
            while True:
                start_time = time.time()
                sensor_values = self.read_sensors()
                error = self.calculate_error(sensor_values)
                dt = time.time() - start_time
                adjustment = self.pid_control(error, dt)
                
                # Motor speed adjustments
                left_speed = base_speed - adjustment
                right_speed = base_speed + adjustment
                left_speed = max(0, min(100, left_speed))
                right_speed = max(0, min(100, right_speed))
                
                # Set the motor speeds
                self.motor_controller.set_speed('left', left_speed)
                self.motor_controller.set_speed('right', right_speed)
                
                self.motor_controller.move_forward_both()
                
                time.sleep(0.1)
                
                # Check the single sensor
                sensor_value = my_sensor.read_line_sensor()
                
                if sensor_value == 0:
                    print("Black line detected by single sensor. Stopping the robot.")
                    self.motor_controller.stop_all()
                    break  # Stop following the line and break out of the loop

        except KeyboardInterrupt:
            self.motor_controller.stop_all()
            GPIO.cleanup()
