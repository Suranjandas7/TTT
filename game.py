#Tic Tak Toe for python

import numpy as np

class Game(object):

	class Player(object):
		def __init__(self, name, symb):
			self.name = name
			self.wins = 0
			self.losses = 0
			self.draws = 0
			self.symb = symb

	#initializes board of the game and the areacodes
	def __init__(self):
		self.board = np.zeros(shape = (3,3), dtype = 'str')
		listA = [['1','2','3'],['4','5','6'],['7','8','9']]
		for x in xrange(0,3):
			for y in xrange(0,3):
				self.board[x][y] = listA[x][y]
		self.showcase = np.zeros(shape = (3,3), dtype = 'str')
		self.areacode = {1: [0,0], 2: [0,1], 3: [0,2],
						4: [1,0], 5: [1,1], 6: [1,2],
						7: [2,0], 8: [2,1], 9: [2,2]}
		self.players = {}
		self.Report = {}

	def create_player(self, name, symb):
		self.players[name] = self.Player(name, symb)

	def show_board(self):
		print self.showcase[0][0] + '\t' + self.showcase[0][1] + '\t' + self.showcase[0][2]
		print self.showcase[1][0] + '\t' + self.showcase[1][1] + '\t' + self.showcase[1][2]
		print self.showcase[2][0] + '\t' + self.showcase[2][1] + '\t' + self.showcase[2][2]
		
	#any move corresponding to areacode marked with symb
	def make_move(self, move, symb):
		try:
			if self.board[self.areacode[move][0]][self.areacode[move][1]] == 'x' or self.board[self.areacode[move][0]][self.areacode[move][1]] == 'o':
				print 'Tile not available'
			else:
				self.board[self.areacode[move][0]][self.areacode[move][1]] = symb
				self.showcase[self.areacode[move][0]][self.areacode[move][1]] = symb
		except KeyError:
			print 'Invalid Tile'

	#checks if board is full or not
	def board_is_full(self):
		for i in xrange(0,3):
			for y in xrange(0,3):
				if self.board[i][y] == 0:
					return False
		return True

	def who_won(self):
		winmethod = ''
		for element in self.Report:
			if self.Report[element] == True: winmethod = element

		if winmethod == 'T_hw' or winmethod == 'T_vw' or winmethod == 'DLR_w':
			return str(self.board[0][0])
		if winmethod == 'B_vw' or winmethod == 'DRL_w':
			return str(self.board[0][2])
		if winmethod == 'M_vw':
			return str(self.board[0][1])
		if winmethod == 'M_hw':
			return str(self.board[1][0])
		if winmethod == 'B_hw':
			return str(self.board[2][0])

	#checks if there is a winner in the game or not
	def any_winner(self):
		#HORIZONTAL COLLECT
		T_h = [self.board[self.areacode[1][0]][self.areacode[1][1]],self.board[self.areacode[2][0]][self.areacode[2][1]],self.board[self.areacode[3][0]][self.areacode[3][1]]]
		T_hw = False
		M_h = [self.board[self.areacode[4][0]][self.areacode[4][1]],self.board[self.areacode[5][0]][self.areacode[5][1]],self.board[self.areacode[6][0]][self.areacode[6][1]]]
		M_hw = False
		B_h = [self.board[self.areacode[7][0]][self.areacode[7][1]],self.board[self.areacode[8][0]][self.areacode[8][1]],self.board[self.areacode[9][0]][self.areacode[9][1]]]
		B_hw = False
		#VERTICLE COLLECT
		T_v = [self.board[self.areacode[1][0]][self.areacode[1][1]],self.board[self.areacode[4][0]][self.areacode[4][1]],self.board[self.areacode[7][0]][self.areacode[7][1]]]
		T_vw = False
		M_v = [self.board[self.areacode[2][0]][self.areacode[2][1]],self.board[self.areacode[5][0]][self.areacode[5][1]],self.board[self.areacode[8][0]][self.areacode[8][1]]]
		M_vw = False
		B_v = [self.board[self.areacode[3][0]][self.areacode[3][1]],self.board[self.areacode[6][0]][self.areacode[6][1]],self.board[self.areacode[9][0]][self.areacode[9][1]]]
		B_vw = False 
		#DIAG COLLECT
		DRL = [self.board[self.areacode[1][0]][self.areacode[1][1]],self.board[self.areacode[5][0]][self.areacode[5][1]],self.board[self.areacode[9][0]][self.areacode[9][1]]]
		DRL_w = False
		DLR = [self.board[self.areacode[3][0]][self.areacode[3][1]],self.board[self.areacode[5][0]][self.areacode[5][1]],self.board[self.areacode[7][0]][self.areacode[7][1]]]
		DLR_w = False
		
		#Checks
		if T_h[0] == T_h[1] == T_h[2]: T_hw = True
		if M_h[0] == M_h[1] == M_h[2]: M_hw = True
		if B_h[0] == B_h[1] == B_h[2]: B_hw = True

		if T_v[0] == T_v[1] == T_v[2]: T_vw = True
		if M_v[0] == M_v[1] == M_v[2]: M_vw = True
		if B_v[0] == B_v[1] == B_v[2]: B_vw = True

		if DRL[0] == DRL[1] == DRL[2]: DRL_w = True		
		if DLR[0] == DLR[1] == DLR[2]: DLR_w = True
		
		self.Report = {'T_hw' : T_hw, 'M_hw' : M_hw, 'B_hw' : B_hw, 'T_vw': T_vw, 'M_vw' : M_vw, 'B_vw' : B_vw, 'DRL_w' : DRL_w, 'DLR_w' : DLR_w} 