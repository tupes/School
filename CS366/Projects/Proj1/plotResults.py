import matplotlib.pyplot as plt

f = open('outResults.txt')
lines = f.readlines()
f.close()

ys = list()
for line in lines:
	ys.append(float(line.rstrip()))

xs = range(1000)

plt.plot(xs, ys)
plt.xlabel('Episode')
plt.ylabel('Average Return')
plt.title('Sarsa Average Return by Episode')
plt.show()