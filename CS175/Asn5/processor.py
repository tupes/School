# processor.py
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


import sys
from collections import deque
import errors
import actions
import inventory

class EventProcessor:

    def __init__(self):

        # Python Deque class is faster than Python Lists
        self._queue = deque()

    def event_queue_count(self):
        return len(self._queue)

    def _execute_action(self, event_data, inventory):

        event_type = event_data[1]

        if event_type == 'EndOfDay':
            event_action = actions.EndOfDayAction()
        elif event_type == 'Receive':
            event_action = actions.ReceiveAction()
        elif event_type == 'Sale':
            event_action = actions.SaleAction()
        elif event_type == 'PetCare':
            event_action = actions.PetCareAction()
        elif event_type == 'PetLoss':
            event_action = actions.PetLossAction()
        elif event_type == 'OrderStock':
            event_action = actions.OrderStockAction()
        else:
            raise errors.EventError("Unidentified event")
        
        event_action.do_action(event_data, inventory)

        return event_action
    
    def _process_action_events(self, event_data):
        for item in event_data:
            self._queue.append(item)

    def process_event(self, raw_event_data, inventory):
        event_data = raw_event_data.split('|')

        processed_action = self._execute_action(event_data, inventory)

        # The result tuple is structure as follows:
        #   SUCCESS: ('SUCCESS',)
        #   SUCCESSWITHEVENTS: ('SUCCESSWITHEVENTS', raw_event_data)
        #   FAIL: ('FAIL', error_message)
        #   FAILWITHEVENTS: ('FAILWITHEVENTS', error_message, raw_event_data)
        if processed_action.result[0] == 'SUCCESS':
            return processed_action
        elif processed_action.result[0] == 'SUCCESSWITHEVENTS':
            self._process_action_events(processed_action.result[1])
        elif processed_action.result[0] == 'FAIL':
            raise errors.ActionError(processed_action.result[1]) 
        elif processed_action.result[0] == 'FAILWITHEVENTS':
            self._process_action_events(processed_action.result[2])
            raise errors.ActionError(processed_action.result[1])
        else:
            raise errors.EventError("Undefined action result")

        return processed_action

    def process_queued_event(self, inventory):
        try:
            event = self._queue.popleft()
            processed_action = self.process_event(event, inventory)
        except IndexError:
            raise errors.EventError("Event dispatcher event queue empty")
        except errors.ActionError:
            print("Action incomplete")
            print("ActionError:", sys.exc_info()[1])
        
        return processed_action

