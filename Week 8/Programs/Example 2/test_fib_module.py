# Set directory
import os
os.chdir(r'C:\Users\lulu\Documents\GitHub\QMSS-GR5072-Spring2025_Class\Week 8\Programs\Example 2')

# Import module
from fib_module import fib

def test_fib0():
    # test edge 0
    obs = fib(0)
    assert obs == 0, "fib(0) = 0, Not " + str(obs)

def test_fib1():
    # test edge 1
    obs = fib(1)
    assert obs == 1, "fib(1) = 1, Not " + str(obs)

def test_fib6():
    # test internal point
    obs = fib(6)
    assert obs == 8, "fib(6) = 8, Not " + str(obs)
    
### Challenge: We are missing some key unit tests for our Fibonacci sequence! 
###            Add them! (Hint: Check the fib_module.py for some special cases)
    
# # Run these two lines in your PC's terminal - updating your path for the Example 2 directory
# cd C:\Users\lulu\Documents\GitHub\QMSS-GR5072-Spring2025_Class\Week 8\Programs\Example 2
# python -m pytest test_fib_module.py

# This code runs the pytest module using the Python interpreter.
# • The -m flag specifies that the module should be run as a script.
# • The pytest module is a testing framework for Python that allows developers to write and run tests for their code.
# • Running this command will execute all the tests in the current directory and its subdirectories.


