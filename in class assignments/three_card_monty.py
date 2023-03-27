import random
money = 100
# done in the loop now for replayability :)
# ace = random.randrange(1, 4)
validBet = False
betIsNumber = True
wrongChoice = [
"Pick a number from 1-3.",
"No, no, this isn't how you play the game!",
"Wrong",
"That's not a card.",
"Try again.",
"Please enter a valid number (1-3)",
"Fast Eddie looks mildy annoyed."]

#   ###  #   #     #   # #####  ###  #   #
#  #   # #   #      # #  #     #   # #   #
#  #   # #####       #   ###   ##### #####
#  #   # #   #       #   #     #   # #   #
#   ###  #   #       #   ##### #   # #   #

#   ###   ###  #   # ####  #     ##### #   #  ###  # #
#  #     #   # ## ## #   # #       #   ##  # #     # #
#  #  ## ##### # # # ####  #       #   # # # #  ## # #
#  #   # #   # #   # #   # #       #   #  ## #   # 
#   ###  #   # #   # ####  ##### ##### #   #  ###  # #

print("#===============================#\n")
print("         Welcome to the ")
print("    Gambling-Simulator-3000!\n")
print("#===============================#\n")

print("You slide up to Fast Eddie's card table.")

while True:
	ace = random.randrange(1, 4)
	while validBet == False:
		print("How much money are you betting? (Current balance: $" + str(money) + ")")
		
		#found on a tutorial online
		betIsNumber = True
		try: 
			bet = int(input())
		except ValueError:
		    betIsNumber = False
		    print ("Not a valid amount. Please enter a number.")
		    
		if betIsNumber == True:
			if bet <= 0:
				print("You can't bet that.")
			elif money - bet >= 0:
				validBet = True
			else:
				print("You don't have that much money.")
				
	validBet = False
	money -= bet
	print("You place $" + str(bet) + " on the table.")
	print("Fast Eddie glances at you out of the corner of his eye and starts shuffling.")
	print("He lays down three cards.")
	print("Which one is the ace?")
	print("\n     ##   ##   ##\n     ##   ##   ##\n     1    2    3\n")

	guess = input("The ace is card number...")

	while guess != "1" and guess != "2" and guess != "3":
		print(wrongChoice[random.randrange(len(wrongChoice))])
		guess = input("The ace is card number...")

	guess = int(guess)
	
	#wtf its that simple
	#Literally just remembered you can add onto string variables this is incredible
	card = "     "
	for i in range(1, 4):
		if i == ace:
			card += "AA   "
		elif i == guess:
			card += "JJ   "
		else:
			card += "##   "
	
	print("Fast Eddie flips over the card.")
	print("\n" + card)
	print(card)
	print("     1    2    3\n") 		
	
	#inefficient!! don't do this
#	 if guess == 1:
# 		if guess == ace:
# 			print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
# 			print("\n     AA   ##   ##\n     AA   ##   ##\n     1    2    3\n")
# 		else:
# 			print("\n     JJ   ##   ##\n     JJ   ##   ##\n     1    2    3\n")
# 			if ace == 2:
# 				print("Ha! Fast Eddie wins again! The ace was card number 2.")
# 				print("\n     JJ   AA   ##\n     JJ   AA   ##\n     1    2    3\n")
# 			elif ace == 3:
# 				print("Ha! Fast Eddie wins again! The ace was card number 3.")
# 				print("\n     JJ   ##   AA\n     JJ   ##   AA\n     1    2    3\n")
# 		
# 	elif guess == 2:
# 		if guess == ace:
# 			print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
# 			print("\n     ##   AA   ##\n     ##   AA   ##\n     1    2    3\n")
# 		else:
# 			print("\n     ##   JJ   ##\n     ##   JJ   ##\n     1    2    3\n")
# 			if ace == 1:
# 				print("Ha! Fast Eddie wins again! The ace was card number 1.")
# 				print("\n     AA   JJ   ##\n     AA   JJ   ##\n     1    2    3\n")
# 			elif ace == 3:
# 				print("Ha! Fast Eddie wins again! The ace was card number 3.")
# 				print("\n     ##   JJ   AA\n     ##   JJ   AA\n     1    2    3\n")
# 		
# 	elif guess == 3:
# 		if guess == ace:
# 			print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
# 			print("\n     ##   ##   AA\n     ##   ##   AA\n     1    2    3\n")
# 		else:
# 			print("\n     ##   ##   JJ\n     ##   ##   JJ\n     1    2    3\n")
# 			if ace == 1:
# 				print("Ha! Fast Eddie wins again! The ace was card number 1.")
# 				print("\n     AA   ##   JJ\n     AA   ##   JJ\n     1    2    3\n")
# 			elif ace == 2:
# 				print("Ha! Fast Eddie wins again! The ace was card number 2.")
# 				print("\n     ##   AA   JJ\n     ##   AA   JJ\n     1    2    3\n")
				
	if guess == ace:
		print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
		money += bet*3
		print("You won $" + str(bet*3) + "! (Current balance: $" + str(money) + ")\n")
	else:
		print("Ha! Fast Eddie wins again! The ace was card number " + str(ace) + ".")
		print("You lost $" + str(bet) + ". (Current balance: $" + str(money) + ")\n")
	
	if money > 0:
		print("Play again?")
		playAgain = input()
		if playAgain != "Yes" and playAgain != "yes": break
	else: break


if money == 0:
	print("All out of money! You are dead broke.")
	print("You head home and cry in the shower.")
elif money >= 100:
	print("Congrats, you made a profit of $" + str(money - 100) + "!")
	if money >= 1000000:
		print("damn go buy a house or something")
else:
	print("Congrats, you lost $" + str(-1*(money - 100)) + ".")
