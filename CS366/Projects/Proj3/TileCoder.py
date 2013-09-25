import math

class TileCoder(object):
    def __init__(self, x1_bounds, x2_bounds, numTilings=4, length=9):
        self.numTilings = numTilings
        self.length = length
        self.numTiles = length * length
        self.total_tiles = self.numTiles * self.numTilings
        self.offset = -1.0 / numTilings
        self.x1_range = x1_bounds[1] - x1_bounds[0]
        self.x2_range = x2_bounds[1] - x2_bounds[0]        
    
    def code(self, x_values, multiplier=0):
        indices = [0] * self.numTilings      
        base = 0
        standX1 = (x_values[0] / self.x1_range) * (self.length - 1)
        standX2 = (x_values[1] / self.x2_range) * (self.length - 1)
        
        for i in range(self.numTilings):
            tileNumX1 = int(math.floor(standX1 - base))
            tileNumX2 = int(math.floor(standX2 - base) * self.length)
            tileNum = tileNumX1 + tileNumX2
            indices[i] = tileNum + (i * self.numTiles) + (multiplier * self.total_tiles)
            base += self.offset
        return indices


def test_tiling():
    bounds = (0, 6)
    numTilings = 8
    length = 11
    coder = TileCoder(bounds, bounds, numTilings, length)
    tests = [(0.1, 0.1), (4.0, 2.0), (5.99, 5.99), (4.0, 2.1)]
    for test in tests:
        print coder.code(test)
    return coder