import random
import collections


class Params(object):
    def __init__(self, protocol, num_stations, prob, num_slots, num_trials):
        self.protocol = protocol
        self.num_stations = num_stations
        self.prob = prob
        self.num_slots = num_slots
        self.num_trials = num_trials

class Station(object):
    def __init__(self, num_stations, prob, number):
        self.num_stations = num_stations
        self.prob = prob
        self.number = number
        self.frames_sent = 0
        self.delay = 0
        self.que = collections.deque()
        self.undelivered_ratios = []
        self.trial_frames_sent = []
        self.trial_delays = []
    
    def reset(self):
        self.que = collections.deque()
        self.frames_sent = 0
        self.delay = 0
    
    def do_slot(self, attempting):
        only_frame = False
        if get_random() < self.prob:
            only_frame = self.create_frame()
        for frame in range(len(self.que)):
            self.que[frame] += 1
        will_attempt = self.check_attempt(only_frame)
        if self.que and will_attempt:
            attempting.append(self)
        
    def create_frame(self):
        if self.que: only_frame = False
        else: only_frame = True
        self.que.append(0)
        return only_frame
    
    def check_attempt(self, not_needed):
        if self.counter:
            self.counter -= 1
            return False
        else:
            return True
    
    def transmit(self):
        next_frame_delay = self.get_frame()
        self.delay += next_frame_delay
        self.frames_sent += 1
        
    def get_frame(self):
        return self.que.popleft()
    
    def store_trial(self):
        self.trial_frames_sent.append(self.frames_sent)
        self.trial_delays.append(self.delay)
        undelivered = len(self.que)
        try:
            self.undelivered_ratios.append(undelivered / float(undelivered + self.frames_sent))
        except ZeroDivisionError:
            self.undelivered_ratios.append(0.0)
    
    def get_throughput(self, total_slots):
        self.throughput = sum(self.trial_frames_sent) / float(total_slots)
    
    def get_delay(self):
        try:
            self.avg_delay = sum(self.delay) / float(self.frames_sent)
        except ZeroDivisionError: 
            self.avg_delay = 0.0
    
    def get_results(self, total_slots):
        total_frames = sum(self.trial_frames_sent)
        throughput = total_frames / float(total_slots)
        try:
            avg_delay = sum(self.trial_delays) / float(total_frames)
        except ZeroDivisionError: 
            avg_delay = 0.0
        return concat_seq([str(result) for result in [self.number, throughput, avg_delay, concat_seq(self.undelivered_ratios)]])
        
    
class P_Station(Station):
    def __init__(self, num_stations, prob, number):
        Station.__init__(self, num_stations, prob, number)
        
    def check_attempt(self, only_frame):
        if only_frame or get_random() < 1 / float(self.num_stations): 
            return True
        else: 
            return False
    
    def collide(self):
        return

class I_Station(Station):
    def __init__(self, num_stations, prob, number):
        Station.__init__(self, num_stations, prob, number)
        self.counter = 0

    def reset(self):
        Station.reset(self)
        self.counter = 0

    def collide(self):
        self.counter = random.randint(0, self.num_stations - 1)
    
class B_Station(Station):
    def __init__(self, num_stations, prob, number):
        Station.__init__(self, num_stations, prob, number)
        self.counter = 0
        self.collisions = 0

    def reset(self):
        Station.reset(self)
        self.counter = 0
        self.collisions = 0
            
    def collide(self):
        if self.collisions < 10: self.collisions += 1
        self.counter = random.randint(0, (2 ** self.collisions) - 1)
    
    def transmit(self):
        Station.transmit(self)
        self.collisions = 0

class T_Station(Station):
    def __init__(self, num_stations, prob, number):
        Station.__init__(self, num_stations, prob, number)
        self.counter = number
    
    def reset(self):
        Station.reset(self)
        self.counter = self.number

    def check_attempt(self, not_needed):
        if self.counter:
            self.counter -= 1
            return False
        else:
            self.counter = self.num_stations - 1
            return True    


# start
def run(protocol, num_stations, prob, num_slots, num_trials, seeds):
    params = Params(protocol, num_stations, prob, num_slots, num_trials)
    if protocol == 'P':
        stations = [P_Station(num_stations, prob, n) for n in range(num_stations)]
    elif protocol == 'I':
        stations = [I_Station(num_stations, prob, n) for n in range(num_stations)]
    elif protocol == 'B':
        stations = [B_Station(num_stations, prob, n) for n in range(num_stations)]
    elif protocol == 'T':
        stations = [T_Station(num_stations, prob, n) for n in range(num_stations)]
    else:
        print 'unknown protocol'
        exit()
    for trial in range(num_trials):
        run_trial(stations, params, seeds[trial])
        store_trial(stations)
    return stations

def run_trial(stations, params, seed):
    random.seed(seed)
    for station in stations: station.reset()
    for slot in range(params.num_slots):
        attempting = list()
        for station in stations:
            station.do_slot(attempting)
        transmit(attempting)

def transmit(attempting):
    tries = len(attempting)
    if not tries: return
    elif tries == 1: attempting[0].transmit()
    else:
        for station in attempting:
            try:
                station.collide()
            except AttributeError:
                print 'num stations:', tries, ', this:', station.number 

def store_trial(stations):
    for station in stations: station.store_trial()

def get_random():
    return random.random()

def concat_seq(seq):
    return ' '.join([str(item) for item in seq])