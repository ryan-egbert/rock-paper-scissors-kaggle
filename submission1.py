# %%writefile submission.py
import numpy as np
import pandas as pd
import random

T = np.zeros((3, 3))
P = np.zeros((3, 3))

a1, a2 = None, None

def transition_agent(observation, configuration):
    global T, P, a1, a2
      
    if observation.step > 1:
        a1 = observation.lastOpponentAction
        T[a2, a1] += 1
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
        return int(np.random.randint(3))