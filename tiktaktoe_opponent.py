class TikTacToeOpponent(object):
	"""a silly tiktactoe opponent"""

	def __init__(self):
		self.spotpreflist = [(0,0),(0,2),(2,2), (2,0),(1,1),(1,2), (1,0),(2,1),(0,1)];
		self.mark = -1

	def takeTurn(self,game):
		'''selects it's favorite available spot and returns that position'''
		#print game.empty
		for spot in self.spotpreflist:
			if spot in game.empty:
				#print spot
				return spot

		return False
