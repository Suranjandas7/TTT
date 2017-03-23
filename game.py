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
		self.board = np.zeros(shape = (3,3), dtype = 'int')
		self.areacode = {1: [0,0], 2: [0,1], 3: [0,2],
						4: [1,0], 5: [1,1], 6: [1,2],
						7: [2,0], 8: [2,1], 9: [2,2]}
		self.players = {}

	def create_player(self, name, symb):
		self.players[name] = self.Player(name, symb)

	#any move corresponding to areacode marked with symb
	def make_move(self, move, symb):
		if self.board[self.areacode[move][0]][self.areacode[move][1]] == 0: self.board[self.areacode[move][0]][self.areacode[move][1]] = symb
		else: print 'Move already made on this tile.' 

	#checks if board is full or not
	def board_is_full(self):
		for i in xrange(0,3):
			for y in xrange(0,3):
				if self.board[i][y] == 0:
					return False
		return True

	def who_won(self, winmethod):
		if winmethod == 'T_h' or winmethod == 'T_v' or winmethod == 'DLR':
			return self.board[0][0]

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
		for element in T_h:
			if int(element) is 0:
				T_hw = False
		
		if M_h[0] == M_h[1] == M_h[2]: M_hw = True
		for element in M_h:
			if int(element) is 0:
				M_hw = False

		if B_h[0] == B_h[1] == B_h[2]: B_hw = True
		for element in B_h:
			if int(element) is 0:
				B_hw = False

		if T_v[0] == T_v[1] == T_v[2]: T_vw = True
		for element in T_v:
			if int(element) is 0:
				T_vw = False

		if M_v[0] == M_v[1] == M_v[2]: M_vw = True
		for element in M_v:
			if int(element) is 0:
				M_vw = False

		if B_v[0] == B_v[1] == B_v[2]: B_vw = True
		for element in B_v:
			if int(element) is 0:
				B_vw = False

		if DRL[0] == DRL[1] == DRL[2]: DRL_w = True
		for element in DRL:
			if int(element) is 0:
				DRL_w = False
		
		if DLR[0] == DLR[1] == DLR[2]: DLR_w = True
		for element in DLR:
			if int(element) is 0:
				DLR_w = False

		Report = {'T_hw' : T_hw, 'M_hw' : M_hw, 'B_hw' : B_hw, 'T_vw': T_vw, 'M_vw' : M_vw, 'B_vw' : B_vw, 'DRL_w' : DRL_w, 'DLR_w' : DLR_w} 