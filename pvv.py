#Implementation of a 2v2 human v/s the dumb AI game format

from game import *

g = Game()
name1 = str(raw_input('Enter name for player 1: '))
name2 = 'Vishal'

player1 = g.Player(name1, 'x')
player2 = g.Player(name2, 'o')

def main_loop(retry_range):
	for x in xrange(retry_range,5): 
		move = int(raw_input('Enter move for ' + player1.name + ' :'))
		g.make_move(move, player1.symb)
		if g.v_fuck is True:
			while g.v_fuck is True:
				move = int(raw_input('Enter move for ' + player1.name + ' :'))
				g.make_move(move, player1.symb)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player1.name

		if x == 4:
			return 'Draw'
		print 'Vishal move'
		
		g.vishal_move(player2.symb)
		if g.v_fuck is True:
			while g.v_fuck is True:
				g.vishal_move(player2.symb)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player2.name

winner = main_loop(0)
if winner == 'Draw': print 'Its a draw'
else: print '\nThe winner is : ' + winner