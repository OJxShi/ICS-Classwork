import pygame
import random
import math
from pygame.locals import K_ESCAPE, K_q, KEYDOWN, QUIT

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

stats_font = pygame.font.SysFont('Arial', 20)
speech_font = pygame.font.SysFont('Comic sans', 50)

speed_x = 0
speed_y = 0
friction = 0.2
cam_x = 0
cam_y = 0

cloud_x = 0
cloud_timer = 0
cloud_direction = "right"

play_animation = False
frame = 0

guy_x = 1
guy_y = 1

door_open = False

def draw_tree(distance, x):
	pygame.draw.rect(screen,(100,50,0),(cam_x*distance+x,cam_y*distance+(235-distance*30),20*distance,90*distance))
	pygame.draw.circle(screen,(100,200,50),(cam_x*distance+x +(10*distance),cam_y*distance+(235-distance*30)),30*distance)

def drawGuy(distance, x): #this hurts my brain and still doesn't work as intended. whatever
	#what do you think i am, a graphic designer?
	gx = cam_x*distance+x
	gy = cam_y*distance
	#head
	pygame.draw.circle(screen,(0,0,0),(gx,gy+(250-distance*30)),15*distance)
	#body
	pygame.draw.rect(screen,(0,0,0),(gx-3*distance,gy+230-(distance-1)*15,6*distance,35*distance))
	#arms
	pygame.draw.rect(screen,(0,0,0),(gx-15*distance,gy+240-(distance-1)*5,30*distance,6*distance))
	#legs
	pygame.draw.rect(screen,(0,0,0),(gx-10*distance,gy+265+(distance-1)*15,20*distance,6*distance))
	pygame.draw.rect(screen,(0,0,0),(gx-10*distance,gy+265+(distance-1)*15,6*distance,30*distance))
	pygame.draw.rect(screen,(0,0,0),(gx+4*distance,gy+265+(distance-1)*15,6*distance,30*distance))

running = True
while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			if event.key == K_q:
				play_animation = True
		elif event.type == QUIT:
			running = False
	
	keys = pygame.key.get_pressed()
	
	if keys[119] == True:  # w
		if cam_y < 25:
			speed_y += 1
	if keys[97] == True:  # a
		if cam_x < 50:
			speed_x += 1
	if keys[115] == True:  # s
		if cam_y > -25:
			speed_y -= 1
	if keys[100] == True:  # d
		if cam_x > -50:
			speed_x -= 1

	if cam_x > 50:
		cam_x = 50
	elif cam_x < -50:
		cam_x = -50
		
	if cam_y > 25:
		cam_y = 25
	elif cam_y < -25:
		cam_y = -25
	
	speed_x *= 1 - friction
	speed_y *= 1 - friction
	cam_x += speed_x
	cam_y += speed_y
	
	if cloud_direction == "right":
		if cloud_x <= 10:
			cloud_x += 0.1
		else:
			cloud_direction = "left"
	elif cloud_direction == "left":
		if cloud_x >= -10:
			cloud_x -= 0.1
		else:
			cloud_direction = "right"
	
	if play_animation == True:
		door_open = True
		if frame < 30:
			guy_y = 2.0 #controls guy drawing
			guy_x = 375
		elif frame < 50:
			guy_y += 0.2
		elif frame > 120 and frame < 145:
			guy_y -= 0.2
		elif frame > 150:
			door_open = False
			play_animation = False
			frame = -1
		frame+=1


##################

	#sky
	screen.fill((200, 240, 255))
	#clouds
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+50 +cloud_x,cam_y*0.1+50),20)
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+75 +cloud_x,cam_y*0.1+40),28)
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+100+cloud_x,cam_y*0.1+52),25)
	
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+400+cloud_x,cam_y*0.1+70),15)
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+415+cloud_x,cam_y*0.1+75),16)
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+430+cloud_x,cam_y*0.1+65),20)
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+450+cloud_x,cam_y*0.1+70),20)
	pygame.draw.circle(screen,(255,255,255),(cam_x*0.1+480+cloud_x,cam_y*0.1+70),10)
	#grass
	pygame.draw.rect(screen, (100,230,50),(0,cam_y*0.5+270,WIDTH,HEIGHT))
	#path
	#pygame.draw.polygon(screen, (220,200,170),((cam_x*0.5+500,cam_y*0.5+270),(cam_x*0.5+550,cam_y*0.5+270),(cam_x*8+540,cam_y*8+600),(cam_x*8+400,cam_y*8+600)))

	draw_tree(0.8,120)
	draw_tree(0.9,600)
	draw_tree(1,250)
	draw_tree(1.3,500)
	draw_tree(1.75,25)
	
	#house
	pygame.draw.rect(screen, (217,203,184), (cam_x*2+275,cam_y*2+140,200,200))
	pygame.draw.rect(screen, (70,70,70), (cam_x*2+325,cam_y*2+180,100,160))
	pygame.draw.polygon(screen,(180,30,30),((cam_x*2+250,cam_y*2+140),(cam_x*2+500,cam_y*2+140),(cam_x*2+450,cam_y*2+100),(cam_x*2+300,cam_y*2+100)))
	if door_open == False:
		pygame.draw.rect(screen, (173, 124, 88), (cam_x*2+325,cam_y*2+180,100,160))
	elif door_open == True:
		pygame.draw.polygon(screen,(173,124,88),((cam_x*2+325,cam_y*2+180),(cam_x*2+325,cam_y*2+340),(cam_x*2.3+315,cam_y*2.2+344),(cam_x*2.3+315,cam_y*2.2+175)))
	

	draw_tree(2,600)
	draw_tree(3,100)
	
	if play_animation == True and frame < 145:
		drawGuy(guy_y,guy_x)
	if frame > 50 and frame < 100:
		speechtext = speech_font.render(("Yo"), False, (255,255,255))
		screen.blit(speechtext, (cam_x*6.2+360, cam_y*6.2+50))
	
	cameratext = stats_font.render(str(round(-cam_x)) + " " +str(round(-cam_y)), False, (0, 0, 0)) 
	screen.blit(cameratext, (10, 3))
		
	pygame.display.flip()
	clock.tick(30)


pygame.quit()