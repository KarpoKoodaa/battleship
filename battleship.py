'''This is a battleship python game. Purpose is to learn code Python programming language'''
from random import randint #random generator


board = []
	
#Create 10x10 board with "O"
for i in range(10):
	board.append(["O"]*10) # One row from 0-9 "O"
#Adds the 1-9 digits into the board sides
i = 1 
board[0][0] = " " 
while (i < 10):
	zero = 0
	board[zero][i] = str(i)
	board[i][zero] = str(i)
	i = i+1
#Get rid of " " and print just O
def print_board(board):
	for i in board:
		print " ".join(i)

def random_row(board):
	return randint(1,len(board)-1) 

def random_col(board):
	return randint(1,len(board)-1)



patrol_ship_row = random_row(board)
patrol_ship_col = random_col(board)

'''direction = patrol_ship_row % patrol_ship_col
if direction  == 0:
	board[patrol_ship_row+1][patrol_ship_col] = "*"
else:
	board[patrol_ship_row][patrol_ship_col+1] = "*"'''

board[patrol_ship_row][patrol_ship_col]= "*"

print patrol_ship_row, patrol_ship_col

print_board(board)
for turn in range(5):
 	print "Turn: ", turn+1
	#guessing
	guess_row = int(raw_input("Guess Row: "))
	guess_col = int(raw_input("Guess Col: "))

	if guess_row == patrol_ship_row and guess_col == patrol_ship_col:
		print "Hit and sank!!"
		break

	elif guess_row not in range(1,10) or guess_col not in range(1,10):
		print "Out of range"
		
	else:
		print "Miss"
		board[guess_row][guess_col] = "X"
		print_board(board)
	
	if turn == 4:
		print "Game Over!"
		
#board = []	
	
#create_board(board)



	