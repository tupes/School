import operator
import datetime
import random
#from start import objective_func
from Sarsa import Sarsa, TileCoder
import MountainCar

path = 'F:/school/cs/366/projects/proj3/'

class Optimizer(object):
    def __init__(self, func, num_members, params, better='min', prototype=None):
        self.func = func
        self.num_members = num_members
        self.members = list()
        self.params = params
        self.best_member = prototype
        self.best_score = float('infinity')
        self.num_runs = 50
        self.results = open(path + 'winners_performance.txt', 'w')
        if better == 'min': self.compare = operator.lt
        else: self.compare = operator.gt
    
    def record_result(self, member):
        self.results.write('\n' + 'Winner:' + str(member.score) + ', ' + str(member.error) +  '\n')
        self.results.write('Number tilings:' + str(member.params['numTilings'].value) + '\n')
        self.results.write('Tile size:' + str(member.params['length'].value) + '\n')
        self.results.write('alpha:' + str(member.params['alpha'].value) + '\n')
        self.results.write('epsilon:' + str(member.params['epsilon'].value) + '\n')
        self.results.write('lambda:' + str(member.params['lambda'].value) + '\n')
        self.results.flush()

    
    def set_terminate_condition(self, kind, termination):
        if kind == 'time':
            self.terminate_condition = self.check_duration
            self.timer = datetime.datetime
            self.start_time = self.timer.now()
        elif kind == 'generations':
            self.terminate_condition = self.check_generation
        elif kind == 'performance':
            pass
        self.termination = termination
    
    def check_duration(self):
        current_time = self.timer.now()
        duration = current_time - self.start_time
        if duration.seconds / 3600.0 > self.termination:
            return True
        else:
            return False
        
    def activate(self):
        self.set_terminate_condition('time', 2)
        self.init_members()
        print 'starting first generation'
        self.run_first_generation()
        self.insertion_sort()
        print 'starting second generation'
        self.run_second_generation()
        self.insertion_sort()
        print 'starting iterative generations'
        while not self.terminate_condition():
            self.run_generation()
            #self.check_contender()
            self.insertion_sort()
    
    def init_members(self):
        for n in range(self.num_members):
            member = Member(self.params)
            self.members.append(member)
    
    def run_first_generation(self):
        for i in range(len(self.members)):
            self.members[i].mutate(i / self.num_members)
            self.evaluate(self.members[i], 1)
    
    def run_second_generation(self):
        for i in range(len(self.members[:10])):
            self.members[i].mutate(i / self.num_members)
            self.evaluate(self.members[i], 5)
        
        for i in range(len(self.members[10:])):
            self.members[i].mutate(i / self.num_members)
            self.evaluate(self.members[i], 1)
    
    def run_generation(self):
        self.evaluate_best()
    
        for i in range(len(self.members[1:10])):
            self.members[i].mutate(i / self.num_members)
            self.evaluate(self.members[i], 5)
        
        for i in range(len(self.members[10:])):
            self.members[i].mutate(i / self.num_members)
            self.evaluate(self.members[i], 1)    
    
    def insertion_sort(self):
        new_list = [self.members[0]]
        #is_best_same = True
        for member in self.members[1:]:
            #if member.value < new_list[0].value:
                #new_list.insert(0, member)
                #is_best_same = False
                #continue
            i = len(new_list)
            while 1:
                if i == 0: 
                    new_list.insert(0, member)
                    break
                elif member.score > new_list[i-1].score:
                    new_list.insert(i, member)
                    break
                i -= 1
            
        self.members = new_list
    
    def evaluate_best(self):
        member = self.members[0]
        member.score, member.error = self.func(member.params, self.num_runs)
        self.record_result(member)
        #if member.same_best:
            #member.runs += self.num_runs
            #member.scores.append(score)
        #else:
            #member.runs = self.num_runs
            #self.scores = [score]
            
    
    def evaluate(self, member, runs):
        score, error = self.func(member.params, runs)
        member.score = score
        if score < self.best_score:
            self.best_score = score
            self.best_member = member
        return score
    
    #def set_baseline(self, runs=50):
        #self.baseline = self.evaluate(self.best_member, runs)


class Member(object):
    def __init__(self, params):
        self.score = 0.0
        self.score = 0.0
        self.params = params
        #self.rank = None
    
    def mutate(self, rank):
        for param in self.params.values():
            param.modify(rank)


class Param(object):
    def __init__(self, name, max_change, data_type='float', default=None, minimum=float('-infinity'), maximum=float('infinity')):
        self.name = name
        self.type = data_type
        self.value = default
        self.min = minimum
        self.max = maximum
        if data_type == 'float': 
            self.modify = self.modify_float
            self.max_sigma = max_change
        else: 
            self.modify = self.modify_int
            self.max_steps = max_change
    
    def modify_float(self, rank):
        sigma = rank * self.max_sigma
        new_value = None
        print 'mutating float'
        while not self.min <= new_value <= self.max:
            new_value = random.gauss(self.value, sigma); #print new_value
        print 'finished mutating float'
        self.value = new_value
    
    def modify_int(self, rank):
        steps = int(rank * self.max_steps)
        new_value = None
        while not self.min < new_value < self.max:
            if random.random() > 0.5: new_value = self.value + steps
            else: new_value = self.value - steps
        self.value = new_value


def objective_func(params, runs):
    position_bounds = (-1.2, 0.5)
    vel_bounds = (-0.07, 0.07)
    coder = TileCoder(position_bounds, vel_bounds, params['numTilings'].value, params['length'].value)
    alpha = params['alpha'].value / coder.numTilings
    print 'activating sarsa'
    sarsa = Sarsa(MountainCar, coder, alpha, params['epsilon'].value, params['lambda'].value)
    mean_performance, standard_error = sarsa.activate(150, runs)
    return mean_performance, standard_error



def proj3():
    print 'starting project'
    params = dict()
    params['numTilings'] = Param('numTilings', 10, 'int', 4, 2)
    params['length'] = Param('length', 10, 'int', 9, 2)
    params['lambda'] = Param('lambda', 0.1, 'float', 0.9, 0.0, 0.99)
    params['alpha'] = Param('alpha', 0.001, 'float', 0.05, 0.0, 0.1)
    params['epsilon'] = Param('epsilon', 0.1, 'float', 0.0, 0.0, 0.9)
    #original = Member(params)
    opt = Optimizer(objective_func, 20, params)
    print 'activating optimizer'
    opt.activate()
    opt.results.close()
    print 'finished'

if __name__ == '__main__':
    proj3()