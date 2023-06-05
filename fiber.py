import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()
pygame.font.init()

WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

gamemode = "main_menu"

title_font = pygame.font.SysFont('Comic Sans MS',100,False,True)
menu_font = pygame.font.SysFont('Arial', 40)
tutorial_font = pygame.font.SysFont('Arial', 25)
level_select_font = pygame.font.SysFont('Arial', 60)
pause_font = pygame.font.SysFont('Arial', 30)
pause_font_selected = pygame.font.SysFont('Arial', 30,True)
menu_options = [
    "LEVEL SELECT",
    "HOW TO PLAY",
    "SETTINGS",
    "QUIT"
]
tutorial_text = [
    "Use WASD keys to move",
    "When you move, you will continue to move until you hit a wall",
    "Collect as many yellow coins as you can!",
    "Try to collect stars too, I guess.",
    "Each coin gives 1 point, while stars give 5.",
    "(Press ESC to return)"
]
settings_sliders = [
    ["Camera movement",300,False],
    ["Speed",300,False]
]
pause_options = [
    "Resume",
    "How to Play",
    "Settings",
    "Exit to Main Menu"
]

levels_unlocked = 0

character_x = 3
character_y = 3
character_r = 255
character_g = 200
character_b = 0

movement_direction_x = 0
movement_direction_y = 0
distance_moved = 0
camera_x = 0
camera_y = 0
mouse_x = 0
mouse_y = 0
clicked = False
moving = False

points = 0
moves_used = 0
stars_collected = 0
current_level = 0
goal_x = 1
goal_y = 1
hit_a_wall = False
walls = []
coins = []
stars = []

coin_animation_timer = 0
coin_animation_switch = False
coin_colour = 0

previously_paused = False

#SETTINGS
camera_slam = 3
speed = 3

def walls_box(x1,y1,x2,y2):
    for i in range(x1,x2):
        walls.append([i,y1])
        walls.append([i,y2])
    for i in range(y1,y2):
        walls.append([x1,i])
        walls.append([x2,i])
    walls.append([x2,y2])
def walls_fill(x1,y1,x2,y2):
    for i in range(x1,x2+1):
       for k in range(y1,y2+1):
           walls.append([i,k])      
def walls_single(x,y):
    walls.append([x,y])

def coins_fill(x1,y1,x2,y2):
    for i in range(x1,x2+1):
       for k in range(y1,y2+1):
           coins.append([i,k])  
def coins_single(x,y):
    coins.append([x,y])

def add_star(x,y):
    global stars
    stars.append([x,y,True])
# i stopped working on this game for like two weeks and now i dont know how any of this works ;u;
def movement(direction):
    global movement_direction_x, movement_direction_y
    global moving, hit_a_wall, moves_used
    if direction == "left":
        movement_direction_x = -1
        movement_direction_y = 0
    elif direction == "right":
        movement_direction_x = 1
        movement_direction_y = 0
    elif direction == "up":
        movement_direction_x = 0
        movement_direction_y = -1
    elif direction == "down":
        movement_direction_x = 0
        movement_direction_y = 1
    moving = True
    hit_a_wall = False
    p = True
    for i in range(len(walls)):
        if character_x + movement_direction_x == walls[i][0] and character_y + movement_direction_y == walls[i][1]:
            p = False
    if p: moves_used += 1
def movement_check():
    global character_x, character_y, camera_x, camera_y, movement_direction_x, movement_direction_y
    global moving, points, stars_collected, hit_a_wall
    
    if hit_a_wall == False and moving:
        for i in range(len(walls)):
            if character_x + movement_direction_x == walls[i][0] and character_y + movement_direction_y == walls[i][1]:
                hit_a_wall = True
        if hit_a_wall == False:
            character_x += movement_direction_x
            character_y += movement_direction_y
            camera_x += movement_direction_x * camera_slam
            camera_y += movement_direction_y * camera_slam
        if hit_a_wall: 
            moving = False
    for i in range(len(coins)):
        if character_x == coins[i][0] and character_y == coins[i][1]:
            points += 1
            del coins[i]
            break
    for i in range(len(stars)):
        if character_x == stars[i][0] and character_y == stars[i][1] and stars[i][2]:
            points += 5
            stars_collected += 1
            stars[i][2] = False

def load_level(level):
    global character_x, character_y, goal_x, goal_y
    global walls, coins, stars, points, moves_used
    global coin_animation_timer, coin_animation_switch, coin_colour
    coin_animation_timer = 0
    coin_animation_switch = False
    coin_colour = 0
    points = 0
    moves_used = 0
    walls = []
    coins = []
    stars = []
    
    walls_box(0,0,int(WIDTH/50)-1,int(HEIGHT/50)-1)
    if level == 1:
        goal_x = 1
        goal_y = 1
        character_x = 7
        character_y = 2
        
        walls_fill(7,3,10,3)
        walls_fill(6,1,6,7)
        walls_single(12,1)
        walls_single(12,3)
        walls_single(7,4)
        walls_single(7,7)
#         walls_fill(11,7,12,8)
#         walls_fill(10,4,10,5)
        
        coins_fill(11,3,11,6)
    elif level == 2:
        goal_x = 12
        goal_y = 8
        character_x = 12
        character_y = 1
        
        walls_box(0,0,int(WIDTH/50)-1,int(HEIGHT/50)-1)
        walls_fill(10,4,12,4)
        walls_single(10,1)
        walls_fill(9,3,9,4)
        walls_single(1,1)
        walls_fill(1,4,7,4)
        
        coins_fill(1,2,9,2)
        coins_fill(10,2,10,3)
        coins_fill(11,1,11,3)
        coins_fill(12,2,12,3)
        
        add_star(9,1)
    else:
        goal_x = 12
        goal_y = 8
        character_x = 12
        character_y = 1
        
# ---------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if gamemode == "main_menu":
                    running = False
                elif gamemode == "level":
                    gamemode = "pause"
                elif gamemode == "pause":
                    gamemode = "level"
                elif gamemode == "tutorial" or gamemode == "settings": 
                    if previously_paused:
                        gamemode = "pause"
                    else:
                        gamemode = "main_menu"
                else: gamemode = "main_menu"
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            clicked = True
        elif event.type == MOUSEBUTTONUP:
            released = True
                        
    mouse_x, mouse_y = pygame.mouse.get_pos()    
    keys = pygame.key.get_pressed()
    
    if gamemode == "main_menu":
        previously_paused = False
        if clicked:
            for i in range(0,4):
                if mouse_x >= 100 and mouse_x <= 600 and mouse_y >= 250+i*65 and mouse_y <= 300+i*65:
                    if i == 0:
                        gamemode = "level_select"
                    elif i == 1:
                        gamemode = "tutorial"
                    elif i == 2:
                        gamemode = "settings"
                    elif i == 3:
                        running = False
    elif gamemode == "level_select":
        if clicked:
            level_clicked = False
            current_level = 0
            for k in range (0,3):
                    for i in range (0,5):
                        if level_clicked == False:
                            current_level += 1
                            if mouse_x >= 20+135*i and mouse_x <= 140+135*i and mouse_y >= 145+115*k and mouse_y <= 245+115*k:
                                load_level(current_level)
                                gamemode = "level"
                                level_clicked = True
    elif gamemode == "settings":
        for i in range(0,len(settings_sliders)):
            if clicked:
                if mouse_x >= 75+settings_sliders[i][1] and mouse_x <= 125+settings_sliders[0][1] and mouse_y >= 98+i*100 and mouse_y <= 127+i*100:
                    settings_sliders[i][2] = True
            if settings_sliders[i][2]:
                settings_sliders[i][0] = mouse_x-50
        if released:
            settings_sliders[0][2] = False
            settings_sliders[1][2] = False

    elif gamemode == "level":
        if moving == False:
            if keys[119] == True:  # w
                movement("up")
            if keys[97] == True:  # a
                movement("left")
            if keys[115] == True:  # s
                movement("down")
            if keys[100] == True:  # d
                movement("right")
                
            if character_x == goal_x and character_y == goal_y:
                gamemode = "level_complete"
        if coin_animation_timer < 70:
            coin_animation_timer += 1
        if coin_animation_timer < 60:
            if coin_animation_switch:
                coin_colour = 255- 255 * coin_animation_timer/60
            else:
                coin_colour = 255 * coin_animation_timer/60
        elif coin_animation_timer >= 60:
            if coin_animation_switch:
                coin_animation_switch = False
            else:
                coin_animation_switch = True
            coin_animation_timer = 0
        #3x speed! it looks bad and slow when its 1 block/frame  
        for i in range(0,int(speed)):
            movement_check()

        
        camera_x = camera_x * 0.75
        camera_y = camera_y * 0.75

    elif gamemode == "level_complete":
        if clicked:
            gamemode = "main_menu"
    elif gamemode == "pause":
        previously_paused = True
        if clicked and mouse_x > 5 and mouse_x < 280:
            if mouse_y > 100 and mouse_y < 30:
                gamemode = "level"
            elif mouse_y > 140 and mouse_y < 170:
                gamemode = "tutorial"
            elif mouse_y > 180 and mouse_y < 210:
                gamemode = "settings"
            elif mouse_y > 220 and mouse_y < 250:
                gamemode = "main_menu"
        
    camera_slam = settings_sliders[0][1]/100
    speed = settings_sliders[1][1]/100 + 1
    clicked = False
    released = False
#=======================================================#
    screen.fill((30,30,40))
    if gamemode == "main_menu":
        for i in range(0,4):
            if mouse_x >= 100 and mouse_x <= 600 and mouse_y >= 250+i*65 and mouse_y <= 300+i*65:
                pygame.draw.rect(screen,(200,200,200),(98,248+i*65,504,54))
            else:
                pygame.draw.rect(screen,(160,160,160),(100,250+i*65,500,50))
                
            menu_text = menu_font.render(menu_options[i], True, (255,255,255))
            screen.blit(menu_text,(100,255+i*65))
        title_text1 = title_font.render("Graphic deisgn",True,(255,255,255))
        title_text2 = title_font.render("is my passion",True,(255,255,255))
        screen.blit(title_text1,(0,0))
        screen.blit(title_text2,(0,110))
    elif gamemode == "tutorial":
        for i in range(len(tutorial_text)):
            tut_text = tutorial_font.render(tutorial_text[i],True,(255,255,255))
            screen.blit(tut_text,(10,40*i))
            
    elif gamemode == "level_select":
        j = 0
        for k in range (0,3):
            for i in range (0,5):
                if mouse_x >= 20+135*i and mouse_x <= 140+135*i and mouse_y >= 145+115*k and mouse_y <= 245+115*k:
                    pygame.draw.rect(screen,(200,200,200),(18+135*i,143+115*k,124,104))
                else:
                    pygame.draw.rect(screen,(160,160,160),(20+135*i,145+115*k,120,100))
                j += 1
                level_number_text = level_select_font.render(str(j), True, (0,0,0))
                screen.blit(level_number_text,(65+135*i-(len(str(j))-1)*18,160+115*k))
    
    elif gamemode == "settings":
        for i in range(0,len(settings_sliders)):
            settings_label = menu_font.render((settings_sliders[i][0] +": "+ str(camera_slam)), True, (255,255,255))
            pygame.draw.rect(screen,(100,100,100),(75,100+i*100,550,25))
            if settings_sliders[i][2]:
                pygame.draw.rect(screen,(200,200,200),(75+settings_sliders[i][1],98+i*100,50,29))
            else:
                pygame.draw.rect(screen,(160,160,160),(75+settings_sliders[i][1],98+i*100,50,29))
            screen.blit(settings_label,(50,50+i*100))
    
    elif gamemode == "level":
        pygame.draw.rect(screen,(255,255,255),(goal_x*50 + camera_x, goal_y*50 + camera_y,50,50))
        for i in range(len(coins)): #renders coins (obviously)
            pygame.draw.circle(screen,(255,255,coin_colour),(coins[i][0]*50+camera_x+25,coins[i][1]*50+camera_y+25),10)
        for i in range(len(walls)): #renders walls (duh)
            pygame.draw.rect(screen,(0,0,0),(walls[i][0]*50 + camera_x, walls[i][1]*50 + camera_y, 50, 50))
            pygame.draw.rect(screen,(60,60,85),(walls[i][0]*50+5 + camera_x, walls[i][1]*50+5 + camera_y,40,40))
        for i in range(len(stars)): #renders stars (who would've guessed
            if stars[i][2]:
                pygame.draw.circle(screen,(255,255,coin_colour),(stars[i][0]*50+camera_x+25,stars[i][1]*50+camera_y+25),20)
        pygame.draw.circle(screen, (character_r, character_g, character_b), (character_x*50+25 + camera_x, character_y*50+25 + camera_y), 25)
    
    elif gamemode == "pause":
        pygame.draw.rect(screen,(155,155,155),(goal_x*50 + camera_x, goal_y*50 + camera_y,50,50))
        for i in range(len(coins)):
            pygame.draw.circle(screen,(155,155,coin_colour*0.6),(coins[i][0]*50+camera_x+25,coins[i][1]*50+camera_y+25),10)
        for i in range(len(walls)):
            pygame.draw.rect(screen,(0,0,0),(walls[i][0]*50 + camera_x, walls[i][1]*50 + camera_y, 50, 50))
            pygame.draw.rect(screen,(36,36,51),(walls[i][0]*50+5 + camera_x, walls[i][1]*50+5 + camera_y,40,40))
        for i in range(len(stars)):
            if stars[i][2]:
                pygame.draw.circle(screen,(255,255,coin_colour*0.6),(stars[i][0]*50+camera_x+25,stars[i][1]*50+camera_y+25),20)

        pygame.draw.circle(screen, (character_r*0.6, character_g*0.6, character_b*0.6), (character_x*50+25 + camera_x, character_y*50+25 + camera_y), 25)
        
        pygame.draw.rect(screen,(0,0,0),(0,0,260,HEIGHT))
        pause_level = menu_font.render(("LEVEL " + str(current_level)),True,(255,255,255))
        screen.blit(pause_level,(5,5))
        points_text = pause_font_selected.render(("Points: "+ str(points)),True,(255,255,255))
        screen.blit(points_text,(5,60))
        for i in range(0, len(pause_options)):
            if mouse_x > 5 and mouse_x < 280 and mouse_y > i*40+100 and mouse_y < i*40+130:
                pause_text = pause_font_selected.render(pause_options[i], True, (255,255,255))
            else:
                pause_text = pause_font.render(pause_options[i], True, (200,200,200))
            screen.blit(pause_text,(5,i*40+100))
        
    
    elif gamemode == "level_complete":
        congration = level_select_font.render(("LEVEL " + str(current_level) + " COMPLETE"), True, (255,255,255))
        stats1 = menu_font.render("Points: "+str(points), True, (255,255,255))
        stats2 = menu_font.render("Stars collected: "+str(stars_collected)+"/"+str(len(stars)), True, (255,255,255))
        stats3 = menu_font.render("Moves used: "+str(moves_used), True, (255,255,255))
        click_anywhere = menu_font.render("Click anywhere to continue",True,(255,255,255))
        
        screen.blit(congration,(50,50))
        screen.blit(stats1,(100,150))
        screen.blit(stats2,(100,200))
        screen.blit(stats3,(100,250))
        screen.blit(click_anywhere,(100,350))
#=======================================================#
    pygame.display.flip()
    clock.tick(60)
#=======================================================#


pygame.quit()
