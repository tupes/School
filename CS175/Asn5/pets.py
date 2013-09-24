# pets.py
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

def new_pet_object(class_type, name, timestamp, special_attribute_data):
	if class_type == "Fish":
		return Fish(name, timestamp, special_attribute_data)
	elif class_type == "Rodent":
		return Rodent(name, timestamp, special_attribute_data)
	elif class_type == "Bird":
		return Bird(name, timestamp, special_attribute_data)
	else:
		raise errors.PetError("Pet class not stocked by the pet store")


# Abstract base class for pet store pets
class Pet:
	"""Base class for petstore pet types."""
	def __init__(self, name, date_added):
		self.name = name
		self.attrition_rate = 1.00
		self.count = 0
		self._last_petcare = None
		self._date_added = date_added
		self.stock_received = 0
		self.stock_sold = 0
		self.stock_lost = 0
		self.on_order = 0

	def time_from_last_petcare(self):
		if not self._last_petcare:
			return "They have not been fed yet."
		else:
			now = timestamp.Timestamp()
			return now.difference(self._last_petcare)
	
	def petcare(self, event):
		assert type(event) == timestamp.Timestamp, "Incorrect event timestamp"
		self._last_petcare = event

	def add(self, amount):
		assert type(amount) is int and amount >= 0,\
				"Error - Invalid amount added; it must be a natural number."
		self.count += amount


class Fish(Pet):
	def __init__(self, name, date_added, special_attribute_data):
		super(Fish, self).__init__(name, date_added)
		self.attrition_rate = 0.1
		self.water_type = special_attribute_data.split('=')[1]

	def order_info(self):
		return 'water=' + self.water_type


class Rodent(Pet):
	def __init__(self, name, date_added, special_attribute_data):
		super(Rodent, self).__init__(name, date_added)
		self.attrition_rate = 0.05
		self.bedding_type = special_attribute_data.split('=')[1]

	def order_info(self):
		return 'bedding=' + self.bedding_type


class Bird(Pet):
	def __init__(self, name, date_added, special_attribute_data):
		super(Bird, self).__init__(name, date_added)
		self.attrition_rate = 0.02
		self.cage_type = special_attribute_data.split('=')[1]

	def order_info(self):
		return 'cage=' + self.cage_type

