from environment import Environment
from agent import Agent

def playEpisode(enviro):
		enviro.newDeal()
		[agent.showHand() for agent in agents]

# start
while 1:
	try:
		numAgents = int(input('Number of poker playing agents: '))
	except: print 'Please enter a number'; continue
	break

enviro = Environment()
agents = [Agent() for x in range(numAgents)]
enviro.embedAgents(agents)

while 1:
		playEpisode(enviro)
		if raw_input('Enter q to quit: ') == 'q': break
		