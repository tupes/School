from Controllers import Sarsa, Default_Controller

class TDLearner(object):
    def __init__(self, enviro, gamma=1.0, alpha=1.0, epsil=0.0, controller='Sarsa'):      
        self.gamma = gamma
        self.alpha = alpha
        if controller == 'Sarsa': self.controller = Sarsa(enviro, alpha, epsil)
        else: self.controller = Default_Controller(enviro, alpha)
    
    def activate(self, num_episodes=150, num_runs=1):
        self.episodeAvgs = [0.0] * num_episodes
        for run in range(num_runs):
            self.do_run(num_episodes)
    
    def do_run(self, num_episodes):
        self.controller.init_values()
        for episode in range(num_episodes):
            self.do_episode()
    
    def do_episode(self):
        self.total_return = 0.0
        state = self.controller.get_init_state()
        action = self.controller.choose_action(state)
        while state != self.controller.enviro.terminal:
            state, action = self.do_action(state, action)

    def do_action(self, state, action):
        current_value, action, reward, next_state, valued_thing = self.controller.act(state, action)
        self.total_return += reward        
        next_value = self.get_value(next_state, valued_thing)
        error = reward + next_value - current_value
        self.learn(valued_thing, error)
        return next_state, action

    def get_value(self, state, valued_thing):
        if state == self.enviro.terminal: return 0
        return self.gamma * valued_thing.value
    
    def learn(self, valued_thing, error):
        valued_thing.value = self.update(valued_thing.value, error)

    def update(self, current_value, error, trace=1.0):
        return current_value + (self.alpha * error * trace)
    

    
class TDLambda(TDLearner):
    def __init__(self, enviro, gamma=1.0, alpha=1.0, epsil=0.0, controller='Sarsa', lam=0.0, neg=0.1):
        super(TDLambda, self).__init__(enviro, gamma, alpha, epsil, controller)        
        self.lam = lam
        self.negligible = neg
        self.eligible = set()
    
    def learn(self, valued_thing, error):
        valued_thing.trace += 1
        self.eligible.add(valued_thing)
        for thing in self.eligible:
            thing.value = self.update(thing.value, error, thing.trace)
            thing.trace = self.gamma * self.lam * thing.trace
            if thing.trace < self.negligible: self.eligible.remove(thing)
        