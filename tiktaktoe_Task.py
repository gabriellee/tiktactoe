
from pybrain.rl.environments.task import Task
from numpy import *
import tiktaktoe_opponent
from pybrain.rl.environments.episodic import EpisodicTask
from tiktaktoe import TikTacToe
from pybrain.utilities import  Named



class TikTacToe_Task(EpisodicTask,Named):

	"""controls evaluations of the observations"""	
	def __init__(self, environment = None, **args):
		#print('fruy')
		EpisodicTask.__init__(self, TikTacToe(3))
		self.setArgs(**args)
		self.env = environment
		# opponent = TikTacToe_Player()
		# opponent = TikTacToe.o
		# opponent.mark = TikTacToe.o
		# self.opponent = opponent


	def reset(self):
		EpisodicTask.reset(self)

	def isFinished(self):
		res = self.env.gameOver()
		return res

	def performAction(self, agent):
		#print "actioning"
		EpisodicTask.performAction(self, agent)
		self.env.oppAction()


	def getObservation(self):
		sensors = self.env.getSensors()
		self.env.state_freqs[sensors] +=1
		return sensors

	def  getReward(self):
		if self.isFinished():
			#print "getting reward"
			if self.env.winner != self.env.opp.mark:
				res = 1
				#print 'I won!'
			else:
				res = -1
		else:
			res = 0
		return res

