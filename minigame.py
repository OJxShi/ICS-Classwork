import pygame, random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_SPACE

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# i coded most of this while i had a bad fever!
# inspired by (read: copied) the fishing minigame from stardew valley

fish_font = pygame.font.SysFont('Comic Sans', 30)
fish_alert_font = pygame.font.SysFont('Arial', 60)

#so many variables and for what
currently_fishing = False
cast_bobber = False
missed_fish = False
caught_fish = False

points = 0

fish_y = 200
fish_movement = 0
float_or_sink = 1
fish_movement_timer = 0
fish_pause = 10
fish_catch = 5

fishing_bar_y = 300
fishing_bar_movement = 0

fish_timer = 0
delay_before_next_cast = 0

text_timer = 0
ocean_bob = "up"
ocean_y = 0

#im not creative enough or knowledgable enough on sea life
list_of_fish = [ #there's probably (definitely) a better way to do this
{
   "name":"sardine",
   "points":50,
   "min":15,
   "max":50,
   "float_chance":50, # percentage change for the fish to float (< 50 = more likely to "sink", > 50 = more likely to "float")
   "timer":30, # misleading name; how quickly the fish moves actually (how many frames it takes for the fish to get from point A to point B)
   "pause":20, # frame delay between each movement
   "catch":10  # how much time is needed for the fish to be caught
},{
   "name":"cod",
   "points":100,
   "min":50,
   "max":60,
   "float_chance":50,
   "timer":25,
   "pause":15,
   "catch":15
},{
   "name":"seahorse",
   "points":150,
   "min":20,
   "max":30,
   "float_chance":50,
   "timer":15,
   "pause":5,
   "catch":15
},{
   "name":"anglerfish",
   "points":200,
   "min":20,
   "max":70,
   "float_chance":25,
   "timer":25,
   "pause":5,
   "catch":20
},{
   "name":"shark",
   "points":750,
   "min":75,
   "max":150,
   "float_chance":50,
   "timer":20,
   "pause":3,
   "catch":30
}
]

# fish = list_of_fish[0]

####################################

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            #the only key you'll ever really need for this game
            if event.key == K_SPACE:
                missed_fish = False
                if currently_fishing:
                    fishing_bar_movement = 30
                elif delay_before_next_cast == 0:
                    if cast_bobber == False:
                        cast_bobber = True
                        fish_timer = random.randrange(75,200)
                    elif fish_timer <= 30 and fish_timer >= 0:
                        cast_bobber = False
                        currently_fishing = True
                        fish = list_of_fish[random.randrange(0,len(list_of_fish))]
                        fish_catch = fish.get("catch")/3
                        fish_y = 200
                        
                    else:
                        cast_bobber = False
                        missed_fish = True
                        text_timer = 60
                    
        elif event.type == QUIT:
            running = False
    
####################################

# A bunch of timers or whatever   
	# counts down to when the fish bites 
    if cast_bobber:
        if fish_timer > 0:
            fish_timer -= 1
        else: # if you wait too long :(
            missed_fish = True
            cast_bobber = False
            fish_timer = 1
            text_timer = 60
    # prevents the player from accidentally casting the rod while still spamming spacebar from catching fish
    if delay_before_next_cast > 0:
        delay_before_next_cast -= 1
    # simple animation because why not
    if ocean_bob == "up":
        if ocean_y >= -5:
            ocean_y -= 0.1
        else: ocean_bob = "down"
    elif ocean_bob == "down":
        if ocean_y <= 5:
            ocean_y += 0.1
        else: ocean_bob = "up"
    # deletes text after set time
    if text_timer > 0:
        text_timer -= 1
    else:
        missed_fish = False
        caught_fish = False
    
# FISHING MINIGAME BAR
    fishing_bar_y = fishing_bar_y - fishing_bar_movement + 10
    fishing_bar_movement = fishing_bar_movement * 0.8
    
    if fishing_bar_y < 0: #stops bar from going too far
        fishing_bar_y = 0
    if fishing_bar_y > 300:
        fishing_bar_y = 300
    
# ACTUAL CODE FOR THE FISHING MINIGAME 
    if currently_fishing:
    
        # If the fishing bar is touching the fish
        if fish_y - 10 <= fishing_bar_y + 150 and fish_y + 10 >= fishing_bar_y:
            fish_catch += 0.1
        else: fish_catch -= 0.1
        
        # moving the "fish" circle
        if fish_movement_timer == 0:
            if fish_pause > 0:
                fish_pause -= 1
            else:
                fish_movement_timer = fish.get("timer")
                if random.randrange(1,100) <= fish.get("float_chance"):
                    float_or_sink = -1  # float (up is negative)
                else: float_or_sink = 1 # sink
                
                fish_movement = (random.randrange(fish.get("min"),fish.get("max")))/fish.get("timer") * float_or_sink
        # after every movement the fish pauses for a bit to make it a little easier
        else:
            fish_pause = fish.get("pause")
            fish_movement_timer -= 1
            fish_y += fish_movement
        # probably a better way to do this but who cares
        if fish_y <= 20:
            fish_y = 20
        elif fish_y >= 380:
            fish_y = 380
            
        if fish_catch >= fish.get("catch"):#caught
            currently_fishing = False
            caught_fish = True
            text_timer = 60
            points += fish.get("points")
            delay_before_next_cast = 10
        elif fish_catch <=0:#missed
            currently_fishing = False
            missed_fish = True
            text_timer = 60
            delay_before_next_cast = 5
####################################
    screen.fill((222, 248, 255))  
    
    #dock
    pygame.draw.rect(screen,(99, 66, 46),(250,300,30,150))
    pygame.draw.rect(screen,(99, 66, 46),(0,300,300,50))

    #player
    pygame.draw.rect(screen,(0,0,0),(185,235,30,6))#hips
    pygame.draw.rect(screen,(0,0,0),(185,235,6,65))#left leg
    pygame.draw.rect(screen,(0,0,0),(209,235,6,65))#right leg
    pygame.draw.rect(screen,(0,0,0),(175,195,50,6))#arms
    pygame.draw.rect(screen,(0,0,0),(197,165,6,75))#body
    pygame.draw.circle(screen,(0,0,0),(200,160),25)#head
    pygame.draw.circle(screen,(255,255,255),(200,160),20)#head
    
    #fishing rod
    if cast_bobber or currently_fishing: #line
        pygame.draw.polygon(screen,(255,255,255),((300,100),(297,97),(447,497+ocean_y),(450,500+ocean_y)))
    pygame.draw.polygon(screen,(156, 84, 33),((210,220),(213,223),(300,100),(297,97))) #rod
        
    #ocean
    pygame.draw.rect(screen,(26, 120, 171),(0,380+ocean_y,WIDTH,HEIGHT))
    # your cue to reel in (you have like 1 second)
    if fish_timer <= 30 and fish_timer >= 0 and cast_bobber:
        fish_alert_text = fish_alert_font.render(("!"), False, (255,0,0))
        screen.blit(fish_alert_text, (190,70))
    # fishing minigame
    if currently_fishing:
        pygame.draw.rect(screen,(100,100,100),(550,40,50,400))
        pygame.draw.rect(screen,(76, 217, 37),(550,40+fishing_bar_y,50,100))
        pygame.draw.circle(screen,(122, 220, 255),(575,40+fish_y),20)
        
        pygame.draw.rect(screen,(50,50,50),(605,40,30,400))
        
        pygame.draw.rect(screen,(255*(1-fish_catch/fish.get("catch")),55+200*fish_catch/fish.get("catch"),0),(605,440-400*fish_catch/fish.get("catch"),30,400*fish_catch/fish.get("catch")))
    # dumbest way to code
    if missed_fish:
        missed_fish_text = fish_font.render(("The fish got away!"), False, (0,0,0))
        screen.blit(missed_fish_text, (150,80))
    if caught_fish:
        caught_fish_text = fish_font.render(("You caught a " + fish.get("name") + "!"), False, (0,0,0))
        screen.blit(caught_fish_text, (150,80))
        
    points_text = fish_font.render(("Points: "+str(points)), False, (0,0,0))
    screen.blit(points_text,(10,0))

    pygame.display.flip()
    clock.tick(30)


pygame.quit()