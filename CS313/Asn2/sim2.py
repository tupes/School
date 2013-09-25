import random
import collections

class Params(object):
    def __init__(self, protocol, num_stations, prob, num_slots, num_trials):
        self.protocol = protocol
        self.num_stations = num_stations
        self.prob = prob
        self.num_slots = num_slots
        self.num_trials = num_trials

class Frame(object):
    def __init__(self):
        self.delay = 1
        self.blocked = False

class Station(object):
    def __init__(self, number, prob):
        self.number = number
        self.prob = prob
        self.frames_sent = 0
        self.delay = 0
        self.que = collections.deque()
    
    def do_slot(self, attempting):
        if get_random() < self.prob:
            self.create_frame()
        for frame in self.que:
            frame.delay += 1
        if self.que:
            self.use_protocol()
        
    def create_frame(self):
        self.que.append(Frame())
    
    def transmit(self):
        if self.que:
            next_frame = self.get_frame()
            self.delay += next_frame.delay
            self.frames_sent += 1
    
    def get_frame(self):
        return self.que.popleft()

class T_Station(Station):
    def __init__(self, number, prob):
        super(T_Station, self).__init__(number, prob)
    

# start
def run(protocol, num_stations, prob, num_slots, num_trials):
    params = Params(protocol, num_stations, prob, num_slots, num_trials)
    stations = [Station(n, prob) for n in range(num_stations)]
    for trial in range(num_trials):
        run_trial(stations, params)
        store_results(stations)
    produce_results(stations, params)
    return stations

def run_trial(stations, params):
    if params.protocol == 'T':
        run_time_trial(stations, params)
    else:
        run_aloha_trial(stations, params)

def run_time_trial(stations, params):
    i = 0
    for slot in range(params.num_slots):
        attempting = list()
        for station in stations:
            station.do_slot(attempting)
        stations[i].transmit()
        i += 1
        if i >= params.num_stations: i = 0

def run_aloha_trial(stations, params):
    for slot in range(params.num_slots):
        attempting = list()
        for station in stations:
            station.do_slot(attempting)
        transmit(stations, attempting)

def transmit(attempting):
    tries = len(attempting)
    if not tries: return
    elif tries == 1: attempting[0].transmit()
    else:
        for station in attempting:
            station.collide()

def store_results(stations):
    print 'storing results not implemented'

def produce_results(stations, params):
    print 'producing results not implemented'

def get_random():
    return random.random()