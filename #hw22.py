#hw22
'''
Question 1: Handling Division by Zero in pandas
Description: # Given a division function, what error is thrown when the divisor is zero?
Catch this error and return a friendly message.

Program：
def safe_divide(x, y): 
  # Write your code here
pass

Example:
# Test case
print(safe_divide(10, 0)) # Should return "Cannot divide by zero"
'''

def safe_divide(x,y):
    try:
        result = x/y
        return result
    except ZeroDivisionError:
        print('cannot divide by 0')

x=int(input('enter number of x:'))
y=int(input('enter number of y:'))
result = safe_divide(x,y)
if result is not None:
    print('result:', result)


