import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setwarnings(False)  # Disable warnings

# Define the GPIO pin connected to the servo
servo_pin = 18  # GPIO18 (Pin 12)

# Set up the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM instance with frequency of 50Hz
pwm = GPIO.PWM(servo_pin, 50)

# Function to set servo angle (0 to 180 degrees)
def set_angle(angle):
    # Convert angle to duty cycle (0 degrees = 2.5%, 180 degrees = 12.5%)
    duty = angle / 18 + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Give the servo time to reach the position

# Start PWM with 0 duty cycle
pwm.start(0)

try:
    while True:
        # Example movement pattern
        print("Moving to 0 degrees")
        set_angle(0)
        time.sleep(1)
        
        print("Moving to 90 degrees")
        set_angle(90)
        time.sleep(1)
        
        print("Moving to 180 degrees")
        set_angle(180)
        time.sleep(1)
        
        # Sweep from 0 to 180 degrees
        print("Sweeping from 0 to 180 degrees")
        for angle in range(0, 181, 10):
            set_angle(angle)
            print(f"Current angle: {angle} degrees")
        
        # Sweep from 180 to 0 degrees
        print("Sweeping from 180 to 0 degrees")
        for angle in range(180, -1, -10):
            set_angle(angle)
            print(f"Current angle: {angle} degrees")
        
        # Ask user if they want to continue
        user_input = input("Press Enter to continue or type 'q' to quit: ")
        if user_input.lower() == 'q':
            break

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    # Clean up
    pwm.stop()
    GPIO.cleanup()
    print("GPIO cleanup completed")