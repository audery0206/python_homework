#function introduction
#define
#if it is even number
def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False
#invoke.
print(is_even(4))
#---------------
def add(x,y):
    return x+y
print(add(1,4))
#---------------
def is_prime(number):
    for i in range(2, number):
        if number%i ==0:
            return False #如果return sth就會直接離開這個不會往下執行
        return True
print(is_prime(5))
#---------------
def echo (x1, x2, *args, **kwargs):
    print(x1, x2, args, kwargs)

echo(1,2,3,4,x=5,y=6)
echo(1,2)
echo(x1=1,x2=2,x3=3)
#先positionaal 在 keyword
#positionaal args用＊打包成list
#keyword args用**打包成dict
