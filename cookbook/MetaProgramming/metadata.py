'''
Preserving Function Metadata When Writing Decorators 
<??>
You’ve written a decorator, but when you apply it to a function, important metadata
such as the name, doc string, annotations, and calling signature are lost.

Always remember to apply @wraps decorator when define a decorator.

'''

# import time 
# from functools import wraps 

# def timethis(func):
#     ''' Decorator that reports execution time '''

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time() 
#         result= func(*args, **kwargs)
#         end = time.time() 

#         print(func.__name__, end-start)

#     return wrapper     



# @timethis
# def countdown(n:int):
#     while n > 0:
#         n -= 1


# countdown(1000000)        

'''  
Defining a Decorator With user Adjusted Attributes 

To write a decorator fun: that wraps  a function, but has user adjustable 
attributes that can be used to control the behavoir of the 
decorator at runtime.

<>
Here is a solution that expands on the last recipe by introducing accessor functions that
change internal variables through the use of nonlocal variable declarations.
'''
from functools import wraps, partial 
import logging 

def attatch_wrapper(obj, func=None):
    if func is None:
        return partial(attatch_wrapper, obj)
    setattr(obj, func.__name__, func)

def logged(level, name=None, message=None):
     '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name  else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
             log.log(level, logmsg)
             return func(*args, **kwargs)


        # Attach setter functions 
        @attatch_wrapper(wrapper)
        def set_level(newlevel):
             nonlocal level 
             level = newlevel

        @attatch_wrapper(wrapper)
        def set_message(newmsg):
             nonlocal logmsg 
             logmsg = newmsg

        return wrapper
    
    return decorate

              
# Example use 
@logged(logging.DEBUG)
def add(x, y):
     return x + y 

@logged(logging.CRITICAL, 'example')
def spam():
     print('Spam!')


''' 
Enforcing Type checking using a Decrator 
<>
You want to optionally enforce type checking of function arguments as a kind of asser‐
tion or contract.


'''   

# This is the implementation of @typeassert decorator 

from inspect import signature
from functools import _wraps 

def typeassert(*ty_args, **ty_kwargs):
     def decorator(func):
        #   If in optimized mode, disable type checking
        if not __debug__:
            return func 
        
        # Map function argument  names to supplied types 
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps 
        def wrapper(*args, **kwargs):
            #  Enforce type assertions across supplied arguments 
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                     if not isinstance(value, bound_types[name]):
                          raise TypeError(
                               'Argument {} must be {}'.format(name, bound_types[name])
                          )         
            return func(*args, **kwargs)
        return wrapper
     
     return decorate

# Defining Decorators As Part of a Class
# 
''' 
You want to define a decorator inside a class definition and apply it to other functions
or methods
<>
Defining a decorator inside a class is straightforward, but you first need to sort out the
manner in which the decorator will be applied. Specifically, whether it is applied as an
instance or a class method.
'''      
from functools improt wraps 
class A:
     # Decorator as an instance method 
    def decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
             print("Decorator !")
             return func(*args, **kwargs)

        return wrapper 

    # Decorator as a class method 
    def decorator(cls, func):
         @wraps(func)
         def wrapper(*args, **kwargs):
              print("decorator 2")
              return func(*args, **kwargs)
         return wrapper 

# As an instance method     
a = A() 

@a.decorator1
def spam():
     pass 

# As a class method 
@A.decorator2
def grok():
     pass 

'''
Writting Decorator That add Arguments to Wrapped Functions
<>
You want to write a decorator that adds an extra argument to the calling signature of
the wrapped function. However, the added argument can’t interfere with the existing
calling conventions of the function.

<> 
Extra arguments can be injected into the calling signature using keyword-only argu‐
ments.

'''
from functools import wraps 

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
            if debug:
               print('Calling', func.__name__)

            return func(*args, **kwargs)
     
    return wrapper 

@optional_debug
def Spam(a, b, c):
     print(a, b, c)
Spam(1, 2, 3, debug=True)     