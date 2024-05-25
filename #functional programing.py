#functional programing
#filter : 數量減少 用函式篩選掉

numbers = [3,1,2,4,5]
def is_even(x):
    if x%2 == 0 :
        return True
    return False
#filtered_numbers = filter(is_even, numbers)
for number in filter(is_even, numbers):
    print(number)

#map : 轉換映射 數量不變
def multiplx_2(x):
    return x*2
for number_mul in map(multiplx_2, numbers):
    print(number_mul)

def mod_2(x):
    if x%2 == 0 :
        return 'even' 
    return 'odd'

for number_mod2 in map(mod_2, numbers):
    print(number_mod2)

prices = ['100', '50', '300', '260']
x = sum(map(float, prices))
print(x)

def great_than_500(x):
    if x>500:
        return x
#y=filter(great_than_500, map(multiplx_2, map(float, prices)))
#print(y)
#<filter object at 0x104d22df0> => 怎麼辦？？
y=list(filter(great_than_500, map(multiplx_2, map(float, prices))))
print(y)

#anonymous function - lambda
def is_even(x):
    return x%2 
lambda x: x%2  #沒有函式名稱
is_even_lambda = lambda x: x%2 #存入一個名稱內 把函式當成一個變數型態運用

z=filter(lambda x: x>500, map(lambda x: x*2, map(float, prices)))
u=list(z)
print(u)
#印出list.

for price in filter(lambda x: x>500, map(lambda x: x*2, map(float, prices))):
    print(price)
#for sth in sth, 會一個一個印出來
#程式如果複雜就不要用lambda 可讀性低
#----
#lambda if else 的用法
foo = lambda x : 1 if x%2 is 0 else 2 #lambda if else是先寫值才寫條件
print(foo(6))

lambda x, y: x+y #lambda用逗點相隔 不需要括弧

