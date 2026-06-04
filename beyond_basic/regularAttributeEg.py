class ClassWithRegualarAttributes:
    def __init__(self, someParameter):
        self.someAttribute = someParameter

obj = ClassWithRegualarAttributes('some initial value')

print(obj.someAttribute)
obj.someAttribute = 'changed value'
print(obj.someAttribute)  # Print c'hanged value'
del obj.someAttribute   # Delete the someAttribute attribute 
 


