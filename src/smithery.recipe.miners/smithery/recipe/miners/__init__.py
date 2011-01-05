"""
Miners are recipes that extract data and metadata from resources
(i.e. files, databases, urls) and collect them into a common namespace.

The namespace is implemented as a python dictonary and miners are free to
structure the data and metadata as they see fit.

In a sequence of collaborating miners later ones can use the namespace as
populated by the previous ones.

The namespace is intended to be eventually processed and published by smiths as they see fit.
"""

from .base import Miner
from .filesystem import listdir2, Namespace, File, Csv
try:
    from .geodata import WMS
except ImportError:
    pass
try:
    from .google import BaseGoogleCalendar, GoogleCalendar
except ImportError:
    pass

__all__ = ('Miner', 'Namespace', 'File', 'Csv', 'WMS',
    'listdir2', 'BaseGoogleCalendar', 'GoogleCalendar')
