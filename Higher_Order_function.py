# A higher order function is a function that takes one or more function as argument.
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    message = func("Hello, World")
    print(message)

greet(shout)  # Here greet is a higher order function that takes the functions shouts and whisper as parameter. 
greet(whisper)    

# A thread is a smallest unit of execution inside a program.
# A program can have one or more threads running.  Each thread runs independently but share the same  memory.
# (variables, data) with other threads.
#  .Useful for:  Downloading  multiple files, handling many users at once  etc.

# eg: of thread in python: 
import threading 

def greet():
    print("Hello from thread!")

#create a thread
t = threading.Thread(target=greet)

# Start the thread
t.start()

# Wait for the thread to finish
t.join()
print("Main thread done!")

