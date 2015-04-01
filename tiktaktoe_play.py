
#from pybrain.rl.environments.twoplayergames import TwoPlayerGame
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import NFQ, ActionValueNetwork
from pybrain.rl.experiments import EpisodicExperiment
from pybrain.rl.environments import Task
from tiktactoe_visualize import showBoard
#from twoplayergame import TwoPlayerGame
from tiktaktoe_Task import TikTacToe_Task
from tiktaktoe import TikTacToe
from restricted_experiment import RestrictedExperiment
import pdb
import numpy as np
import matplotlib.pyplot as plt
# import pylab
# pylab.gray()
plt.ion()



#DEFINE THE EXPERIMENT
#there are 3^9 states
#the action space has an upper bound of 9
avnet = ActionValueNetwork(3,9)#Ill need to tell it somewhere that not all states and actions are allowed
#vnet.initialize(0.)
learner = NFQ()
agent = LearningAgent(avnet, learner)
env = TikTacToe(3)
task = TikTacToe_Task(env)
# experiment = EpisodicExperiment(task,agent)
experiment = RestrictedExperiment(task,agent)

#performance = np.zeros(10000)
q_stack = [0 for i in range(9)]

#show the board at the chosen state
watch_state = 12099.0

winloss_record =list()
learning_curve = list()
#while True:
for i in range(1000):
	experiment.doEpisodes(1)
 	agent.history.addSample(agent.lastobs, agent.lastaction, 0)

	agent.learn()
	does_occur = [state_list[0] == watch_state for sequence in agent.learner.dataset for state_list,av,rew in sequence]
	action_taken = [av for sequence in agent.learner.dataset for state_list,av,rew in sequence if state_list[0] == watch_state]

	if any(does_occur):
		#pdb.set_trace()
		#generate a list of q values for each action taken
		q_stack[int(action_taken[0][0])] = agent.learner.module.getValue(int(watch_state), int(action_taken[0]))
		# if action_taken[0][0] == 1:
		# 	pdb.set_trace()
		#[self.module.getValue(12099, ac[0]) for sequence in self.dataset for state, action, reward in eq]

	#pdb.set_trace()
	winloss_record.append(env.winner)
	av_intvl = 10
	if len(winloss_record)%av_intvl == 0:
		learning_curve.append(np.mean(winloss_record[-av_intvl:]))

	agent.reset()

#map q_stack to the board
q_table = np.flipud(np.array(q_stack).reshape(3,3).transpose())

plt.plot(learning_curve)
#plt.pcolor(q_table)
#plt.draw()
plt.show()
	


#pdb.set_trace()
print q_stack
#showBoard(env.state_dict[np.array([watch_state])[0]])


#plt.plot(env.state_freqs, 'x')
#plt.plot(performance,'o')
#plt.show()
#pdb.set_trace()

for i in range(30):
	ind1 = env.state_freqs.index(max(env.state_freqs))
	board = env.state_dict[ind1]
	print ind1
	print board
	#frozendict({(0, 1): 0, (1, 2): 0, (0, 0): -1, (2, 1): 1, (1, 1): 1, (2, 0): 0, (2, 2): 0, (1, 0): 0, (0, 2): -1})

	#showBoard(board)
	print max(env.state_freqs)
	env.state_freqs[ind1] = 0


