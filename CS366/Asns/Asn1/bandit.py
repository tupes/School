import sys
import random

arms = int(sys.argv[1])

def bandit(a):
	return random.randint(-10, 10)

def newEstimate(old, target, trials):
	return old + (1.0 / trials) * (target - old)

actions = [0] * arms	
k = 1
while 1:
	print 'actions:', actions
	a = actions.index(max(actions))
	print 'choosing', a
	reward = bandit(a)
	print 'reward', reward
	actions[a] = newEstimate(actions[a], reward, k)
	k += 1
	if raw_input('Continue: (q to quit) ') == 'q': break
	