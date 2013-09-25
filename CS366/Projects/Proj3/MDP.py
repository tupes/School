import random

class MDP(object):
    def __init__(self):
        pass

class Party(MDP):
    def __init__(self):
        state_names = ['RU_8p', 'TU_10p', 'RU_10p', 'RD_10p', 'RU_8a', 'RD_8a', 'TU_10a', 
                   'RU_10a', 'RD_10a', 'TD_10a']
        num_actions = [3, 2, 3, 2, 3, 2, 3, 3, 3, 3]
        transitions = [trans1, trans2, trans3, trans4, trans5, trans6, trans7, trans8, trans9, trans10]
        self.states = dict()
        for x in range(len(state_names)):
            self.states[state_names[x]] = State(state_names[x], num_actions[x], transitions[x])

class State(object):
    def __init__(self, name, num_actions):
        self.name = name
        self.num_actions = num_actions