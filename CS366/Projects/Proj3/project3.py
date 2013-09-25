from Sarsa import Sarsa 
from TileCoder import TileCoder
import MountainCar

def write_results(avgs):
    f = open('results.txt', 'w')
    for avg in avgs:
        f.write(str(avg) + '\n')
    f.close()

def write_row(row, f):
    for value in row:
        f.write(str(value) + ',')
    f.write('\n')

def objective_func(eps, runs=1, numTilings=4, length=9, alpha_init=0.05, epsilon=0.0, lam=0.9):
    position_bounds = (-1.2, 0.5)
    vel_bounds = (-0.07, 0.07)
    coder = TileCoder(position_bounds, vel_bounds, numTilings, length)
    alpha = alpha_init / coder.numTilings
    sarsa = Sarsa(MountainCar, coder, alpha, epsilon, lam)
    sarsa.activate(eps, runs)
    return sarsa

def create_learning_curve():
    sarsa = objective_func(150, 50)
    write_results(sarsa.episodeAvgs)

def create_matrix():
    sarsa = objective_func(200)
    pos_step = 0.034
    vel_step = 0.0028
    pos_min = -1.2 - pos_step
    vel_min = -0.07 - vel_step
    chunks = 50
    f = open('matrix.csv', 'w')
    
    pos = pos_min
    for p in range(chunks):
        vel = vel_min
        pos += pos_step
        row = list()
        for v in range(chunks):
            vel += vel_step
            state = [pos, vel]
            junk, value = sarsa.get_best_action(state)
            row.append(value * -1)
        write_row(row, f)
    
    f.close()
