

class Agent(object):
		def __init__(self):
			pass
		
		def showHand(self):
			print self.hand.cards[0].rank + self.hand.cards[0].suit, self.hand.cards[1].rank + self.hand.cards[1].suit  