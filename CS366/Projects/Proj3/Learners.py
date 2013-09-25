from tilecoder import TileCoder

class LinearLearner(object):
    def __init__(self, alpha, coder):
        self.alpha = alpha
        self.coder = coder
        self.weights = [0.0] * self.coder.total_tiles
        print len(self.weights)        
        #self.numWeights = len(self.weights)
    
    def ask(self, x_vals):
        self.coder.code(x_vals)
        returnVal = 0.0
        for i in self.coder.indices:
            returnVal += self.weights[i]
        return returnVal
    
    def learn(self, x_vals, y):
        weightChange = self.alpha * (y - self.ask(x_vals))
        for i in self.coder.indices:
            self.weights[i] += weightChange


def test1(learner):
    tests = [(0.1, 0.1, 2.0), (4.0, 2.0, -1.0), (5.99, 5.99, 3.0), (4.0, 2.1, -1.0)]
    for test in tests:    
        before = learner.ask(test[:2])
        learner.learn(test[:2], test[2])
        after = learner.ask(test[:2])
        print 'before:', before, ',', 'after:', after

if __name__ == '__main__':
    bounds = (0, 6)
    numTilings = 8
    length = 11
    coder = TileCoder(bounds, bounds, numTilings, length)
    alpha = 0.1 / numTilings
    learner = LinearLearner(alpha, coder)
    test1(learner)