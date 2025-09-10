from l298n_dual_motor import L298NDualMotor
from line_follower_pid_dl import LineFollowerPID_dl
from servo_control import ServoControl 
import time

direct_line = True
turning = False
approach = False
testing_flower = False
move_back = False
back_turn = False

def main():
    # Define GPIO pins for the line sensors and motors
    sensor_pins = [5, 6, 13, 19, 26]  # Update with your actual sensor GPIO pins
    left_motor_pins = {'in1': 17, 'in2': 27, 'en': 22}
    right_motor_pins = {'in1': 23, 'in2': 24, 'en': 25}
    
    # Initialize the motor controller
    motor_controller = L298NDualMotor(left_motor_pins, right_motor_pins)
    
    # PID constants (tune these values based on your robot's performance)
    Kp_dl = 500
    Ki_dl = 0
    Kd_dl = 0.01
    
    # Initialize the line follower PID controller
    line_follower = LineFollowerPID_dl(sensor_pins, motor_controller, Kp_dl, Ki_dl, Kd_dl)
    
    servo_pin = 16  # Example GPIO pin, adjust based on your setup

    # Create an instance of the ServoControl class
    servo = ServoControl(servo_pin)

    
    try:
        while True:
              servo.set_angle(50)

              time.sleep(5)
              motor_controller.set_speed("right", 100)
              motor_controller.set_speed("left", 100)
              motor_controller.move_forward_both()
              time.sleep(6)
              # After line following, perform motor action
              motor_controller.move_forward("right")
              motor_controller.move_backward("left")
              print("Turning left")
              time.sleep(4.9)
              motor_controller.move_forward_both()
              time.sleep(2)
              line_follower.follow_line(base_speed=70)
              servo.move_slowly(50, 90, step=1, delay=0.1)
              time.sleep(2)
              servo.move_slowly(90, 50, step=1, delay=0.1)
              time.sleep(2)
              motor_controller.move_backward_both()
              time.sleep(9.5)
              motor_controller.move_forward("left")
              motor_controller.set_speed("left", 100)
              motor_controller.move_backward("right")
              motor_controller.set_speed("right", 100)
              time.sleep(5)
              print("Turning right")
              break

    except KeyboardInterrupt:
        print("Line following stopped by user.")
        motor_controller.cleanup()

if __name__ == "__main__":
    main()
