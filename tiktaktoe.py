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
		# x = map(lambda x: x[1], sorted(self.board.items()))
		# state_num = sum([(x[i]+1)*3**i for i in range(len(x))])
		# self.state_dict[state_num] = frozendict(self.board)

		#feature space: is the opponent about to win?
		#one feature for each space that the opponent might win by, plus a bias term
		#self.board = {(key1,key2):0 for key1 in [0,1,2] for key2 in [0,1,2]}
		# pdb.set_trace()
		#create dictionary of feature to positions, then turn it into a list
		feat_dict = {(key1,key2):0 for key1 in [0,1,2] for key2 in [0,1,2]};
		for opos in self.opos:
			ytest_vec = [0,1,2]
			ytest_vec.remove(opos[0])
			xtest_vec = [0,1,2]
			xtest_vec.remove(opos[1])
			#for each opponent position, check whether one of the other 2 spots in the row and then column are taken

		 	#check row, and col
			if ((opos[0],xtest_vec[0]) in self.opos) or ((opos[0],xtest_vec[1]) in self.opos):
				#pdb.set_trace()
				if ((opos[0],xtest_vec[0]) in self.empty):
					feat_dict[(opos[0],xtest_vec[0])] = 1;
				elif (opos[0],xtest_vec[1]) in self.empty:
					feat_dict[(opos[0],xtest_vec[1])] = 1;

			if (((ytest_vec[0],opos[1]) in self.opos) or ((ytest_vec[1],opos[1]) in self.opos)):
				#pdb.set_trace()
				if ((ytest_vec[0],opos[1]) in self.empty):
					feat_dict[(ytest_vec[0],opos[1])] = 1;
				elif (ytest_vec[1],opos[1]) in self.empty:
					feat_dict[(ytest_vec[0],opos[1])] = 1;

		#pdb.set_trace()
		if sum([self.board[(0,0)],self.board[(1,1)],self.board[(2,2)]])==-2:
			for key in [(0,0),(1,1),(2,2)]:
				if key in self.empty:
					feat_dict[key] = 1
					break
		if sum([self.board[(0,2)],self.board[(1,1)],self.board[(2,0)]])==-2:
			for key in [(0,2),(1,1),(2,0)]:
				if key in self.empty:
					feat_dict[key] = 1
					break

		#feature 2: could I win?  1=yes, 0=no
		# for mypos in self.mypos:
		# 	ytest_vec = [0,1,2]
		# 	ytest_vec.remove(opos[0])
		# 	xtest_vec = [0,1,2]
		# 	xtest_vec.remove(opos[1])
		# # 	#check row, col, and maybe diag
		# 	#print (((mypos[0],xtest_vec[0]) in mypos) or (((mypos[0],xtest_vec[1]) in mypos)) and (((mypos[0],xtest_vec[0]) in self.empty) or (mypos[0],xtest_vec[1]) in self.empty))
		# 	print mypos
		# 	if (((mypos[0],xtest_vec[0]) in self.mypos) or (((mypos[0],xtest_vec[1]) in self.mypos)) and (((mypos[0],xtest_vec[0]) in self.empty) or (mypos[0],xtest_vec[1]) in self.empty)):
		# 		feat2 = 1;
		# 		break
		# 	elif (((ytest_vec[0],mypos[1]) in self.mypos) or (((ytest_vec[1],mypos[1]) in self.mypos)) and (((ytest_vec[0],mypos[1]) in self.empty) or (ytest_vec[1],mypos[1]) in self.empty)):
		# 		feat2 = 1;
		# 		break
		# if sum([self.board[(0,0)],self.board[(1,1)],self.board[(2,2)]])==2 or sum([self.board[(0,2)],self.board[(1,1)],self.board[(2,0)]])==2:
		# 	feat2 = 1;
		# #feature three: are there corners open?
		# if ((0,0) in self.empty) or ((2,2) in self.empty) or ((0,2) in self.empty) or ((2,0) in self.empty):
		# 	feat3 = 1;

		#flatten the dictionary
		#add a bias term
		feat_list = [feat_dict[key] for key in sorted(feat_dict)]
		feat_list.append(1)
		print array(feat_list)
		print len(array(feat_list))
		return array(feat_list)
		#return array([state_num])

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




