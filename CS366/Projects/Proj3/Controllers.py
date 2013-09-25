import random
from Learners import LinearLearner

class Controller(object):

    def get_init_state(self):
        return self.enviro.init()

    def take_action(self, state, action):
        next_state = self.enviro.transition(state, action)
        reward = self.enviro.reward(state, action, next_state)
        return reward, next_state

class Sarsa(Controller):
    def __init__(self, enviro, alpha, epsilon, state_type='table'):
        self.enviro = enviro
        self.alpha = alpha
        self.epsilon = epsilon
        self.state_type = state_type
    
    def assign_learner(self, coder, learner_type='linear'):
        if learner_type == 'linear':
            self.learner = LinearLearner(self.alpha, coder) 
    
    def init_values(self):
        pass
    
    def act(self, state, action):
        reward, next_state = self.take_action(state, action)        
        next_action = self.choose_action(next_state)
        return action.value, next_action, reward, next_state, next_action
    
    def choose_action(self, state):
        if random.random() > self.epsilon:
            return state.get_best_action()
        else:
            return state.get_random_action()

class Default_Controller(Controller):
    def __init__(self, enviro, epsilon=0.0):
        self.enviro = enviro
        self.epsilon = epsilon
        self.policy = None
    
    def init_values(self):
        pass
        
    def act(self, state, action):
        # only accepts action to make it consistent with Sarsa
        action = self.choose_action(state)
        reward, next_state = self.take_action(state, action)
        return state.value, action, reward, next_state, next_state
    
    def choose_action(self, state):
        if self.policy: return self.policy(state)
        else: return state.get_random_action()