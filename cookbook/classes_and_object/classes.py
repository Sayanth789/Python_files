'''   
Changing the String Representation of instances

<> Want to change the output produced by the printing or 
viewing instances to something more sensible

<> To change the string representation of an instance, define the __str__() and
__repr__() methods. For example:

# '''
# class Pair:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y 

#     def __repr__(self):
#         return 'Pair({0.x!r}, {0.y!r})'.format(self)
#         # alternatively 
#         # return 'Pair(%r, %r)' % (self.x, self.y)

#     def __str__(self):
#         return '({0.x!s}, {0.y!s})'.format(self)

''''  
The __repr__() method returns the code representation of an instance, and is usually
the text you would type to re-create the instance. The built-in repr() function returns
this text, as does the interactive interpreter when inspecting values. The __str__()
method converts the instance to a string, and is the output produced by the str() and
print() functions

'''    

# f = open('file.txt')
# print(f)

''' 
Customizing String Formatting.
><
You want an object to support customized formatting through the format() function
and string method.
To customize string Formatting, define __format__() method on a class 

'''
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'

}

class Date:
    def __init__(self, year, month, day):
        self.year = year 
        self.month = month 
        self.day = day 

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2012, 12, 21)
print(format(d))


print(format(d, 'mdy'))
print('The date is {:ymd}'.format(d))

# Creating Managed Attributes 
''' 
<>
You want to add extra processing (e.g., type checking or validation) to the getting or
setting of an instance attribute.

A simply way to customize access to an attribute is to define it as a "property"
Here is the code that define a property adds simple type checking to an attrbiute 

'''

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter Function 
    @property 
    def first_name(self):
        return self._first_name 

    # Setter function 
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value 

    # Deleter function (optional) 
    @first_name
    def first_name(self):
        raise AttributeError("can't delete attribute")       
    
    ''' 
    A critical feature of a property is that it looks like a normal attribute, but access auto‐
matically triggers the getter, setter, and deleter methods. For example:
    '''

a = Person('Guido')
print(a.first_name)


''' 
Extending Clases with Mixins 
<>
You have a collection of generally useful methods that you would like to make available
for extending the functionality of other class definitions. However, the classes where
the methods might be added aren’t necessarily related to one another via inheritance.
Thus, you can’t just attach the methods to a common base class.

'''
import math 

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __repr__(self):
        return  '{!r:}, {r:})'.format(self.x, self.y) 

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

p = Point(3, 6)
d = getattr(p, 'distance')(0, 0)      

