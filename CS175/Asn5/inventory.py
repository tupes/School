# inventory.py
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


import errors
import pets

class Inventory:
    """Inventory class. The data is stored in a dictionary. The keys will be
    the specific pet species, i.e. goldfish. The data will be the pet type
    object, i.e. fish. Once a species is added to inventory, it will never
    be removed even if current stock is zero.
    """
    def __init__(self):
        """Initializes an empty inventory object."""
        self._inventory = dict()
        
    def __iter__(self):
        return _InventoryIterator(self._inventory)
    
    def __contains__(self, item):
        if item in self._inventory:
            return True
        return False

    def add_new_pet_type(self, pet):
        """Add a new specific pet type to inventory (i.e. goldfish)."""
        if pet.name in self._inventory:
            raise errors.InventoryError("Pet type already in inventory")
        
        self._inventory[pet.name] = pet
        
    def order_stock(self, pet_type, amount):
        if pet_type not in self._inventory:
            raise errors.InventoryError("Pet not in inventory system")
        
        self._inventory[pet_type].on_order = amount
    
    def increase_stock(self, pet_type, amount):
        """Increase the current stock count for a given pet type."""
        if pet_type not in self._inventory:
            raise errors.InventoryError("Pet not in inventory system")

        self._inventory[pet_type].count += amount
        self._inventory[pet_type].stock_received += amount
        if self._inventory[pet_type].on_order < amount:
            self._inventory[pet_type].on_order = 0
        else:
            self._inventory[pet_type].on_order -= amount

    def decrease_stock(self, pet_type, amount):
        """Decrease the current stock levels for a given pet type."""
        if pet_type not in self._inventory:
            raise errors.InventoryError("Pet not in inventory system")
        if amount > self._inventory[pet_type].count:
            raise errors.InventoryError("Insufficient stock")

        self._inventory[pet_type].count -= amount
        self._inventory[pet_type].stock_sold += amount

    def write_off_stock(self, pet_type, amount):
        """Decreases the current stock levels for a given pet type to
        account for losses.
        """
        if pet_type not in self._inventory:
            raise errors.InventoryError("Pet not in inventory system")
        
        # Cannot loss more than the amount actually in stock
        if amount > self._inventory[pet_type].count:
            self._inventory[pet_type].stock_lost +=\
                    self._inventory[pet_type].count
            self._inventory[pet_type].count = 0
        else:
            self._inventory[pet_type].count -= amount
            self._inventory[pet_type].stock_lost += amount

        
class _InventoryIterator:
    def __init__(self, data):
        self._items = list()
        for key in data:
            self._items.append(data[key])
        self._current_item = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current_item < len(self._items):
            item = self._items[self._current_item]
            self._current_item += 1
            return item
        else:
            raise StopIteration

