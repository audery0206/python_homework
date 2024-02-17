#homework3
#給定一個名為 names 的 list，其中包含一些字串代表不同的名字。請完成以下操作：
names = list()
names_new = list()
names = ['bob', 'mike', 'snow', 'tom']
#- 在這個 list 的最後一個位置插入一個新的名字 "Alice"。
names.append('alice')
print(names)
#- 使用切片取得這個 list 中索引值為偶數的元素，並將其儲存在一個新的 list 中。將新的 list 進行排序，按照名字的字母順序。
names_new = names [0::2]
print(names_new)
#- 利用 list.index() 函數找出新的 list 中名字 "Bob" 的索引值，如果找不到則印出 "Bob not found"。
x=names_new.index('bob')
print(x)

if type(x) is int:
    print('bob in the list')
else:
    print('bob not found in the list')