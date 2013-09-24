# timestamp.py
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
import datetime
import time

class Timestamp:
    def __init__(self, data = None):
        if data:
            try:
                self._moment = self._clean_timestamp(data)
            except errors.TimestampError:
                print("Invalid timestamp:", data)
                print("Timestamp Object not created")
                self._moment = None 
        else:
            self._moment = datetime.datetime.now()

    def __str__(self):
        if self._moment:
            return self._moment.strftime('%Y-%m-%dT%H:%M:%S')
        else:
            return str()

    def __sub__(self, other_moment):
        """Returns a datetime.timedelta object."""
        return other_moment - self._moment

    def difference(self, other_moment):
        """Returns a string showing the length of time between two timestamps.
        """
        tmp = other_moment - self._moment
        return ''.join(str(tmp).split('.')[:1]) 

    def _clean_timestamp(self, moment):
        """Returns the timestamp as a datetime.datetime object."""
        if type(moment) is not datetime.datetime:
            try:
                valid_date =\
                    datetime.datetime.strptime(moment, '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                raise errors.TimestampError('Invalid timestamp')
        
            return datetime.datetime.strptime(moment, '%Y-%m-%dT%H:%M:%S')
    
    def date(self):
        return self._moment.date()

    def time(self):
        return self._moment.strftime('%H:%M:%S')


def is_valid_timestamp(timestamp):
    if type(timestamp) is not Timestamp:
        return False
    return True

