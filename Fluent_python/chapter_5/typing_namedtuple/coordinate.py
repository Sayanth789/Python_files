# This is an eg: of namedtuple 
"""
``Coordinate``: a simple ``NamedTuple`` subclass with a custom ``__str__``::

    >>> moscow = Coordinate(55.756, 37.617)
    >>> print(moscow)
    55.8°N, 37.6°E

"""


from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float 
    lon: float 

    def __str__(self):
        ns = "N" if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

'''  
frozen=True
(*) Protects against accidental changes to the class instances
(*) order = True 
Allows sorting of instances of data class.

'''
