import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['c', 'd', 'h', 's']

class Environment(object):
		def __init__(self):
			self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
		
		def embedAgents(self, agents):
			self.agents = agents
		
		def newDeal(self):
			self.round = 1
			self.deck = self.cards[:]
			for agent in self.agents:
				agent.hand = Hand()
				self.dealHand(agent)
		
		def dealHand(self, agent):
			agent.hand.addCard(self.drawCard())
			agent.hand.addCard(self.drawCard())
		
		def newRound(self):
			self.round += 1
			self.board.append(self.drawCard())
			if self.round < 3:
				self.board.append(self.drawCard())
				self.board.append(self.drawCard())
		
		def drawCard(self):
			card = random.choice(self.deck)
			self.deck.remove(card)
			return card

class Hand(object):
		def __init__(self):
			self.cards = []
		
		def addCard(self, card):
			self.cards.append(card)

class Card(object):
		def __init__(self, rank, suit):
			self.rank = rank
			self.suit = suit
			self.ordinal = self.convRank()
		
		def convRank(self):
			try:
				return int(self.rank) - 1
			except:
				if self.rank == 'T': return 9
				elif self.rank == 'J': return 10
				elif self.rank == 'Q': return 11
				elif self.rank == 'K': return 12
				elif self.rank == 'A': return 13
				else:
					print 'Unknown card type'
					raise 
		