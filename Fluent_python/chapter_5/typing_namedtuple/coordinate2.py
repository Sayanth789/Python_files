"""
    ``Coordinate``: a simple ``NamedTuple`` subclass

    This version has a field with a default value::
        >>> moscow = Coordinate(55.756, 37.617)
        >>> moscow
        Coordinate(lat=55.756, lon=37.617, reference='WGS84')
"""

from typing import NamedTuple 

class Coordinate(NamedTuple):
    lat: float 
    lon: float 
    reference: str = 'WGS84'

moscow = Coordinate(55.756, 37.617)
print(moscow)
