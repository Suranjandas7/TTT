
MAW
def anton_move(self, symb):
	possible_moves = [] 

	if self.board[0][0] != player1.symb:
		tl_corner = self.board[0][0] 
	if self.board[0][2] != player1.symb:
		tr_corner = self.board[0][2]
	if self.board[2][0] != player1.symb:
		bl_corner = self.board[2][0] 
	if self.board[2][2] != player1.symb:
		br_corner = self.board[2][2]

	for element in [tl_corner, tr_corner, bl_corner, br_corner]:
		if element != symb:
			possible_moves.append(element)

	#write a sorting procedure that removes ememy moves from possible_moves
	for element in possible_moves:
		print 'MAW'