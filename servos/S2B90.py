#PCA9685 PWM servo/LED controller library.
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure servo pulse lengths
servo_0 = 150  # Min pulse length out of 4096
servo_90 = 360  # Mid pulse length out of 4096
servo_180 = 605  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0 to 90%, press Ctrl-C to quit...')
pwm.set_pwm(1, 0, servo_90)
exit()
