import math

class TileCoder(object):
    def __init__(self, x1_bounds, x2_bounds, numTilings=4, length=9, numDims=2):
        self.numTilings = numTilings
        self.numDims = numDims
        self.length = length
        self.numTiles = length * length
        self.total_tiles = self.numTiles * self.numTilings
        self.offset = -1.0 / numTilings
        self.max_x1 = x1_bounds[1]
        self.max_x2 = x2_bounds[1]
        self.reset()
        #self.x1 = lengths[0]
        #self.x2 = lengths[1]
    
    def reset(self):
        self.indices = [0] * self.numTilings
    
    def code(self, x_values):
        self.reset()        
        base = 0
        standX1 = (x_values[0] / self.max_x1) * (self.length - 1)
        standX2 = (x_values[1] / self.max_x2) * (self.length - 1)
        
        for i in range(self.numTilings):
            tileNumX1 = int(math.floor(standX1 - base))
            tileNumX2 = int(math.floor(standX2 - base) * self.length)
            tileNum = tileNumX1 + tileNumX2
            self.indices[i] = tileNum + (i * self.numTiles)
            base += self.offset


if __name__ == '__main__':
    bounds = (0, 6)
    numTilings = 8
    length = 11
    coder = TileCoder(bounds, bounds, numTilings, length)
    tests = [(0.1, 0.1), (4.0, 2.0), (5.99, 5.99), (4.0, 2.1)]
    for test in tests:
        coder.code(test)
        print coder.indices