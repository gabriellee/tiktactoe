"""
created by Gabrielle Ewall

1/17/2015

"""


import matplotlib.pyplot as plt
import numpy as np
import pdb

def showBoard(board):
    """ """
    opp_hcoords = list()
    opp_vcoords = list()
    learner_vcoords = list()
    learner_hcoords = list()


    #divide positions into x positions and o positions
    #map positions onto their locations on the graph
    for pos in board:
        if board[pos] == 0:
            continue
        elif board[pos] == -1:
            opp_hcoords.append(pos[0]*10 + 5)
            opp_vcoords.append(pos[1] * 10 + 5)
        else:
            learner_hcoords.append(pos[0]*10 + 5)
            learner_vcoords.append(pos[1] * 10 + 5)

    #make graph
    #pdb.set_trace()
    plt.figure()
    #hold on;
    #draw lines
    plt.hlines(20,0,30)
    plt.hlines(10,0,30)

    plt.vlines(20,0,30)
    plt.vlines(10,0,30)

    #pdb.set_trace()

    #draw marks
    plt.scatter(opp_hcoords, opp_vcoords, marker = 'o', s=900)
    plt.scatter(learner_hcoords, learner_vcoords, marker = 'x', s=900)
    #plt.legend('line','line','opponent', 'learner')

    plt.show()



    #graph horizontal and vertical lines
    #graph the xs and os
    #new board position = old *20 + 10