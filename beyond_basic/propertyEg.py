class ClassWithProperties:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self):   # this is a "getter" method 
        return self._someAttribute 

    @someAttribute.setter 
    def someAttribute(self, value):
        #  yeah this is setter 
        self._someAttribute = value 

    @someAttribute.deleter 
    def someAttribute(self):  # this is "deleter" method.
        del self._someAttribute


obj = ClassWithProperties() 
print(obj.someAttribute)  # print 'some initial value'
obj.someAttribute = 'changed value'
print(obj.someAttribute)  # Print 'changed value'
del obj.someAttribute  # Delete the _someAttribute attribute 


