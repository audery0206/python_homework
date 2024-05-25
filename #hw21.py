#hw21
'''
Description:  

Define a function add(*args) that takes any number of positional arguments and returns their sum.
Example:
print(add(1, 2, 3, 4)) # 10
print(add(1, 2, 3, 4, 5, 6, 7)) # 28
'''
def add(*args):
    total = sum(args)
    return total

print(add(1,2,3,4))
print(add(1,2,3,4,5,6,7))
