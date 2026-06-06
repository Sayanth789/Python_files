'''   
Raising an Exception in response to another Exception
<>
You want to raise an exception in response to catching a different exception, but want
to include information about both exceptions in the traceback 


'''

'''  
Issuing Warning Messages
<>
You want to have your program issue warning messages (e.g., about deprecated features
or usage problems)

<>
To have your program issue a warning message, use the warnings.warn() function. 
'''

import warnings 

def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfiles argument deprecated', DeprecationWarning)

        