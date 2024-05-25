#exception
print("hello")
try:
    1/0
except: 
    print("1無法除0")
print('world')
#正常終止normal termination
'''異常終止案例
print("hello")
1/0
print('world')
'''
try:
    1/0
except ZeroDivisionError as e: 
    print(e)
    print(e.__class__.__name__)
try:
    x=int(input('enter a number:'))
    y=int(input('enter a number:'))
    print(x/y)
except(ZeroDivisionError,ValueError):
    print('wrong')

try:
    x=int(input('enter a number:'))
    y=int(input('enter a number:'))
    print(x/y)
except(ZeroDivisionError):
    print('不能除0')
except(ValueError):
    print('需要是數字')

try:
    1/0
except:
    print('in except')
finally:
    print('in finally')