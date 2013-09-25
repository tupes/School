import random
from TileCoder import *

class Sarsa(object):
    def __init__(self, enviro, coder, alpha=1.0, epsilon=0.0, lam=0.0):      
        self.enviro = enviro
        self.coder = coder        
        self.alpha = alpha
        self.epsilon = epsilon
        self.lam = lam
        self.actions = [0, 1, 2]
        self.vector_length = self.coder.total_tiles * len(self.actions)
        self.weights = list()
        self.traces = list()
    
    def randomize_weights(self):
        self.weights = list()
        for i in range(self.vector_length):
            self.weights.append(random.uniform(0.0, -0.01))

    def activate(self, num_episodes=150, num_runs=1):
        self.episodeAvgs = [0.0] * num_episodes
        for run in range(num_runs):
            print 'starting a new run'
            self.do_run(num_episodes)

        for i in range(num_episodes):
            self.episodeAvgs[i] /= num_runs
    
    def do_run(self, num_episodes):
        self.randomize_weights()
        for episode in range(num_episodes):
            steps = self.do_episode()
            print 'number of steps:', steps
            self.episodeAvgs[episode] += steps
    
    def do_episode(self):
        self.traces = [0.0] * self.vector_length
        steps = 0
        state = self.enviro.init()
        action, value = self.choose_action(state)
        while state != self.enviro.terminal:
            steps += 1
            state, action = self.do_action(state, action)
        return steps

    def do_action(self, state, action):
        indices = self.coder.code(state, action)
        self.add_traces(indices)
        reward, new_state = self.take_action(state, action)
        error = reward - self.get_value(indices)
        next_action, next_value = self.choose_action(new_state)
        error += next_value
        self.learn(error)
        return new_state, next_action        

    def add_traces(self, indices):
        for i in indices:
            self.traces[i] += 1

    def take_action(self, state, action):
        new_state = self.enviro.transition(state, action)
        reward = self.enviro.reward(state, action, new_state)
        return reward, new_state
    
    def get_value(self, indices):
        returnVal = 0.0
        for i in indices:
            returnVal += self.weights[i]
        return returnVal

    def choose_action(self, state):
        if state == None: return None, 0.0
        if random.random() > self.epsilon:
            chosen_action, chosen_value = self.get_best_action(state)
        else:
            chosen_action = random.choice(self.actions)
            indices = self.coder.code(state, chosen_action)
            chosen_value = self.get_value(indices)
        return chosen_action, chosen_value

    def get_best_action(self, state):
        chosen_value = float('-infinity')
        for action in self.actions:
            indices = self.coder.code(state, action)
            this_value = self.get_value(indices)
            if this_value > chosen_value:
                chosen_value = this_value
                chosen_action = action
        return chosen_action, chosen_value

    def learn(self, error):
        for i in range(len(self.weights)):
            self.weights[i] += self.alpha * error * self.traces[i]
            self.traces[i] *= self.lam


def test_learning(coder):
    alpha = 0.1 / coder.numTilings
    sarsa = Sarsa(None, coder, alpha)
    tests = [(0.1, 0.1, 2.0), (4.0, 2.0, -1.0), (5.99, 5.99, 3.0), (4.0, 2.1, -1.0)]
    for test in tests:
        indices = coder.code(test[:2])
        sarsa.add_traces(indices)
        before = sarsa.get_value(indices)
        error = test[2] - before     
        sarsa.learn(error)
        after = sarsa.get_value(indices)
        print 'before:', before, ',', 'after:', after

if __name__ == '__main__':
    coder = TileCoder.test_tiling()
    test_learning(coder)