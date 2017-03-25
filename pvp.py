#Implementation of a 2v2 human game format

from game import *

g = Game()
I_name1 = str(raw_input('Enter name for player 1: '))
I_name2 = str(raw_input('Enter name for player 2: '))
I_symb1 = str(raw_input('X or O for ' + I_name1 + ' : '))
I_symb2 = ''

if I_symb1 is 'X':
	I_symb2 = 'O'
if I_symb1 is 'O':
	I_symb2 = 'X'

if I_symb1 == 'X':
	player1 = g.create_player(I_name1, I_symb1)
	player2 = g.create_player(I_name2, I_symb2)
if I_symb2 == 'X':
	player1 = g.create_player(I_name2, I_symb2)
	player2 = g.create_player(I_name1, I_symb1)
	
def main_loop():
	for x in xrange(0,5): 
		move = int(raw_input('Enter move for ' + player1.name + ' :'))
		g.make_move(move, player1.name, 0)
		if g.v_fuck is True:
			while g.v_fuck is True:
				move = int(raw_input('Enter move for ' + player1.name + ' :'))
				g.make_move(move, player1.name)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player1.name
		
		if x == 4:
			return 'Draw'
		
		move = int(raw_input('Enter move for ' + player2.name +' :'))
		g.make_move(move, player2.name, 0)
		if g.v_fuck is True:
			while g.v_fuck is True:
				move = int(raw_input('Enter move for ' + player2.name + ' :'))
				g.make_move(move, player2.name)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player2.name

winner = main_loop()

if winner == 'Draw': print 'Its a draw'
else: print '\nThe winner is : ' + winner