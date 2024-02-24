#homework6
'''
實作題目 1:
 給定一個包含水果名稱的列表請使用set來刪除重複的水果並返回一個不含重複水果的列表。 
fruits = ['apple', 'banana', 'mongo', 'apple', 'banana']
範例輸出：
['apple', 'banana', 'mongo']
'''
#list and set convert
fruits = ['apple', 'banana', 'mongo', 'apple', 'banana']
converted = set(fruits)
print(converted)

'''
實作題目 2:
 給定一個包含會員資訊的字典其中每個鍵是會員的名字每個值是一個包含會員興趣的列表請使用dict的方法來查找某個會員的興趣並返回一個包含該會員興趣的列表。如果該會員不存在則返回空列表。

member = {
  'kevin': ['coding', 'play'],
  'john': ['reading', 'music'],
  'tom': ['sports', 'movie']
}
name = 'kevin'
範例輸出：
['coding', 'play']
'''
#dictionary practice
member = {
  'kevin': ['coding', 'play'],
  'john': ['reading', 'music'],
  'tom': ['sports', 'movie']
}
print(member['kevin'])


'''
實作題目 3:
 給定兩個包含數字的列表請使用list的方法來合併兩個列表並返回一個包含兩個列表所有元素的列表。合併後的列表不需要排序或去除重複。

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
name = 'kevin'
範例輸出：
[1, 2, 3, 4, 5, 6]
'''
#list practice
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.insert(0, list_2)
print(list_1)
#print(list_2)
