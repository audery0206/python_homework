#homework17
'''Question 2: 
Implement a function that multiplies each number in a given list of numbers by 2 and returns a new list.
Input: ['100', '0', '300', '500']
Output: [200.0, 0.0, 600.0, 1000.0]'''
numbers = ['100','0','300','500']
double_number = [
    number*2
    for number in map(float, numbers)
]
print(double_number)