if 5 is 5:
    print('xd')
if 5>= 3:
    print("yes")
x=-0.5
if x>0:
    print('good')
elif x>-1:
    print('soso')
else:
    print('bad')

score = 75
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else :
    print('F')
# 條件後面都要加：
# nested condition, 要縮排
is_logged_in = True
role = 'teacher'
if is_logged_in:
    print('登入中')
    if role is 'member':
        print('welcome member')
    elif role is 'admin':
        print('welcome admin')
    elif role is 'teacher':
        print('welcome teacher')
else:
    print('無人登入')
# == 值一樣型態不用一樣, is 要值跟型態都一模一樣才會對
# in的用法
# dictionary, in 是檢查key的部分
member = {
    "name":"kk",
    "gender": 0,
    "age": 25
}
# list
user_list = ['kk', 'louis', 'alan']
# tuple
point=(3,4,1)
# set
allow_user = {'kk', 'louis'}
if 'age' in member :
    print('age in member')
if 'kk' in user_list :
    print('yes')
#dictionay內部的資料要加逗號 ,
member_list = {
    'M001':{
        'name':'audrey',
        'age':25,
        'tages':['female','young','good']
    },
    'M002':{
        'name':'Jeff',
        'age':52,
        'tages':['male','old','bad']
    },
    'M003':{
        'name':'Pink',
        'age':60,
        'tages':['female','old','good']
    }
}
member_id ='M001'
if member_id in member_list:
    print('he is the member')
else :
    print('not a member')

#['tages'] 要看清楚dictionary的命名
#如何取value的部分出來判斷
member_id ='M001'
tag = 'male'
print(member_list[member_id])

if tag in member_list[member_id]['tages']:
    print('he is the mamber')
else :
    print('he is not the member')

#兩三個條件要如何取出來處理呢 或是條件想要反過來怎麼處理
#not, and or
if not 5 < 3:
    print('false')

is_logged_in = False
is_admin = True
if not is_logged_in:
    print('未登入')

#真值表
#true and true = true
#false and true = false
#true and false = false
#false and false = false

if is_logged_in and is_admin:
    print('管理員登入')
elif is_logged_in:
    print('一班會員登入')
else:
    print('未登入')
#true or true = true
#false or true = true
#true or false = true
#false or false = false
if not is_logged_in or not is_admin:
    print('沒登入或不是管理員')

#for, while loop
#decide the initial status, and iterate method use while loop
#initial status, iterate method is fixed use for loop
for x in [1,2,3]:
    print(x)
for x in (3,2,1):
    print(x)
for x in {'name':'kk','age':25}:
    print(x)
foo = {
    'name':'kk',
    'age':25
    }
for x in foo.values():
    print(x)

x=1
while x<5:
    x=x+1
    print(x)
print("-------")
#for ... in ...
# iterable list, tuple, dic, set, string, range
#list
for x in [1,2,3]:
    print(x)
#tuple
for x in (1,2,3):
    print(x)
#dict
#interate -> dict's key
for x in {"name":"kk", "age":25}:
    print(x)
foo = {
    "name":"kk", 
    "age":25
    }
for x in foo.values():
    print(x)
bar ={"a", 12, "b"}
for x in bar:
    print(x)

#string
for x in "hello":
    print(x)
#range, 想要執行固定次數
for x in range(1,20):
    print(x)
for i in range(0,5):
    print('hello')

for i in range(5):
    print('--------')
    print('i=',i)
    for j in range(10):
        print('j=',j)

for i in range(1,10):
    print('----')
    for j in range(1,10):
        print(i, 'x', j,'=',i*j)
member_list = [
    {
        'name':'audrey',
        'age':25,
        'tages':['female','young','good']
    },
    {
        'name':'Jeff',
        'age':52,
        'tages':['male','old','bad']
    },
    {
        'name':'Pink',
        'age':60,
        'tages':['female','old','good']
    }
]
for member in member_list:
    print('member:', member['name'])
    for tag in member['tages']:
        print(tag)

#break
for i in range(5):
    if i % 2 == 0:
        print(i)
        break

#continue
for i in range(5):
    #print(i)
    if i % 2 is 0:
        continue
    print(i)
#質數2,3,5,7.....
check=False
n=int(input('please enter a number:'))
for x in range(2,n):
    if n % x is 0: #n倍x整除
        print('不是質數！')
        check=True
        break
if check==False:
    print('是質數！')
#何時要用一個= 何時用兩個＝＝
#= 是定義 ＝＝是在做比較
n=input('')
print('hello,',n)
