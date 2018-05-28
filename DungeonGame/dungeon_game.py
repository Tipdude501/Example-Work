import random

print("")
print("YOU ARE IN THE DUNGEON.")
print("")

CELLS = [(0, 0), (0, 1), (0, 2),
(1, 0), (1, 1), (1, 2),
(2, 0), (2, 1), (2, 2)]

def get_locations():
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	start = random.choice(CELLS)

	if monster == door or monster == start or door == start:
		return get_locations()

	return monster, door, start

def move_player(player, move):
	#player = (x,y)
	x, y = player

	if move == "LEFT":
		y -= 1
	elif move == "RIGHT":
		y += 1
	elif move == "UP":
		x -= 1
	elif move == "DOWN":
		x += 1
		
	return x, y

def get_moves(player):
	moves = ["LEFT", "RIGHT", "UP", "DOWN"]
	#player = (x, y)

	if player[1] == 0:
		moves.remove("LEFT")
	if player[1] == 2:
		moves.remove("RIGHT")
	if player[0] == 0:
		moves.remove("UP")
	if player[0] == 2:
		moves.remove("DOWN")

	return moves

monster, door, player = get_locations()

while True:
	moves = get_moves(player)

	print("Your location is: {}".format(player))
	print("You can move {}".format(moves)) 
	print("Enter 'QUIT' to exit game")

	for item in CELLS:
		if item == player:
			item = "X"
		else:
			item = " "

	print("|{}|{}|{}|".format((CELLS[0]),(CELLS[1]),(CELLS[2])))
	print("|{}|{}|{}|".format((CELLS[3]),(CELLS[4]),(CELLS[5])))
	print("|{}|{}|{}|".format((CELLS[6]),(CELLS[7]),(CELLS[8])))


	
	move = input("> ")
	move = move.upper()

	if move == "QUIT":
		break


	if move in moves:
		player = move_player(player, move)
	else:
		print("** You bumb clumbsily into a wall **")
		input("Press ENTER to continue")
		print("") 
		continue

	if player == door:
		print("You escaped!")
		input("Press ENTER to continue")
		break
	elif player == monster:
		print("You were eaten by the monster!")
		input("Press ENTER to continue")
		break

 

