from abc import ABC, abstractmethod
from inspect import getmembers, isfunction

'''
This is an eg: of duck typing with ABCs
'''

class Tombola(ABC):

    @abstractmethod
    def __init__(self, iterable):
        """New instance is loaded from an iterable."""

    @abstractmethod
    def load(self, iterable):
        """ Add items from an iterable """

    @abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """    
    def loaded(self):
        try:
            item = self.pick()
        except LookupError:
            return False 
        else:
            self.load([item])
            return True

    @classmethod 
    def __subclasshook__(cls, other_cls):
        if cls is Tombola:
            interface_names = function_names(cls)
            found_names = set()
            for a_cls in other_cls.__mro__:
                found_names |= function_names(a_cls)
            if found_names >= interface_names:
                return True 
        return NotImplemented        

def function_names(obj):
    return {name for name, _ in getmembers(obj, isfunction)}
