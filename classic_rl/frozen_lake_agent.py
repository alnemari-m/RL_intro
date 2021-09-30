import gym
import numpy
import matplotlib.pyplot as plt
import numpy as np

"""
There are various policy it can be done to reach to the goal 
the determnstic policy if we are known the environment we
will be able to reach the goal determinstically 
policy = 2 * right + 3 * down + 1 * right 



"""


env = gym.make('FrozenLake-v1')

"""
0 --> left 
1 --> down 
2 --> right 
3 --> up 
SFFF
FHFH
FFFH
HFFG
"""

winer = []
scores = []
policy = {0:2,1:2,2:1,3:0,4:1,6:1,8:2,9:1,10:1,13:2,14:2}
#policy = {0:2,1:2,2:1,3:1,4:1,5:2}
for i in range(1000):
    done = False
    obs = env.reset()
    score = 0
    while not  done:
        obs, reward, done, info = env.step(policy[obs])
        score +=reward
        scores.append(score)
    if i %10 == 0:
        avg = np.mean((scores[-10:]))
        winer.append(avg)


plt.plot(winer)
plt.show()