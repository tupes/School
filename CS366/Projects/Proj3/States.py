import random

class State(object):
    def __init__(self, value=0.0, trace=0.0):
        self.value = value
        self.trace = trace
        self.actions = list()
    
    def get_best_action(self):
        best_action = self.actions[0]
        best_value = best_action.value
        for action in self.actions:
            if action.value > best_value:
                best_value = action.value
                best_action = action
        return best_action
    
    def get_random_action(self):
        return random.choice(self.actions)
    
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class FactoredState(State):
    def __init__(self, num_features, value=0.0):
        self.features = [0] * num_features
        self.value = value
    
    def get_value(self, values, coder):
        coder