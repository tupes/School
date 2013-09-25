import random
import math

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
        self.averages = list()
    
    def randomize_weights(self):
        self.weights = list()
        for i in range(self.vector_length):
            self.weights.append(random.uniform(0.0, -0.01))
    
    def init_run(self):
        self.randomize_weights()
        self.results = list()

    def init_episode(self):
        self.traces = [0.0] * self.vector_length
        self.steps = 0
        self.total_return = 0.0

    def activate(self, num_episodes=150, num_runs=1):
        self.episodeAvgs = [0.0] * num_episodes
        scores = list()
        for run in range(num_runs):
            print 'starting a new run'
            scores.append(self.do_run(num_episodes))
            #avg = sum(self.results) / float(len(self.results))
            #print 'average number of steps:', avg
            #self.averages.append(avg)
        #final = sum(self.averages) / float(len(self.averages))
        mean_performance =  sum(scores) / float(num_runs)       
        print 'mean_performance:', mean_performance
        if num_runs == 1:
            standard_error = 0.0
        else:
            standard_error = calc_standard_error(mean_performance, scores)
        #for i in range(num_episodes):
            #self.episodeAvgs[i] /= num_runs
        #return self.episodeAvgs
        return mean_performance, standard_error
    
    def do_run(self, num_episodes):
        self.init_run()
        score = 0
        for episode in range(num_episodes):
            steps = self.do_episode()
            #print 'number of steps:', self.steps
            print 'number of steps:', steps
            score += steps
            #self.results.append(self.steps)
            #self.episodeAvgs[episode] += self.steps
        return score
    
    def do_episode(self):
        self.init_episode()
        steps = 0
        state = self.enviro.init()
        action, value = self.choose_action(state)
        while state != self.enviro.terminal:
            #self.steps += 1
            steps += 1
            state, action = self.do_action(state, action)
        return steps

    def do_action(self, state, action):
        indices = self.coder.code(state, action)
        self.add_traces(indices)
        reward, new_state = self.take_action(state, action)
        self.total_return += reward
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
        

class TileCoder(object):
    def __init__(self, x1_bounds, x2_bounds, numTilings=4, length=9, numDims=2):
        self.numTilings = numTilings
        self.numDims = numDims
        self.length = length
        self.numTiles = length * length
        self.total_tiles = self.numTiles * self.numTilings
        self.offset = -1.0 / numTilings
        self.x1_range = x1_bounds[1] - x1_bounds[0]
        self.x2_range = x2_bounds[1] - x2_bounds[0]        
    
    def code(self, x_values, multiplier=0):
        indices = [0] * self.numTilings      
        base = 0
        standX1 = (x_values[0] / self.x1_range) * (self.length - 1)
        standX2 = (x_values[1] / self.x2_range) * (self.length - 1)
        
        for i in range(self.numTilings):
            tileNumX1 = int(math.floor(standX1 - base))
            tileNumX2 = int(math.floor(standX2 - base) * self.length)
            tileNum = tileNumX1 + tileNumX2
            indices[i] = tileNum + (i * self.numTiles) + (multiplier * self.total_tiles)
            base += self.offset
        return indices


def calc_standard_error(mean, scores):
    errors = list()
    for score in scores:
        error = mean - score
        errors.append(error ** 2)
    mse = sum(errors) / len(errors)
    stdev = math.sqrt(mse)
    #if len(scores) == 1: return stdev
    return stdev / math.sqrt(len(scores) - 1)

def test_tiling():
    bounds = (0, 6)
    numTilings = 8
    length = 11
    coder = TileCoder(bounds, bounds, numTilings, length)
    tests = [(0.1, 0.1), (4.0, 2.0), (5.99, 5.99), (4.0, 2.1)]
    for test in tests:
        print coder.code(test)
    return coder

def test_learning(coder):
    alpha = 0.1 / coder.numTilings
    sarsa = Sarsa(None, coder, alpha)
    tests = [(0.1, 0.1, 2.0), (4.0, 2.0, -1.0), (5.99, 5.99, 3.0), (4.0, 2.1, -1.0)]
    for test in tests:
        indices = coder.code(test[:2])
        sarsa.add_traces(indices)
        before = sarsa.get_value(indices)
        error = test[2] - before
        #error = before - test[2]        
        sarsa.learn(error)
        after = sarsa.get_value(indices)
        print 'before:', before, ',', 'after:', after

if __name__ == '__main__':
    coder = test_tiling()
    test_learning(coder)