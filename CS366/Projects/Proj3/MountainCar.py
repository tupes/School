import random
import math

terminal = None

def init():
    return random.uniform(-0.6, -0.4), 0.0

def numActions(s):
    return 3

def reward(s1, a, s2):
    return -1.0

def transition(state, action):
    assert len(state) == 2
    action -= 1
    assert action in {-1, 0, 1}
    
    new_pos = state[0] + state[1]
    if new_pos >= 0.5: return terminal
    elif new_pos >= -1.2:
        return [new_pos, 
                max(min(state[1] + 0.001 * action + -0.0025 * math.cos(3 * state[0]),
                  0.07), -0.07)]
    else:
        return [-1.2, 0.0]

