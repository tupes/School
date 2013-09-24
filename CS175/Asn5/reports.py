# reports.py
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

from pets import Bird, Fish, Rodent

attributes = ['count', 'stock_received', 'stock_sold', 'stock_lost']
displays = ['Current Stock', 'Stock Received', 'Stock Sold', 'Pet Losses']
subclasses = [Bird, Fish, Rodent]

def display_stock_report(inventory):
    print('Petstart Report')
    for d in range(len(displays)):
        print('\n' + displays[d])
        for subclass in subclasses:
            print(format_name(subclass))
            for species in inventory:
                if isinstance(species, subclass):
                    print('\t\t' + species.name + '\t' + 
                    str(getattr(species, attributes[d])))

def format_name(subclass):
    name = subclass.__name__
    if name == 'Fish': return '\n\t' + name
    elif name == 'Bird': return '\t' + name + 's'
    else: return '\n\t' + name + 's'
