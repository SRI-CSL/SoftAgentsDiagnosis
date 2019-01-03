""" A StringBuffer class for string buffer addicts.
"""
import io

from ..crap.py import deviation_unicode

class StringBuffer(object):

    def __init__(self):
        self.empty = True
        self._stringio = io.StringIO()

    def __str__(self):
        val = self._stringio.getvalue()
        self._stringio.close()
        return val

    def append(self, obj):
        data = deviation_unicode(obj)
        if self.empty and data:
            self.empty = False
        self._stringio.write(data)
        return self

    def isempty(self):
        return self.empty
