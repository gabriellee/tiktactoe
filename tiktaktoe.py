from scipy import *
import sys, time

#from pybrain.rl.environments.twoplayergames import TwoPlayerGame
from tiktaktoe_opponent import TikTacToeOpponent

from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.environments import Task
from pybrain.rl.environments import Environment
from frozen_dict import frozendict
import pdb

#from twoplayergame import TwoPlayerGame
from random import randint


import pdb
import pylab


class TikTacToe(Environment):
	"""store info about the board in a list of xs and a list of os"""
	def __init__(self,dim):
		self.dim = 3
		self.reset()
		self.opp = TikTacToeOpponent()
		self.state_dict = {}
		self.state_freqs = [0 for i in range(3**9)]

	def reset(self):
		self.mypos = []
		self.opos = []
		self.board = {(key1,key2):0 for key1 in [0,1,2] for key2 in [0,1,2]}
		self.empty = [(i,j) for i in range(3) for j in range(3)]

	def getSensors(self):
		"""what is visible of the environment to the agent"""
		#pdb.set_trace()
		x = map(lambda x: x[1], sorted(self.board.items()))
		state_num = sum([(x[i]+1)*3**i for i in range(len(x))])
		self.state_dict[state_num] = frozendict(self.board)
		return array([state_num])

	def isLegal(self,newpos):
		if newpos[0] > self.dim:
			return False
		if newpos[1] > self.dim:
			return False
		print "my position ", self.mypos
		print "opos ", self.opos
		print 'newpos ', newpos
		if newpos in self.mypos or newpos in self.opos:
			print "ILLEGAL"
			return False
		return True

	def performAction(self, action):
		#check somewhere that the board is not filled
		#choose pos
		#play until the end
		#print('my turn!')
		#fix this

		
		newrow = int(action[0])/3
		newcol = action[0]%3

		if not self.isLegal((newrow,newcol)):
			return False
		else:
			self.mypos.append((newrow,newcol))
			#print self.mypos
			self.board[(newrow,newcol)] = 1 #us
			self.empty.remove((newrow,newcol))
			return True

	def oppAction(self):
		newopp_pos = self.opp.takeTurn(self)
		if newopp_pos == False:
			return False
		self.opos.append(newopp_pos)
		self.board[newopp_pos] = -1
		#print self.empty
		#print 'opp goes', newopp_pos
		#print newopp_pos
		self.empty.remove(newopp_pos)
		return True

	def gameOver(self):
		#print "Who won?"
		#pdb.set_trace()
		if self.empty == []:
			self.winner = 0
			print "gameover, no space left"
			return True
		elif self.board[(0,0)] != 0 and ((self.board[(0,0)] == self.board[(1,1)]) and (self.board[(2,2)] == self.board[(1,1)])):
			self.winner = self.board[(0,0)]
			#print "gameover, diag right"
			#pdb.set_trace()
			#print self.winner
			return True
		elif self.board[(0,2)] != 0 and ((self.board[(0,2)] == self.board[(1,1)]) and (self.board[(0,2)] == self.board[(2,0)])):
			self.winner = self.board[(0,2)]
			#print "gameover, diag left"
			#pdb.set_trace()
			#print self.winner
			return True
		for i in range(3):
			if self.board[(i,0)] != 0 and (self.board[(i,0)] == self.board[(i,1)] and (self.board[(i,2)] == self.board[(i,1)])):
				self.winner = self.board[(i,0)]
				#print "gameover, hor"
				#print self.winner
				return True
		for j in range(3):
			if self.board[(0,j)] != 0 and (self.board[(0,j)] == self.board[(1,j)] and (self.board[(2,j)] == self.board[(1,j)])):
				self.winner = self.board[(0,j)]
				#print "gameover, vert"
				#print self.winner
				return True
		return False




