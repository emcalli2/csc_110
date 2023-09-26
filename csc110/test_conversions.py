'''
Author: Adriana Picoral
Course: CSC 110

This python script tests the solution for programming problem 3.
No need to make any changes to this code. Just have this .py in the same
folder/directory as your temperatures.py and run this file.
'''

# from the solution file, import all functions
from conversions import *

def pass_or_fail(result, assert_value):
  '''
  This function tests whether a value returned by a function matches
  the expected value -- it's used to test functions
  Args:
    result: any type returned by a function
    assert_value: any type that is expected
  Returns:
    nothing, it prints messages
  '''
  # try to assert value returned by function is equal to expected value
  try:
    assert result == assert_value
    print("Test passed.")
  except AssertionError: # try failed, values are different
    print("Test failed. " + str(result) + " != " + str(assert_value))

def main():
  '''
  This function calls pass_or_fail to assert the accuracy of the
  functions in this programming problem solution
  '''
  print("Enter 1:")
  pass_or_fail( kg_to_lbs(), 2.21 )

  print("Enter 6:")
  pass_or_fail( kg_to_lbs(), 13.23 )

  print("Enter 120:")
  pass_or_fail( kg_to_lbs(), 264.6 )

  print("Enter 1:")
  pass_or_fail( liters_to_gallons(), 0.26 )

  print("Enter 3:")
  pass_or_fail( liters_to_gallons(), 0.79 )

  print("Enter 6:")
  pass_or_fail( liters_to_gallons(), 1.59 )

main()