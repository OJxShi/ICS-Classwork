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
warningFlash = 0
flashCount = 0
attackTimer = 10
playAttack = 0
attackX = random.randint(0,4)
immunityFrames = 0
score = 0

while hp > 0:
    # so the play doesn't get instantly killed by touching the beam
    if immunityFrames > 0:
        immunityFrames -= 1
    #this is awful
    if attackTimer > 0 and flashCount == 0 and playAttack == 0 and warningFlash == 0:
        attackX = random.randint(0,4)
    # countdown/delay before next attack
    if attackTimer > 0:
        attackTimer -= 1
    # warning for attack
    else:
        if flashCount < 20:
            if warningFlash < 8:
                warningFlash += 2
            elif warningFlash > 0:
                warningFlash -= 2
            flashCount += 1
        #resets
        if flashCount == 20:
            flashCount = 0
            warningFlash= 0
            playAttack = 9
            score += 1
            attackTimer = random.randint(15,35)
    #beam animation
    if playAttack > 0:
        playAttack -= 1
        if characterX == attackX and playAttack > 4 and immunityFrames == 0:
            hp -= 1
            immunityFrames = 5
    
    if button_a.was_pressed() and characterX != 0:
        characterX -= 1
    elif button_b.was_pressed() and characterX != 4:
        characterX += 1

    display.clear()
    #warning
    display.set_pixel(attackX, 0, warningFlash)
    #attack
    if playAttack > 0:
        display.set_pixel(attackX, 0, playAttack)
        display.set_pixel(attackX, 1, playAttack)
        display.set_pixel(attackX, 2, playAttack)
        display.set_pixel(attackX, 3, playAttack)
        display.set_pixel(attackX, 4, playAttack)
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
        

