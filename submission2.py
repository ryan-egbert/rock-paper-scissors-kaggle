import numpy as np

def mirror_opponent_agent(observation, configuration):
    if observation.step > 1:
      return observation.lastOpponentAction
    else:
      return int(np.random.randint(3))