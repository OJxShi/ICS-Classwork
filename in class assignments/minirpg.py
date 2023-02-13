x = 2
y = 1
goalx = 6
goaly = 5
movable = True
movecount = 0
wallcheck = 0

# # old "box" system
# ybound1 = 0
# ybound2 = 7 #i dont know!!! my coding is bad!!
# xbound1 = 1
# xbound2 = 7

#this is probably one of the worst ways to do this but uhhh it can't be helped :P
wallsListX = [
#upper bounds
2, 3, 4, 5, 6,
#lower bounds
2, 3, 4, 5, 6,
#left side
1, 1, 1, 1,
#right side
#ha~ o mukidashite
7, 7, 7, 7, 7, 
#wall 1
3, 3, 3,
#wall 2
5, 5, 5
]

wallsListY = [
#upper bounds
5, 5, 5, 5, 6,
#lower bounds
0, 0, 0, 0, 0,
#left side
1, 2, 3, 4,
#right side
#ha~ o mukidashite
1, 2, 3, 4, 5,
#wall 1
1, 2, 3,
#wall 2
1, 3, 4
]


def p(): print("Your current position is (" + str(x) + ", " + str(y) + ").")
def cantMoveError(): print ("Sorry, you can't do that. Try moving in smaller increments, or in other directions!")

print("Enter your name.")
name = input()
print("Hello,", name + "!")
print("Welcome! Please make your way to the goal.")

# repeat until at goal
while x != goalx or y != goaly:
    p()
    print("The goal is (" + str(goalx) + ", " + str(goaly) + ").")
    print("What direction do you want to go? (up, down, left, right)")
 
    direction = input()
    
# so i don't softlock and have to reset
    if direction == "quit" or direction == "up" or direction == "left" or direction == "down" or direction == "right":
        if direction == "quit":
            x = goalx
            y = goaly
        else: movecount += 1
        
        print("Okay, and how many steps would you like to go?")
        movement = abs(int(input()))
        
       #IT WORKS!!! GOD IS GOOD!! GOD IS GREAT!!
        if direction == "up":
            i = 0
            movable = True
            while i < movement:
                i += 1
                wallcheck = 0
                while wallcheck <= len(wallsListX) - 1: #ITS THAT SIMPLE ALL I WAS MISSING WAS A -1 OF COURSE 
                    if x == wallsListX[wallcheck] and y + i == wallsListY[wallcheck]:
                        movable = False
                    wallcheck += 1
            if movable == True:
                y += movement
            else: cantMoveError()
            
        if direction == "down":
            i = 0
            movable = True
            while i < movement:
                i += 1
                wallcheck = 0
                while wallcheck <= len(wallsListX) - 1:
                    if x == wallsListX[wallcheck] and y - i == wallsListY[wallcheck]:
                        movable = False
                    wallcheck += 1
            if movable == True:
                y -= movement
            else: cantMoveError()
            	
        if direction == "right":
            i = 0
            movable = True
            while i < movement:
                i += 1
                wallcheck = 0
                while wallcheck <= len(wallsListX) - 1:
                    if x + i == wallsListX[wallcheck] and y == wallsListY[wallcheck]:
                        movable = False
                    wallcheck += 1
            if movable == True:
                x += movement
            else: cantMoveError()
            
        if direction == "left":
            i = 0
            movable = True
            while i < movement:
                i += 1
                wallcheck = 0
                while wallcheck <= len(wallsListX) - 1:
                    if x - i == wallsListX[wallcheck] and y == wallsListY[wallcheck]:
                        movable = False
                    wallcheck += 1
            if movable == True:
                x -= movement
            else: cantMoveError()
    


# ==========================
# ====== WALLS V.1.0 =======
# ==========================  
#(doesn't work)  

#         if direction == "up":
#             i = 0
#             loopquit = False
#             movalble = True
#             wallcheck = 1
#             while i <= movement:
#                  i += 1
#                  while wallcheck <= 25 and loopquit == False:
#                      if x == wallsList[wallcheck * 2 - 1] and y + i == wallsList[wallcheck * 2]:
#                          movable = False
#                          print("Sorry, you can't do that. There is a wall in your way. Try again!")
#                          wallcheck = 26
#                          loopquit == True
#                          i = movement + 1  #instantly cancels the loop
#                      
#                      #else:
#                      #    movable = True
#                      wallcheck += 1
#                      
#             if movable == True:
# 	            y += movement

# ==========================
# ========SIMPLE BOX========
# ==========================
#(Works, but is incredibly stupid and only has a box)

#     if direction == "up":
#     #I'm gonna be real with you this was awful I hate coding
#       i = 0  #
#       while i <= movement:  #tracing steps forwards to see if there is a wall
#         i += 1
#         if y + i == ybound1 or y + i == ybound2:
#           movable = False
#           print(
#             "Sorry, you can't do that. There is a wall in your way. Try again!"
#           )
#           i = movement + 1  #instantly cancels the loop
#         else:
#           movable = True
# 
#       if movable == True:
#         y += movement
# 
#     elif direction == "down":
#       i = 0  #vibe check
#       while i <= movement:  #tracing steps forwards to see if there is a wall
#         i += 1
#         if y - i == ybound1 or y - i == ybound2:
#           movable = False
#           print("Action failed. Try moving in another direction, or move in smaller steps.")
#           i = movement + 1  #instantly cancels the loop
#         else:
#           movable = True
# 
#       if movable == True:
#         y -= movement
#     elif direction == "left":
#       x -= movement
#     elif direction == "right":
#       x += movement

    else: print("Sorry, please enter a valid direction. (up, down, left, right)")

#finish
print("Congratulations,", name + "! You made it to the goal in", movecount, "moves.")

# # Old code that auto completes maze (also shows sequence needed)
# p()
#
# y += 3
# p()
#
# x += 2
# p()
#
# y -= 2
# p()
#
# x += 2
# p()
#
# y +=3
# p()
#
# print("GOAL!!")
