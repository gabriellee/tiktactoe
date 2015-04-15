from pybrain.rl.experiments.episodic import EpisodicExperiment
from tiktactoe_visualize import showBoard
import pdb


class RestrictedExperiment(EpisodicExperiment):
	#'''restricts moves allowed to being legal if perform action returns false, it asks the agent to reselect a move.''' 
	def __init__(self,task,agent):
		EpisodicExperiment.__init__(self, task, agent)

	def _oneInteraction(self):
		#check legality, by looking into environment, it can call right to is legal, bypassing performAction.  If it's not, get a new action, and repeat. THEN call to episdoic"
        #self.agent


		self.stepid += 1
		print "integrating observation"
		print self.task.getObservation()
		#self.agent
		self.agent.integrateObservation(self.task.getObservation())
		print "done integrating"
		action = self.agent.getAction()
		#showBoard(self.task.env.state_dict[self.task.getObservation()[0]])

		counter = 0
		tally = 0
		while not(self.task.isLegal(action)):
			tally+=1
			#clear last action
			self.agent.lastaction = None#is this right?
			if len(self.task.env.empty):
				action = [self.task.env.empty[0][0]*3 + self.task.env.empty[0][1]]
				self.agent.lastaction = action
			else:
				action = self.agent.getAction()
			print action
			print int(action[0])/3, action[0]%3
			if tally == 40:
			 	pdb.set_trace()

		print "selected action is ", action
		self.task.performAction(action)
		reward = self.task.getReward()
		self.agent.giveReward(reward)
		return reward


