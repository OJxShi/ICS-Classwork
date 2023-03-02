# Imports go at the top
from microbit import *

def set_servo_angle(pin, angle):
    duty = 26 + (angle * 102) / 180
    pin.write_analog(duty)

wheelTurnAngle = 90
set_servo_angle(pin0, 90)
# Code in a 'while True:' loop repeats forever
while True:
    
    x_strength = accelerometer.get_x()
    x = round(x_strength/128,2)
    if x > 6: x = 6
    elif x < -6: x = -6

    wheelTurnAngle = 90 + 90 * x / 10
    
    print(wheelTurnAngle)
    display.clear()
    
    if button_b.was_pressed():
        break
    set_servo_angle(pin0, wheelTurnAngle)
    sleep(100)

    