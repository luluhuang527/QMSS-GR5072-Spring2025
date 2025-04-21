
# Set directory
import os
os.chdir(r'C:\Users\nicho\OneDrive\Desktop\MDS\QMSS-GR5072-Spring2025\Week 8\Programs\Example 1')
os.getcwd()

from calculate_age import get_age
from calculate_age import t
# import calculate_age       # <--- Does not work !
# from calculate_age import *  # <--- Works -- but use wildcard "*" importing with extreme caution ! 
import pytest
import datetime


def test_get_age():
    # Given example data to test. 
    yyyy, mm, dd = map(int, "1996/07/11".split("/")) # Example date -- should be 29 if today is March 2025 since we are rounding age   
    # Call function and collect output so it can be tested
    age = get_age(yyyy, mm, dd)
    # Check for a potential exception
    assert age == 29, "Age is incorrectly calculated, it should be 29!"  # If this assertaion fails, an exception is raised ! We need to check our code

# Question: Which other tests should we add to get at a comprehensive test suite?

# get_age(1980, 1, 23)

# Why the map function helps ! 
# yyyy, mm, dd = (int(x) for x in "1996/07/11".split("/"))
# get_age(yyyy, mm, dd)
# yyyy, mm, dd = map(int, "1996/07/11".split("/"))
# yyyy

#########################################
  # Run unit test !  
#########################################

# Run these two lines in your PC's terminal - updating your path to Example 1
# cd C:\Users\nicho\OneDrive\Desktop\MDS\QMSS-GR5072-Spring2025\Week 8\Programs\Example 1
# python -m pytest  

# This code runs the pytest module using the Python interpreter.
# • The -m flag specifies that the module should be run as a script.
# • The pytest module is a testing framework for Python that allows developers to write and run tests for their code.
# • Running this command will execute all the tests in the current directory and its subdirectories.

