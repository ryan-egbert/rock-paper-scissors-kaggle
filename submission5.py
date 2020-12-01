# %%writefile 2_prev_wlt.py
import numpy as np
import pandas as pd
import random

Tw = np.zeros((3, 3))
Tl = np.zeros((3, 3))
Tt = np.zeros((3, 3))
P = np.zeros((3, 3))

# a1 is the action of the opponent 1 step ago
# a2 is the action of the opponent 2 steps ago
a1, a2 = None, None
lastAction = 0

def transition_agent(observation, configuration):
    global Tw, Tl, Tt, P, a1, a2, lastAction
    T = None
      
    if observation.step > 1:
        a1 = observation.lastOpponentAction
        if (lastAction == 0 and a1 == 0) or (lastAction == 1 and a1 == 1) or (lastAction == 2 and a1 == 2):
          Tt[a2,a1] += 1
          T = Tt
        elif (lastAction == 0 and a1 == 1) or (lastAction == 1 and a1 == 2) or (lastAction == 2 and a1 == 0):
          Tw[a2,a1] += 1
          T = Tw
        elif (lastAction == 0 and a1 == 2) or (lastAction == 1 and a1 == 0) or (lastAction == 2 and a1 == 1):
          Tl[a2,a1] += 1
          T = Tl
        else:
          return int(np.random.randint(3))
        a2 = a1
        max = 0
        maxI = -1
        for i in range(len(T[a2])):
          if T[a2][i] > max:
            max = T[a2][i]
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
        lastAction = int(np.random.randint(3))
        return lastAction