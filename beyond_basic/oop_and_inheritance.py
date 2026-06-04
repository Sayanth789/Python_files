'''    
Similar to functions, inheritance is a code reuse technique that you can
apply to classes. It’s the act of putting classes into parent-child relationships
in which the child class inherits a copy of the parent class’s methods, free-
ing you from duplicating a method in multiple classes.

'''

class ParentClass:
    def printHello(self):
        print("Hello, world!")

class ChildClass(ParentClass):
    def someNewMethod(self):
        print("ParentClass objects don't have this method.")
        

class GrandChildClass(ChildClass):
        def anotherNewMethod(self):
                     
            print('Only GrandchildClass objects have this method.')


print('Create a ParentClass object and call its methods:')
parent = ParentClass()
parent.printHello()

# print('Create a ParentClass object and call its methods: ')
# child = ChildClass()
# child.printHello()
# child.someNewMethod()


# print('Create a GrandChildClass object and call its methods: ')
# grandChild = GrandChildClass()
# grandChild.printHello()
# grandChild.someNewMethod()
# grandChild.anotherNewMethod()


print('An error: ')
parent.someNewMethod()

''''  
Always Prefer Combosition over inheritance 

'''

'''  

isinstance()  and issubclass() functions 
'''

# ClassMethods 

'''  
You can recognize a class method in code when
you see two markers: the @classmethod decorator before the method’s def
statement and the use of cls as the first parameter, as shown in the follow-
ing example.
'''

class ExampleClass:
    def exampleRegualrMethod(self):
          print('This is a class method')

    @classmethod
    def exampleClassMethod(cls):
        print('This is a class method...')

# Call the class method without instantiating an object 
ExampleClass.exampleClassMethod() 

obj = ExampleClass() 

# Given the above line, these two lines are equivalent:
obj.exampleClassMethod() 
obj.__class__.exampleClassMethod() 

''' 

The cls parameter acts like self except self refers to an object, but the
cls parameter refers to an object’s class. This means that the code in a class
method cannot access an individual object’s attributes or call an object’s
regular methods. Class methods can only call other class methods or access
class attributes.
'''


