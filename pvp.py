#Implementation of a 2v2 human game format

from game import *

g = Game()
name1 = str(raw_input('Enter name for player 1: '))
name2 = str(raw_input('Enter name for player 2: '))

player1 = g.Player(name1, 'x')
player2 = g.Player(name2, 'o')

def main_loop():
	for x in xrange(0,5): 
		move = int(raw_input('Enter move for ' + player1.name + ' :'))
		g.make_move(move, player1.symb)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player1.name
		if x == 4:
			return 'Draw'
		move = int(raw_input('Enter move for ' + player2.name +' :'))
		g.make_move(move, player2.symb)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player2.name
winner = main_loop()
print '\nThe winner is : ' + winner