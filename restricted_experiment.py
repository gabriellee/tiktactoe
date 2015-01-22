'''
by Gabrielle Ewall
1/20/15

'''

import episodicExperiment...

class RestrictedExperiment(EpisodicExperiment):
	'''restricts moves allowed to being legal
	if perform action returns false, it asks the agent to reselect a move.
	''' 
	def __init__(self,task,agent):
		EpisodicExperiment.__init__(self, task, agent)


	def _oneInteraction(self):
		check legality, by looking into environment, it can call right to is legal, bypassing performAction.  If it's not, get a new action, and repeat. THEN call to episdoic
		if self.task.isLegal(self.task.env, (int(action[0])/3, action[0]%3))
		return EpisodicExperiment._oneInteraction(self)

	do I redefine the method?
