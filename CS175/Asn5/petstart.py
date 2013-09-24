# petstart.py
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


import processor
import errors
import reports
import inventory

import sys
import fileinput

__version__ = "1.2.2"


# Main
event_processor = processor.EventProcessor()
completed_actions = list()
myinventory = inventory.Inventory()

for input_line in fileinput.input():
    input_line = input_line.rstrip("\n")

    # Process any backlog of stored queued events first
    # The queue only receives events when an action triggers a new event
    # which is then added to the event processor's internal event queue.
    while event_processor.event_queue_count() > 0:
        try:
            completed_queued_action =\
                    event_processor.process_queued_event(myinventory)
        except errors.EventError:
            print("Error:", sys.exc_info()[1])
        completed_actions.append(completed_queued_action)

    try:
        completed_action =\
                event_processor.process_event(input_line, myinventory)
    except errors.ActionError:
        print("Action Error - Unable to complete action:",\
                sys.exc_info()[1])
    except errors.EventError:
        print("Event Error:", sys.exc_info()[1])
    completed_actions.append(completed_action)

# Generate Report
reports.display_stock_report(myinventory)
