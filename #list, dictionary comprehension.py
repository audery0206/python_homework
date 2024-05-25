#list, dictionary comprehension
#做產生的動作利用for loop產生出來的直收集起來變成list,or dictionary
#normal for loop example
numbers = [2,3,1,4,6,3,5]
for number in numbers:
    print(number*2)
#-------------
#list comprehesion
numbers = [2,3,1,4,6,3,5]
numbers2 =[
    number*2
    for number in numbers
]
print(numbers2)
#-------------
#normal for loop
numbers = [2,3,1,4,6,3,5]
for number in numbers:
    if number%2 is 0:
        print(number*2)
#-------------
#filter comprehesion 先放結果後放條件
numbers = [2,3,1,4,6,3,5]
numbers2 = [
    number*2
    for number in numbers
    if number%2 is 0
]
print(numbers2)
#--------------
#normal case
numbers = [2,3,1,4,6,3,5]
for number in numbers:
    if number%2 is 0:
        print(number*2)
    else:
        print(number+1)
        
#map comprehesion 寫法好像是完全倒過來 結果寫前面 條件寫後面
numbers = [2,3,1,4,6,3,5]
numbers2=[
    number*2
    if number%2 is 0
    else number + 1
    for number in numbers
]
print(numbers2)
#-------
#函式化編成會需要把一連串算好的東西變成一個變數接下來傳給下一個東西
#example
numbers = [3,2,1,5,3]
for number in numbers:
    print(number)
#------
numbers2 =[
    number
    for number in numbers
]    
print(numbers2)
#-------
#filter 條件寫在後面 list comprehension
print([
    number
    for number in numbers
    if number>2
    ])
#map 條件寫在前面
new_numbers=[
    number
    if number%2 is 0
    else number +1
    for number in numbers
]
print(new_numbers)
#dic comprehension
#---mutable寫法, 先初始化一個figure,再將值塞進去
normal = {
    'height' : 175,
    'weight' : 75,
}
figure={}
for key, value in normal.items(): #把key, value從normal這個dictionary裡面拿出來
    print(key, value)
    figure[key] = value/100
print(figure)
#----immutable寫法, dic comprehension

normal = {
    'height' : 175,
    'weight' : 75,
}
figure={
    key : value/100
    for key,value in normal.items()
}
print(figure)
#-----filter mutable if else put after for loop

normal = {
    'height' : 175,
    'weight' : 75,
}
figure={}
for key,value in normal.items():
    if key is "height":
        figure[key]=value/100
print(figure)
#------filter immutable
normal = {
    'height' : 175,
    'weight' : 75,
}
figure={
    key:value/100
    for key, value in normal.items()
        if key is "height"   
}
print(figure)
#-------map mutable
normal = {
    'height' : 175,
    'weight' : 75,
}
figure={}
for key, value in normal.items():
    if key is "height":
        figure[key]=value/2
    else :
        figure[key]=value
print(figure)
#-------map immutable, if else put before for loop
normal = {
    'height' : 175,
    'weight' : 75,
}
figure={
    key:(
        value/2 
        if key is "height"
        else value
    )
    for key, value in normal.items()
}
print(figure)