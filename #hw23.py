#hw23
'''
Question 2: Handling Invalid Input
Description: 
# Given a function that takes a string from the user 
# and tries to convert it to an integer. 
# If the input is invalid, 
# catch the error and return "Invalid input".

Program：
def convert_to_int(input_str): 
  # Write your code here
pass

Example:
print(convert_to_int("abc")) 
# Should return "Invalid input"
'''
x=input('enter a number:')
def convert_to_int(x):
    try:
        number=int(x)
        return number
    except ValueError:
        return 'Invalid input, need enter digital numbers'

result = convert_to_int(x)
print('number=', result, ',thank you!!!')