"""
The main idea we want to build a robot,
this robot able to assmble a guitar
if you have this enviorment
[L1]   [L2]  [L3]
__
[L4]| [L5] |[L6]
            __
[L7] [L8]  [L9]

every L1 has its role to build the guitar
L6 is the most impratn
but L4 and L6 has some barrier

States -- >
Actions
Rewards
the bellman equation
"""
import numpy as np

states = {"l1":0,"l2":1,"l3":2,"l4":3,"l5":4,"l6":6,"l7":6,"l8":7,"l9":8}
actions = [0,1,2,3,4,5,6,7,8]
rewards = np.array([[0,1,0,0,0,0,0,0,0],
              [1,0,1,0,1,0,0,0,0],
              [0,1,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,1,0,0],
              [0,1,0,0,0,0,0,1,0],
              [0,0,1,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,1,0],
              [0,0,0,0,1,0,1,0,1],
              [0,0,0,0,0,0,0,1,0]])
# if there are direct between two state it can be one

