# Imports go at the top
from microbit import *
import random
import math

currentMode = "world"
#character info
charWorldX = 2
charWorldY = 4
hp = 10
facing = 0 #0 up 1 right 2 down 3 left
damage = 1
damageMultiplier = 1
heal = 3
#enemy info
enemyWorldX = 1
enemyWorldY = 1
enemyHP = 3
enemyAttack = 1

#totally random generated enemies trust me the spawns are uhh not preset trust me bro
enemyCount = -1
enemySpawnX    = [3,  2  ,0,3, 1,2]
enemySpawnY    = [4,  2  ,1,3, 4,2]
newEnemyHP     = [5,  7  ,3,10,8,15]
newEnemyAttack = [1.5,0.5,3,2, 3,5]

#battle
battleflash = 0
whogotattacked = "idk"
whoseturn = "you"
characterBattleFlash = 9
enemyBattleFlash = 9
attackBarX = 4

#currentMode = "inventory"
invPage = 0
invPageIcon = [Image.HEART,Image("97000:""79709:""07995:""00990:""09509"),Image("05950:""55955:""99999:""55955:""05950"), Image.NO]

while hp > 0 and enemyCount < len(enemySpawnX) - 1:
    #world mode
    if currentMode == "world":
        if button_a.was_pressed():
            if facing == 0 and charWorldY !=0:#First checks if the move won't put you out of bounds
                #Then checks to see if enemy is in front
                if charWorldX == enemyWorldX and charWorldY - 1 == enemyWorldY:
                    currentMode = "battle"
                else: #if there's nothing move forward
                    charWorldY -= 1
            if facing == 1 and charWorldX !=4:
                if charWorldX + 1 == enemyWorldX and charWorldY == enemyWorldY:
                    currentMode = "battle"
                else:
                    charWorldX += 1
            if facing == 2 and charWorldY !=4:
                if charWorldX == enemyWorldX and charWorldY + 1 == enemyWorldY:
                    currentMode = "battle"
                else:
                    charWorldY += 1
            if facing == 3 and charWorldX !=0:
                if charWorldX - 1 == enemyWorldX and charWorldY == enemyWorldY:
                    currentMode = "battle"
                else:
                    charWorldX -= 1
        if button_b.was_pressed():
            if facing != 3: facing += 1
            else: facing = 0
        
    #battle mode
    if currentMode == "battle":
        if enemyHP <= 0 and battleflash == 0: #Upon winning
            sleep(500)
            display.scroll("VICTORY", delay = 75)
            itemDrop = random.randint(0,5)
            if itemDrop > 2:
                damageMultiplier += 0.5
            elif itemDrop == 2:
                damageMultiplier += 2
            elif itemDrop == 3 or itemDrop == 4:
                heal += 3
            elif itemDrop == 5:
                heal += 5
            enemyCount += 1
            battleflash = 0
            whoseturn = "you" #prevents enemy from attacking beyond the grave
            #New enemy spawns
            enemyWorldX = enemySpawnX[enemyCount]
            enemyWorldY = enemySpawnY[enemyCount]
            enemyHP = newEnemyHP[enemyCount]
            enemyAttack = newEnemyAttack [enemyCount]
            currentMode = "world"
        if hp <= 0:
            sleep(500)
            display.scroll("YOU DIED", delay = 75)
            break
        if battleflash > 0:
            battleflash -= 1
            if whogotattacked == "enemy":
                if enemyBattleFlash == 9:
                    enemyBattleFlash -= 3
                elif enemyBattleFlash == 6: enemyBattleFlash += 3
            if whogotattacked == "you":
                if characterBattleFlash == 9:
                    characterBattleFlash -= 3
                elif characterBattleFlash == 6: characterBattleFlash += 3
        elif whoseturn == "you":
            if button_a.was_pressed():
                attackBarX = 4
                currentMode = "attack"
                whoseturn = "enemy"
            elif button_b.was_pressed():
                invPage = 0
                currentMode = "inventory"
        elif whoseturn == "enemy":
            whogotattacked = "you"
            battleflash = 10
            whoseturn = "you"
            hp -= enemyAttack
            sleep(500)
            display.scroll(enemyAttack, delay = 75, wait = True)
            sleep(500)
            
    #attack mode
    if currentMode == "attack":
        if attackBarX > 0:
            attackBarX -= 0.2
            if button_a.was_pressed():
                damage = round((3 - math.sqrt((attackBarX - 1)**2)) / 3,1)*damageMultiplier
                enemyHP -= damage
                whogotattacked = "enemy"
                whoseturn = "enemy"
                battleflash = 10
                
                sleep(500)
                display.scroll(damage, delay = 75, wait = True)
                currentMode = "battle"
                
        elif attackBarX <= 0:
            sleep(200)
            display.scroll("MISS", delay = 75)
            currentMode = "battle"
            
    #inventory/menu mode
    if currentMode == "inventory":
        if button_a.was_pressed(): 
            if invPage == 0:
                display.scroll(hp, delay = 75)     
            elif invPage == 1:
                display.scroll(damageMultiplier, delay = 75)      
            elif invPage == 2:
                if heal > 0:
                    heal -= 1
                    hp += 3
                else: 
                    display.show(Image.NO)
                    sleep (500)
                display.scroll(str(heal)+" left", delay = 75)
            currentMode = "battle"
        elif button_b.was_pressed():
            if invPage >= len(invPageIcon) - 1:
                invPage = 0
            else: invPage += 1
    
    #rendering
    display.clear()
    if currentMode == "world":
        #character
        display.set_pixel(charWorldX, charWorldY, 9)
        #pointer telling you which way you're facing
        if facing == 0 and charWorldY !=0:
            display.set_pixel(charWorldX, charWorldY - 1, 5)
        if facing == 1 and charWorldX !=4:
            display.set_pixel(charWorldX + 1, charWorldY, 5)
        if facing == 2 and charWorldY !=4:
            display.set_pixel(charWorldX, charWorldY + 1, 5)
        if facing == 3 and charWorldX !=0:
            display.set_pixel(charWorldX - 1, charWorldY, 5)
        #enemy
        display.set_pixel(enemyWorldX, enemyWorldY, 9)
    if currentMode == "battle":
        #character sprite
        display.set_pixel(0,2, characterBattleFlash)
        display.set_pixel(1,2, characterBattleFlash)
        display.set_pixel(0,3, characterBattleFlash)
        display.set_pixel(1,3, characterBattleFlash)
        display.set_pixel(0,4, characterBattleFlash)
        display.set_pixel(1,4, characterBattleFlash)
        display.set_pixel(2,4, characterBattleFlash)
        #enemy sprite
        display.set_pixel(3,0, enemyBattleFlash)
        display.set_pixel(4,0, enemyBattleFlash)
        display.set_pixel(3,1, enemyBattleFlash)
        display.set_pixel(4,1, enemyBattleFlash)
        display.set_pixel(3,2, enemyBattleFlash)
        display.set_pixel(4,2, enemyBattleFlash)
    if currentMode == "attack":
        display.show(Image("99999:""06000:""06000:""06000:""99999"))
        display.set_pixel(round(attackBarX),1,9)
        display.set_pixel(round(attackBarX),2,9)
        display.set_pixel(round(attackBarX),3,9)
    if currentMode == "inventory":
        display.show(invPageIcon[invPage])
    
    sleep(33)

if enemyCount >= len(enemySpawnX) - 1:
    display.clear()
    display.scroll("ALL ENEMIES BEAT!")
    while True:
        display.show(Image.HAPPY)
while hp <= 0:
    display.show(Image.SAD)
