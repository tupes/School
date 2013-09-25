from Sarsa import Sarsa, TileCoder
import MountainCar


path = 'F:/school/cs/366/projects/proj3/'

def write_results(avgs):
    f = open(path + 'results.txt', 'w')
    for avg in avgs:
        f.write(str(avg) + '\n')
    f.close()

def write_row(row, f):
    for value in row:
        f.write(str(value) + ',')
    f.write('\n')

def write_target(mean_performance, standard_error, runs):
    f = open(path + 'baseline_performance.txt', 'w')
    f.write('Original parameters performance\n')
    f.write('Mean performance: ' + str(mean_performance) + '\n')
    f.write('Standard error: ' + str(standard_error) + '\n')
    f.write('Number of runs: ' + str(runs) + '\n')
    f.close()

def objective_func(eps, runs=1, numTilings=4, length=9, alpha_init=0.05, epsilon=0.0, lam=0.9):
    position_bounds = (-1.2, 0.5)
    vel_bounds = (-0.07, 0.07)
    coder = TileCoder(position_bounds, vel_bounds, numTilings, length)
    alpha = alpha_init / coder.numTilings
    sarsa = Sarsa(MountainCar, coder, alpha, epsilon, lam)
    mean_performance, standard_error = sarsa.activate(eps, runs)
    write_target(mean_performance, standard_error, runs)
    #write_results(episode_avgs)
    #return sarsa
    #return sum(episode_avgs)

def create_matrix():
    sarsa = objective_func(200)
    pos_step = 0.034
    vel_step = 0.0028
    pos_min = -1.2 - pos_step
    vel_min = -0.07 - vel_step
    chunks = 50
    f = open(path + 'matrix.csv', 'w')
    
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
        


if __name__ == '__main__':
    objective_func(150, 50)
    #create_matrix()