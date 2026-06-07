# This is an eg: of namedtuple 
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
