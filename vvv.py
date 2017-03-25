#Implementation of a 2v2 human v/s the dumb AI game format
from game import *

def main_loop():
	g = Game()
	player1 = g.create_player('Vishal', 'X')
	player2 = g.create_player('VishalB', 'O')

	for x in xrange(0,5): 
		if player1.name == 'Vishal':
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
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player1.name 

		if x == 4:
			return 'Draw'
		
		if player2.name == 'VishalB':
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
		g.any_winner()
		for element in g.Report:
			if g.Report[element] == True: return player2.name

results = {'Vishal':0,'VishalB':0,'Draw':0}
megaresults = {1000:[],2000:[],3000:[],4000:[],5000:[],6000:[],7000:[],8000:[],9000:[],10000:[]}
for i in xrange(1,10002):
	winner = main_loop()
	results[winner] = int(results[winner])+1
	print 'Game Instance over'
	if i > 980:
		if ((i)%1000) is 1:
			megaresults[i-1] = ([results['Vishal'],results['VishalB'],results['Draw']])

print 'Results' + 'Vishal|VishalB|Draw'
print '100: ' + str(megaresults[1000])
print '200: ' + str(megaresults[2000])
print '300: ' + str(megaresults[3000])
print '400: ' + str(megaresults[4000])
print '500: ' + str(megaresults[5000])
print '600: ' + str(megaresults[6000])
print '700: ' + str(megaresults[7000])
print '800: ' + str(megaresults[8000])
print '900: ' + str(megaresults[9000])
print '1000: ' + str(megaresults[10000])

print 'Percentage : \n'
print 'Vishal :' + str(((int(results['Vishal']) * 100/10000)))
print 'VishalB :' + str(((int(results['VishalB']) * 100/10000)))
print 'Draw :' + str(((int(results['Draw']) * 100/10000)))