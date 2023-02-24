# Imports go at the top
from microbit import *
import random

# Code in a 'while True:' loop repeats forever
# while True:
#     display.show(Image.SMILE)
#     sleep(1000)
#     display.scroll('Hello')

direction = 0
# 0 right
# 1 down
# 2 left
# 3 up
characterX = 2
hp = 5
menu = True
selectMenu = True
hardMode = False

boxX = 1
boxY = 0
boxREAL = 9
boxTimer = 20

boxX2 = 1
boxY2 = 0
boxREAL2 = 9
boxTimer2 = 60

score = 0

#display.scroll("Select Difficulty")
display.show(Image("09990:"
                   "09990:"
                   "00000:"
                   "05550:"
                   "05550"))

while menu == True:
    if selectMenu == True:
        if button_a.was_pressed():
            if hardMode == False:
                display.scroll("Easy")
            elif hardMode == True:
                display.scroll("Hard")
            selectMenu = False
                
        elif button_b.was_pressed():
            if hardMode == False:
                hardMode = True
            elif hardMode == True:
                hardMode = False
    else:
        display.show(Image("09990:""90009:""00990:""00000:""00900"))
        if button_a.was_pressed():
            menu = False
        elif button_b.was_pressed():
            selectMenu = True
    
    display.clear()
    if selectMenu == True:
        if hardMode == False:
            display.show(Image("09990:"
                               "09990:"
                               "00000:"
                               "05550:"
                               "05550"))
        elif hardMode == True:
            display.show(Image("05550:"
                               "05550:"
                               "00000:"
                               "09990:"
                               "09990"))
            

while hp > 0 and menu == False:
    print(hp)
    if boxTimer > 0:
        boxTimer -= 1
        boxX = random.randint(0,4)
        boxREAL = 0
    elif boxY < 4:
        boxREAL = 9
        boxY += 0.2
    else:#if boxY == 4:
        boxREAL = 0
        boxTimer = 20
        boxY = 0
        score += 1
        if characterX == boxX:
            hp -= 1
    if hardMode == True:
        if boxTimer2 > 0:
            boxTimer2 -= 1
            boxX2 = random.randint(0,4)
            boxREAL2 = 0
        elif boxY2 < 4:
            boxREAL2 = 9
            boxY2 += 0.2
        else:#if boxY == 4:
            boxREAL2 = 0
            boxTimer2 = random.randint(15, 80)
            boxY2 = 0
            score += 1
            if characterX == boxX2:
                hp -= 1
    
    if button_a.was_pressed() and characterX != 0:
        characterX -= 1
    elif button_b.was_pressed() and characterX != 4:
        characterX += 1

    display.clear()
    display.set_pixel(boxX, round(boxY), boxREAL)
    if hardMode == True: display.set_pixel(boxX2, round(boxY2), boxREAL2)
    #character
    display.set_pixel(characterX, 4, hp + 4)
    sleep(33)

sleep(500)    
display.show(Image('99999:'
                   '99999:'
                   '99999:'
                   '99999:'
                   '99999'))
sleep(2000)
display.scroll("You lose!")
display.scroll(score)
        

