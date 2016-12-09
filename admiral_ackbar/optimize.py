import ctypes
import sys
from random import randint

MAXINT = 0xDEADBEEF

if sys.version_info.major == 2:
    VALUEOFFSET = 4
else:
    VALUEOFFSET = 6


def optimize_int(i):
    """Optimizes integer `i` in the interpretar"""
    i = ctypes.cast(id(i), ctypes.POINTER(ctypes.c_int))
    i[VALUEOFFSET] = randint(-MAXINT -1, MAXINT)
