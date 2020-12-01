# %%writefile 5_prev.py
import numpy as np
import pandas as pd
import random

T = np.zeros((3, 3, 3, 3, 3))
# P = np.zeros((3, 3))

# a1 is the action of the opponent 1 step ago
# a2 is the action of the opponent 2 steps ago
a1, a2, a3, a4, a5 = None, None, None, None, None

def transition_agent(observation, configuration):
    global T, P, a1, a2, a3, a4, a5
      
    if observation.step > 4:
        a1 = observation.lastOpponentAction
        T[a5][a4][a3][a2][a1] += 1
        a5 = a4
        a4 = a3
        a3 = a2
        a2 = a1
        max = 0
        maxI = -1
        for i in range(len(T[a5][a4][a3][a2])):
          if T[a5][a4][a3][a2][i] > max:
            max = T[a5][a4][a3][a2][i]
            maxI = i
        if maxI == 0:
          return 1
        elif maxI == 1:
          return 2
        elif maxI == 2:
          return 0
        else:
          return int(np.random.randint(3))

    else:
        if observation.step == 1:
            a2 = observation.lastOpponentAction
        elif observation.step == 2:
            a3 = observation.lastOpponentAction
        elif observation.step == 3:
            a4 = observation.lastOpponentAction
        elif observation.step == 4:
            a5 = observation.lastOpponentAction
        return int(np.random.randint(3))