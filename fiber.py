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
    "(Press ESC to exit to the menu)"
]
settings_sliders = [
    ["Camera movement",300,False]
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

#SETTINGS
camera_slam = 3

def simple_box(x1,y1,x2,y2):
    for i in range(x1,x2):
        walls.append([i,y1])
        walls.append([i,y2])
    for i in range(y1,y2):
        walls.append([x1,i])
        walls.append([x2,i])
    walls.append([x2,y2])
def simple_fill(x1,y1,x2,y2):
    for i in range(x1,x2+1):
       for k in range(y1,y2+1):
           walls.append([i,k])      
def single_wall(x,y):
    walls.append([x,y])

def simple_fill_coins(x1,y1,x2,y2):
    for i in range(x1,x2+1):
       for k in range(y1,y2+1):
           coins.append([i,k])  
def single_coin(x,y):
    coins.append([x,y])

def add_star(x,y):
    global stars
    stars.append([x,y,True])

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
    global walls, coins, points, moves_used
    points = 0
    moves_used = 0
    walls = []
    coins = []
    
    if level == 1:
        goal_x = 12
        goal_y = 8
        character_x = 12
        character_y = 1
        
        simple_box(0,0,int(WIDTH/50)-1,int(HEIGHT/50)-1)
        simple_fill(10,4,12,4)
        single_wall(10,1)
        simple_fill(9,3,9,4)
        single_wall(1,1)
        simple_fill(1,4,7,4)
        
        simple_fill_coins(1,2,9,2)
        simple_fill_coins(10,2,10,3)
        simple_fill_coins(11,1,11,3)
        simple_fill_coins(12,2,12,3)
        
        add_star(9,1)
    else:
        goal_x = 12
        goal_y = 8
        character_x = 12
        character_y = 1
        
        simple_box(0,0,int(WIDTH/50)-1,int(HEIGHT/50)-1)
# ---------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if gamemode == "main_menu":
                    running = False
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
        if clicked:
            for i in range(0,3):
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
        if clicked:
            if mouse_x >= 75+settings_sliders[0][1] and mouse_x <= 125+settings_sliders[0][1] and mouse_y >= 98 and mouse_y <= 127:
                settings_sliders[0][2] = True
        elif released and settings_sliders[0][2]:
            settings_sliders[0][2] = False
        
        if settings_sliders[0][2]:
            settings_sliders[0][1] = (mouse_x-100)
            
        if settings_sliders[0][1] < 0:
            settings_sliders[0][1] = 0
        elif settings_sliders[0][1] > 500:
            settings_sliders[0][1] = 500
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
        
        #3x speed! it looks bad and slow when its 1 block/frame  
        movement_check()
        movement_check()
        movement_check()
        
        camera_x = camera_x * 0.8
        camera_y = camera_y * 0.8

    elif gamemode == "level_complete":
        if clicked:
            gamemode = "main_menu"
    camera_slam = settings_sliders[0][1]/100
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
        settings_label = menu_font.render((settings_sliders[0][0] +": "+ str(camera_slam)), True, (255,255,255))
        pygame.draw.rect(screen,(100,100,100),(75,100,550,25))
        if settings_sliders[0][2]:
            pygame.draw.rect(screen,(200,200,200),(75+settings_sliders[0][1],98,50,29))
        else:
            pygame.draw.rect(screen,(160,160,160),(75+settings_sliders[0][1],98,50,29))
        screen.blit(settings_label,(50,50))
    elif gamemode == "level":
        pygame.draw.rect(screen,(255,255,255),(goal_x*50 + camera_x, goal_y*50 + camera_y,50,50))
        for i in range(len(coins)):
            pygame.draw.circle(screen,(255,255,0),(coins[i][0]*50+camera_x+25,coins[i][1]*50+camera_y+25),10)
        for i in range(len(walls)):
            pygame.draw.rect(screen,(0,0,0),(walls[i][0]*50 + camera_x, walls[i][1]*50 + camera_y, 50, 50))
            pygame.draw.rect(screen,(60,60,85),(walls[i][0]*50+5 + camera_x, walls[i][1]*50+5 + camera_y,40,40))
        for i in range(len(stars)):
            if stars[i][2]:
                pygame.draw.circle(screen,(255,255,0),(stars[i][0]*50+camera_x+25,stars[i][1]*50+camera_y+25),20)

        pygame.draw.circle(screen, (character_r, character_g, character_b), (character_x*50+25 + camera_x, character_y*50+25 + camera_y), 25)
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