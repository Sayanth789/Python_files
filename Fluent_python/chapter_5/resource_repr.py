from dataclasses import dataclass, field, fields
from typing import Optional, TypedDict 
from enum import Enum, auto 
from datetime import date 

class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()

@dataclass 
class Resource:
    """ Media resources description """
    identifier: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date : Optional[date] = None 
    type: ResourceType = ResourceType.BOOK 
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        ident = ' ' * 4 
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{ident}{f.name} = {value!r},')

            res.append(')')
            return '\n'.join(res)
        

class ResourceDict(TypedDict):
    identifier: str 
    title: str 
    creators: list[str]
    date: Optional[date]
    type: ResourceType
    description: str 
    language: str 
    subjects: list[str]


if __name__ == "__main__":
    r = Resource('0')    
    description = 'Improving the design of existing code'
    book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
                    ['Martin Flower', 'Kent Beck'], date(2018, 11, 19),
                     ResourceType.BOOK, description,
                     
                     'EN', ['computer programming', 'OOP'])
    print(book)
    book_dict: ResourceDict = {
        'identifier': '978-0-13-475759-9',
        'title': 'Refactoring, 2nd Edition',
        'creators': ['Martin Fowler', 'Kent Beck'],
        'date': date(2018, 11, 19),
        'type': ResourceType.BOOK,
        'description': 'Improving design of existing code',
        'language': 'EN',
        'subjects': ['computer programming', 'OOP']
    }    

    book2 = Resource(**book_dict)
    print(book == book2)