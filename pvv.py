#Implementation of a 2v2 human v/s the dumb AI game format
from game import *

g = Game()
I_name1 = str(raw_input('Enter name for player 1: '))
I_name2 = 'Vishal'
I_symb1 = str(raw_input('X or O for ' + I_name1 + ' : '))
if I_symb1 == 'X':
	player1 = g.create_player(I_name1, I_symb1)
	player2 = g.create_player('Vishal', 'O')
if I_symb1 == 'O':
	player1 = g.create_player('Vishal', 'X')
	player2 = g.create_player(I_name1, I_symb1)

def main_loop(retry_range):
	for x in xrange(0,5): 
		if player1.name == 'Vishal':
			print 'Making Dumb AI MOVE'
			move = np.random.randint(1,10)	
			g.make_move(move, player1.name, 1)		
			if g.v_fuck is True:
				while g.v_fuck is True:
					move = np.random.randint(1,10)
					g.make_move(move, player1.name, 1)
		else:
			move = int(raw_input('Enter move for ' + player1.name + ' :'))
			g.make_move(move, player1.name, 0)
			if g.v_fuck is True:
				while g.v_fuck is True:
					move = int(raw_input('Enter move for ' + player1.name + ' :'))
					g.make_move(move, player1.name, 0)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player1.name

		if x == 4:
			return 'Draw'
		
		if player2.name == 'Vishal':
			print 'Making Dumb AI MOVE'
			move = np.random.randint(1,10)	
			g.make_move(move, player2.name, 1)
			if g.v_fuck is True:
				while g.v_fuck is True:
					move = np.random.randint(1,10)
					g.make_move(move, player2.name, 1)
		
		else:
			move = int(raw_input('Enter move for ' + player2.name + ' :'))
			g.make_move(move, player2.name, 0)
			if g.v_fuck is True:
				while g.v_fuck is True:
					move = int(raw_input('Enter move for ' + player2.name + ' :'))
					g.make_move(move, player2.name, 0)
		g.show_board()
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player2.name

winner = main_loop(0)
if winner == 'Draw': print 'Its a draw'
else: print '\nThe winner is : ' + winner