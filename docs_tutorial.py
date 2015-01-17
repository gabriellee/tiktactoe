from scipy import *
import sys, time

from pybrain.rl.environments.mazes import Maze, MDPMazeTask
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.environments import Task

import pylab
pylab.gray()
pylab.ion()

#create a maze!


structure = array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0, 0, 1, 0, 1],
                   [1, 0, 0, 1, 0, 0, 1, 0, 1],
                   [1, 0, 0, 1, 0, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1]])

environment = Maze(structure,(7,7))

#create agent containing controller (which maps states to actions), learner (updates states to actions), explorere (there by default)
#initialize table with # of states and actions
controller = ActionValueTable(81,4)
#initialize all Q values as 1
controller.initialize(1.)
learner = Q()
agent  = LearningAgent(controller,learner)

task = MDPMazeTask(environment)

#time to learn!
experiment = Experiment(task, agent)

while True:
	experiment.doInteractions(100)
	agent.learn()
	agent.reset()

	pylab.pcolor(controller.params.reshape(81,4).max(1).reshape(9,9))
	pylab.draw()



