
#from pybrain.rl.environments.twoplayergames import TwoPlayerGame
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q
from pybrain.rl.experiments import EpisodicExperiment
from pybrain.rl.environments import Task
#from twoplayergame import TwoPlayerGame
from tiktaktoe_Task import TikTacToe_Task
from tiktaktoe import TikTacToe
import pdb
import numpy
import matplotlib.pyplot as plt
# import pylab
# pylab.gray()
# pylab.ion()


# class TikTacToe_Player(Agent):
# 	def __init__(self, game, mark = TikTacToe.X, **args):
#         self.game = game
#         self.mark = mark
#         self.setArgs(**args)

#there are 3^9 states
#the action space has an upper bound of 9
avtable = ActionValueTable(3**9, 9)#Ill need to tell it somewhere that not all states and actions are allowed
avtable.initialize(0.)


learner = Q()
agent = LearningAgent(avtable, learner)

env = TikTacToe(3)
task = TikTacToe_Task(env)
experiment = EpisodicExperiment(task,agent)

performance = numpy.zeros(10000)



#while True:
for i in range(10000):
	#agent moves, wits for next player to move.  updates Q accordingly.  next move. OR
	#agent moves, waits for other player to move. Repeats until end.  updates Q
	#print 'Lets play!'
	experiment.doEpisodes(1)
	#print agent._getLearning()
	#print "and the winner is: ", experiment.task.env.winner
	#performance[i] = (experiment.task.env.winner)
	#print avtable
	agent.learn()
	agent.reset()
	
	#print env.board[(0,0)], env.board[(0,1)], env.board[(0,2)]
	#print env.board[(1,0)], env.board[(1,1)], env.board[(1,2)]
	#print env.board[(2,0)], env.board[(2,1)], env.board[(2,2)]
	#if agent.controller == avtable:
	#	print "i learned"
	#reset clears out the agents last observations and action log
	#pylab.pcolor(avtable.params.max(1))
	#pylab.draw()

#pdb.set_trace()
plt.plot(env.state_freqs, 'x')
#plt.plot(performance,'o')
plt.show()

for i in range(10):
	ind1 = env.state_freqs.index(max(env.state_freqs))
	board = env.state_dict[ind1]
	print board
	print max(env.state_freqs)
	env.state_freqs[ind1] = 0


