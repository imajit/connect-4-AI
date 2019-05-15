import numpy as np 
import random
import collections 
import math
ROWS =6
COLUMNS=7
PLAYER=0
AI=1
CHECK_LEN=4
EMPTY=0
def create_board():
	Board= np.zeros((ROWS,COLUMNS))
	return Board

def validate(board,move):
	if board[ROWS-1][move]==0:
		return True
	return False

def print_board(board):
	print(np.flip(board,0))

def make_move(board,move,player):
	for r in range(ROWS):
		if board[r][move]==0:
			board[r][move]=player+1
			break

def check_victory(board,player):
	for r in range(ROWS):
		for c in range(COLUMNS-3):
			if board[r][c]==player+1 and board[r][c+1]==player+1 and board[r][c+2]==player+1 and board[r][c+3]==player+1:
				return True

	for r in range(ROWS-3):
		for c in range(COLUMNS):
			if board[r][c]==player+1 and board[r+1][c]==player+1 and board[r+2][c]==player+1 and board[r+3][c]==player+1:
				return True

	for r in range(ROWS-3):
		for c in range(COLUMNS-3):
			if board[r][c]==player+1 and board[r+1][c+1]==player+1 and board[r+2][c+2]==player+1 and board[r+3][c+3]==player+1:
				return True		

	for r in range(3,ROWS):
		for c in range(COLUMNS-3):
			if board[r][c]==player+1 and board[r-1][c+1]==player+1 and board[r-2][c+2]==player+1 and board[r-3][c+3]==player+1:
				return True

def evaluate_move(aer,player):
	score=0
	opponent=PLAYER
	if player==PLAYER:
		opponent=AI

	if aer[player+1] == 4:
		score+=100
	elif aer[player+1]==3 and aer[EMPTY]==1:
		score+=5
	elif aer[player+1]==2 and aer[EMPTY]==2:
		score+=2
	if aer[opponent+1]==3 and aer[EMPTY]==1:
		score-=4
	return score

def scoring(board,player):
	score=0
	#center column
	col_check=board[:,COLUMNS//2]
	for i in range(ROWS):
		col_check[i]=int(col_check[i])
		for r in range(ROWS-3):
			check_len = col_check[r:r+CHECK_LEN]
			aer=collections.Counter(check_len)
			score+=aer[player+1]*3
	#score horizontal
	for r in range(ROWS):
		row_check= board[r,:]
		for i in range(COLUMNS):
			row_check[i]=int(row_check[i])
		for c in range(COLUMNS-3):
			check_len = row_check[c:c+CHECK_LEN]
			aer=collections.Counter(check_len)
			score+=evaluate_move(aer,player)
	
	#score vertical
	for c in range(COLUMNS):
		col_check= board[:,c]
		for i in range(ROWS):
			col_check[i]=int(col_check[i])
		for r in range(ROWS-3):
			check_len = col_check[r:r+CHECK_LEN]
			aer=collections.Counter(check_len)
			score+=evaluate_move(aer,player)	

	#score positive diagnol
	for r in range(ROWS-3):
		for c in range(COLUMNS-3):
			check_len=[ board[r+i][c+i] for i in range(CHECK_LEN) ]
			aer=collections.Counter(check_len)
			score+=evaluate_move(aer,player)

	#score negative diagnol
	for r in range(ROWS-3):
		for c in range(COLUMNS-3):
			check_len=[ board[r+CHECK_LEN-1-i][c+i] for i in range(CHECK_LEN) ]
			aer=collections.Counter(check_len)
			score+=evaluate_move(aer,player)

	return score

def minimax(board,depth,player,aplha,beta):
	valid_loc=valid_locations(board,player)
	if valid_loc==[]:
		return (None,0)
	if check_victory(board,PLAYER)==True:
		return (None,-100000000)
	if check_victory(board,AI)==True:
		return (None,100000000)
	if depth==0:
		return (None,scoring(board,AI))
	if player==AI:
		value=-math.inf
		col =random.choice(valid_loc)
		for c in valid_loc:
			temp_board=board.copy()
			make_move(temp_board,c,AI)
			new_scr=minimax(temp_board,depth-1,PLAYER,aplha,beta)[1]
			if new_scr>value:
				value=new_scr
				col=c
			aplha=max(aplha,value)
			if aplha>=beta:
				break
		return col,value

	if player==PLAYER:
		value=math.inf
		col =random.choice(valid_loc)
		for c in valid_loc:
			temp_board=board.copy()
			make_move(temp_board,c,AI)
			new_scr=minimax(temp_board,depth-1,AI,aplha,beta)[1]
			if new_scr<value:
				value=new_scr
				col=c
			beta=min(beta,value)
			if aplha>=beta:
				break
		return col,value

def valid_locations(board,player):
	valid_loc=[]
	for c in range(COLUMNS):
		if validate(board,c)==True:
			valid_loc.append(c)
	return valid_loc

def best_move(board,player):
	valid_loc=valid_locations(board,player)
	best_scr=-40000
	best_col=random.choice(valid_loc)
	for c in valid_loc:
		temp_board=board.copy()
		make_move(temp_board,c,player)
		scr=scoring(temp_board,player)
		if scr> best_scr:
			best_scr=scr
			best_col=c
	return best_col

board=create_board()
print_board(board)
end=False
player=PLAYER
while not end:
	#if player has his turn 
	if player==PLAYER:
		move = int(input("Enter your move P1 "))
		if validate(board,move)==True:
			make_move(board,move,player)
			print("User move")			
			print_board(board)
			if check_victory(board,player):
				print("Player 1 wins")
				end=True			
		else:
			print("invalid move ")
			player-=1

	if player==AI and end!= True:
		move,score = minimax(board,4,AI,-math.inf,math.inf)
		if validate(board,move)==True:
			make_move(board,move,player)
			print("AI move")
			print_board(board)
			if check_victory(board,player):
				print("Player 2 wins")
				end=True
		else:
			print("invalid move")
			player-=1

	player+=1
	player%=2