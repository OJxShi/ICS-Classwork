from microbit import *
import radio
radio.config(group=7)
radio.on()

#this is just for my computer... prob wont work on anyone else's
KEY_A = 1
KEY_B = 49
KEY_C = 95
KEY_D = 136
KEY_E = 542

frame_count = 0
blue_light = 0
red_light = 0
while True:
    #steering
    x_strength = accelerometer.get_x()
    x = round(x_strength/128,2)#rounded because the nromal results are large
    if x > 6: x = 6
    elif x < -6: x = -6#limits how far it can turn
    wheelTurnAngle = 90 + 90 * x / 10#converts to angle
    radio.send(str(wheelTurnAngle))#has to be a string to send
    #the message gets converted back on the receiving end
    
    value = pin0.read_analog() #taken from mr gallos code
    #https://github.com/MrGallo/microbit-tutorial/blob/main/adkeys-python.md
    
    frame_count += 1 #controls lights flashing
    if frame_count == 25:
        frame_count = 0
    print(frame_count)
    
    if value == KEY_A:
        red_light = 0
        #if on, turn off
        #if off, turn on
        if blue_light == 30:
            blue_light = 0
        else:
            blue_light = 30
       
    elif value == KEY_B:

        blue_light = 0
        if red_light == 30:
            red_light = 0
        else:
            red_light = 30
   
    if blue_light == 30 and frame_count >=12:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)

    if red_light == 30 and frame_count >=12:
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)

    
    sleep(30)
