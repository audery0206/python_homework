#hw19
'''
Description: 

Write a function is_even(x) that takes an integer x and returns True if x is even, and False otherwise.
Example:
print(is_even(4)) # True
print(is_even(5)) # False
'''
def is_even(x):
    if x%2 == 0:
        return True
    return False
print(is_even(4))
print(is_even(5))