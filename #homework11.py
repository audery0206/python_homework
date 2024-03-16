#homework11
'''Given a positive integer year representing a Gregorian calendar year, 
determine whether it is a leap year and output True or False. A year is a leap year if:
It is divisible by 4 but not divisible by 100, or
It is divisible by 400.
For instance:
For year = 2000, the output should be True.
For year = 2100, the output should be False.
'''
year = int(input ('please enter the year number :'))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print ('True')
else:
        print ('False')
