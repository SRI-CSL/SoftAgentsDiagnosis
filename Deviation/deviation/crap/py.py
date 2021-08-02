import sys

def deviation_intern(string):
    return sys.intern(string) if sys.version_info[0] > 2 else intern(string)

def deviation_unicode(string):
    return  str(string) if sys.version_info[0] > 2 else unicode(string)
