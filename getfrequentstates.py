from tiktactoe_visualize import showBoard

for i in range(10):
	ind1 = env.state_freqs.index(max(env.state_freqs))
	board = env.state_dict[ind1]
	print board
	showBoard(board)
	print max(env.state_freqs)
	env.state_freqs[ind1] = 0


#get most frequent states
#find most frequent decision state
#moniter them for learning
