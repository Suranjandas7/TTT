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
for i in xrange(1,10001):
	winner = main_loop()
	results[winner] = int(results[winner])+1
	print 'Game Instance [' + str(i) + '] ongoing.'
	if i > 980:
		if i%1000 is 0:
			megaresults[i] = ([results['Vishal'],results['VishalB'],results['Draw']])
print '\n Opening file to write data.'
with open('Data.dat','a') as f:
	f.write('\n------NEWFILE--------\n')
	for x in [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
		Vishal = megaresults[x][0]
		VishalB = megaresults[x][1]
		Draw = megaresults[x][2]
		line = str(x) + '|' + str(Vishal) + '|' + str(VishalB) + '|' + str(Draw) + ''
		f.write(line + '\n')
	f.write('\n')
	overall_percent_Vishal = int(results['Vishal']) * 0.01
	overall_percent_VishalB = int(results['VishalB']) * 0.01
	overall_percent_Draw = int(results['Draw']) * 0.01
	f.write('Overall Percentages \n' + 'Vishal : ' + str(overall_percent_Vishal) + '\n' + 'VishalB : ' + str(overall_percent_VishalB) + '\n' + 'Draw : ' + str(overall_percent_Draw) + '\n')

print 'Data written for 10,000 matches in data.dat'