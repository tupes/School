import sys
import matplotlib.pyplot as plt

step = float(sys.argv[1])
try: changes = int(sys.argv[2])
except: changes = 0
if 'i' in sys.argv: invert = True
else: invert = False

def newEstimate(old, target, step):
	print abs(target - est)
	return old + step * (target - old)

target = 1
iters = 6
est = 0

xs = []
ys = []
tys = []
for x in range(1, iters + 1):
	xs.append(x)
	tys.append(1)
	ys.append(est)
	est = newEstimate(est, target, step)
	if invert: step = 1 / float(x)

if changes > 0:
	# change target to 0
	target = 0
	for x in range(iters + 1, iters * 2 + 1):
		xs.append(x)
		tys.append(0)
		ys.append(est)
		est = newEstimate(est, target, step)
		if invert: step = 1 / float(x)

if changes > 1:
	# change target on every trial
	for x in range(iters * 2 + 1, iters * 3 + 1):
		if target == 0: target = 1
		else: target = 0
		xs.append(x)
		tys.append(target)
		ys.append(est)
		est = newEstimate(est, target, step)
		if invert: step = 1 / float(x)

f = open('step' + str(step) + 'results.dat', 'w')
for y in ys:
	f.write(str(y) + '\n')
f.close()

plt.plot(xs, ys)
plt.plot(xs, tys)
plt.show()

