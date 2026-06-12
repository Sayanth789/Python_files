from clock_deco import clock 
import fib_demo
import fib_demo_lru 

@clock 
def demo1():
    fib_demo.fibonacci(30)

@clock 
def demo2():
    fib_demo_lru.fibonacci(30)    

print(demo1())    
print(demo2())  
