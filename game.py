#Tic Tak Toe for python
import numpy as np
from anton import *

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
		self.tiles_marked = []
		self.v_fuck = False

	def create_player(self, name, symb):
		obj = self.Player(name, symb)
		self.players[name] = obj
		return obj

	def show_board(self):
		print self.showcase[0][0] + '\t' + self.showcase[0][1] + '\t' + self.showcase[0][2]
		print self.showcase[1][0] + '\t' + self.showcase[1][1] + '\t' + self.showcase[1][2]
		print self.showcase[2][0] + '\t' + self.showcase[2][1] + '\t' + self.showcase[2][2]
		
	#any move corresponding to areacode marked with symb
	def make_move(self, move, name, vmode):
		if vmode is 1:
			vishal_move = np.random.randint(1,10)
		used = False
		vishal_used = 1

		for tiles in self.tiles_marked:
			if tiles == move: 
				used = True
				if vmode is 1:
					if tiles == vishal_move:
						vishal_used = 0
		if used is False:
			if vishal_used == 0:
				if name is 'Vishal':
					move = vishal_move
					for items in self.players.values():
						if name is 'Vishal':
							symb = str(items.symb)
				self.board[self.areacode[vishal_move][0]][self.areacode[vishal_move][1]] = symb
				self.showcase[self.areacode[vishal_move][0]][self.areacode[vishal_move][1]] = symb
				self.v_fuck = True
			for items in self.players.values():
					if name is str(items.name):
						symb = str(items.symb)
			self.board[self.areacode[move][0]][self.areacode[move][1]] = symb
			self.showcase[self.areacode[move][0]][self.areacode[move][1]] = symb
			self.tiles_marked.append(move)
			self.v_fuck = False
		else:
			self.v_fuck = True

	#checks if there is a winner in the game or not
	def any_winner(self):
		#HORIZONTAL COLLECT
		T_h = [self.board[0][0],self.board[0][1],self.board[0][2]]
		M_h = [self.board[1][0],self.board[1][1],self.board[1][2]]
		B_h = [self.board[2][0],self.board[2][1],self.board[2][2]]
		T_hw = False 
		M_hw = False 
		B_hw = False
		#VERTICLE COLLECT
		T_v = [self.board[0][0],self.board[1][0],self.board[2][0]]
		M_v = [self.board[0][1],self.board[1][1],self.board[2][1]]
		B_v =  [self.board[0][2],self.board[1][2],self.board[2][2]]
		T_vw = False 
		M_vw = False
		B_vw = False 
		#DIAG COLLECT
		DRL = [self.board[0][0],self.board[1][1],self.board[2][2]]
		DLR = [self.board[2][0],self.board[1][1],self.board[0][2]]
		DRL_w = False 
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