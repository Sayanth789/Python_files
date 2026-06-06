'''
You want to know in detail what your code is doing under the covers by disassembling
it into lower-level byte code used by the interpreter.

<>
The dis module can be used to output a disassembly of any Python function. For
example:

'''

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print("BlastOff!")


import dis 
dis.dis(countdown)