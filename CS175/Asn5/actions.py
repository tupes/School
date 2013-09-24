# actions.py
#
# Copyright 2011 by Barry Gergel.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.
#
# Created:		Barry Gergel <gergel@ualberta.ca>
# Modified by Mark Tupala

import timestamp
import errors
import random
import inventory
import pets
import sys

class ActionID:
	"""Static class for generating ID values."""
	_action_id = 0

	@staticmethod
	def set_id(value):
		ActionID._action_id = value
	
	@staticmethod
	def next():
		ActionID._action_id += 1
		return ActionID._action_id

class Action:
	"""Abstract class to capture a business action process. These objects
	are immutable.
	"""
	def __init__(self):
		self.id = ActionID.next()
		self.name = "Action"
		self.data = None
		self.result = None
		self.timestamp = timestamp.Timestamp('1492-01-01T00:00:00')

	def do_action(self, event_data, inventory):
		# The result tuple is structure as follows:
		#   SUCCESS: ('SUCCESS',)
		#   SUCCESSWITHEVENTS: ('SUCCESSWITHEVENTS', raw_event_data)
		#   FAIL: ('FAIL', error_message)
		#   FAILWITHEVENTS: ('FAILWITHEVENTS', error_message, raw_event_data)
		# raw_event_data must always be returned as a list, even if it is only
		# a single event
		return('FAIL','Base action - does nothing')

	def parse_event(self, event_data, inventory):
		assert len(event_data) == 4
		assert event_data[2] in inventory
		return event_data[2], int(event_data[3])

	def get_date(self):
		return self.timestamp.date()

	def get_time(self):
		return self.timestamp.time()

	def __str__(self):
		return str(self.id) + ":" + self.name + ":" + str(self.result) +\
				":" + str(self.data) + ":" + str(self.timestamp)


class EndOfDayAction(Action):
	# Event data structure: [<timestamp>,'EndOfDay']
	def __init__(self):
		super().__init__()
		self.name = "EndOfDayAction"
	
	def do_action(self, event_data, inventory): 
		self.timestamp = timestamp.Timestamp(event_data[0])

		# Check for random pet deaths
		deaths = list()
		for item in inventory:
			chance = random.random()
			if chance <= item.attrition_rate and item.count > 0:
				try:
					amount = random.randrange(1, (item.count // 2))
				except ValueError:
					amount = 1
				event = str(self.timestamp) + "|" + "PetLoss" +\
					  "|" + item.name + "|" + str(amount)
				deaths.append(event)
		
		if len(deaths) > 0:
			self.result = ("SUCCESSWITHEVENTS", deaths)
		else:
			self.result = ("SUCCESS",)


class OrderStockAction(Action):
	# Event data structure:
	#     [<timestamp>,'OrderStock',<pet class>,<pet type/name>,
	#        <special attribute>,<amount>]
	# Ex. ['2011-11-19T09:54:01','OrderStock','Fish','Goldfish',
	#        'water=fresh', 100]
	
	def __init__(self):
		super().__init__()
		self.name = "OrderStockAction"
	
	def do_action(self, event_data, inventory):
		try:
			inventory.order_stock(event_data[3], int(event_data[5]))
		except errors.InventoryError:
			try:
				new_pet = pets.new_pet_object(event_data[2], event_data[3],\
											  event_data[0], event_data[4])
			except errors.PetError:
				self.result = ("FAIL", sys.exc_info()[1])
				return
			
			inventory.add_new_pet_type(new_pet)
			inventory.order_stock(event_data[3], int(event_data[5]))
		
		self.result = ("SUCCESS",)


class PetCareAction(Action):
	# Event data structure:
	#     [<timestamp>,'PetCare',<pet type/name>]
	# Ex. ['2011-11-21T17:12:01','PetCare','Goldfish']
	def __init__(self):
		super().__init__()
		self.name = "PetCareAction"
	
	def do_action(self, event_data, inventory):
		time = timestamp.Timestamp(event_data[0])
		try:
			pet = inventory._inventory[event_data[2]]
			pet.petcare(time)
			self.result = ("SUCCESS",)
		except:
			self.result("FAIL", sys.exc_info()[1])


class PetLossAction(Action):
	# Event data structure:
	#     [<timestamp>,'PetLoss',<pet type/name>, <amount>]
	# Ex. ['2011-11-21T23:59:59','PetLoss','Goldfish',5]
	def __init__(self):
		super().__init__()
		self.name = "PetLossAction"
	
	def do_action(self, event_data, inventory):
		try:
			species, amount = self.parse_event(event_data, inventory)
			inventory.write_off_stock(species, amount)
			self.result = ("SUCCESS",)
		except:
			self.result("FAIL", sys.exc_info()[1])


class ReceiveAction(Action):
	# Event data structure: 
	#     [<timestamp>,'Receive',<pet type/name>,<amount>]
	# Ex. ['2011-11-20T10:23:32','Receive','Goldfish',100]
	def __init__(self):
		super().__init__()
		self.name = "ReceiveAction"
	
	def do_action(self, event_data, inventory):
		try:
			species, amount = self.parse_event(event_data, inventory)
			inventory.increase_stock(species, amount)
			self.result = ("SUCCESS",)
		except:
			self.result("FAIL", sys.exc_info()[1])


class SaleAction(Action):
	# Event data structure:
	#     [<timestamp>,'Sale',<pet type/name>,<amount>]
	# Ex. ['2011-11-21T12:10:03','Sale','Goldfish',100]
	def __init__(self):
		super().__init__()
		self.name = "SaleAction"
	
	def do_action(self, event_data, inventory):
		try:
			species, amount = self.parse_event(event_data, inventory)
		except:
			self.result("FAIL", sys.exc_info()[1])
			return
		pet = inventory._inventory[species]
		try:
			inventory.decrease_stock(species, amount)
			if pet.count == 0:
				order = self.place_order(pet, event_data[0])
				self.result = ("SUCCESSWITHEVENTS", order)
			else:
				self.result = ("SUCCESS",)
		except errors.InventoryError:
			inventory.decrease_stock(species, pet.count)
			order = self.place_order(pet, event_data[0])
			self.result = ("FAILWITHEVENTS", 'Insufficient Stock', order)

	def place_order(self, pet, time_string):
		self.timestamp = timestamp.Timestamp(time_string)
		order = str(self.timestamp) + "|" + "OrderStock" + "|" +\
			str(pet.__class__) + "|" + pet.name + "|" +\
			pet.order_info() + "|" + str(50)
		return [order]
