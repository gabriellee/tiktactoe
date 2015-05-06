class TikTacToeOpponent(object):
	"""a silly tiktactoe opponent"""

	def __init__(self):
		self.spotpreflist = [(0,0),(0,2),(2,2), (2,0),(1,1),(1,2), (1,0),(2,1),(0,1)];
		self.mark = -1

	def takeTurn(self,game):
		'''selects it's favorite available spot and returns that position'''
		#print game.empty

		#check for places it can go to win
		for opos in game.opos:
			ytest_vec = [0,1,2]
			ytest_vec.remove(opos[0])
			xtest_vec = [0,1,2]
			xtest_vec.remove(opos[1])
			#for each opponent position, check whether one of the other 2 spots in the row and then column are taken

		 	#check row, and col
			if ((opos[0],xtest_vec[0]) in game.opos) or ((opos[0],xtest_vec[1]) in game.opos):
				#pdb.set_trace()
				if ((opos[0],xtest_vec[0]) in game.empty):
					return (opos[0],xtest_vec[0])
				elif (opos[0],xtest_vec[1]) in game.empty:
					return (opos[0],xtest_vec[1])

			if (((ytest_vec[0],opos[1]) in game.opos) or ((ytest_vec[1],opos[1]) in game.opos)):
				#pdb.set_trace()
				if ((ytest_vec[0],opos[1]) in game.empty):
					return (ytest_vec[0],opos[1])
				elif (ytest_vec[1],opos[1]) in game.empty:
					return (ytest_vec[0],opos[1])

		#pdb.set_trace()
		if sum([game.board[(0,0)],game.board[(1,1)],game.board[(2,2)]])==-2:
			for key in [(0,0),(1,1),(2,2)]:
				if key in game.empty:
					return key
		if sum([game.board[(0,2)],game.board[(1,1)],game.board[(2,0)]])==-2:
			for key in [(0,2),(1,1),(2,0)]:
				if key in game.empty:
					return key

		for spot in self.spotpreflist:
			if spot in game.empty:
				#print spot
				return spot
				feat_dict = {(key1,key2):0 for key1 in [0,1,2] for key2 in [0,1,2]};
		return False

