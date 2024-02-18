#homework4
#1. 建立一個dictionary：請寫一段程式碼，建立一個dictionary，其中包含三個key-value pair，key是你喜歡的水果，value是它們的價格（整數）。

fruits = dict()
fruits = {
    'MANGO':120, 
    'STRAWBERRY':200, 
    'BANANA':20
    }
fruits['MANGO']
#2. 存取dictionary中的元素：請寫一段程式碼，使用索引或get方法，從上一題建立的dictionary中存取某個水果的價格，並印出來。
print (fruits.get('MANGO'))

#3. 更新或刪除dictionary中的元素：請寫一段程式碼，使用update或del方法，對上一題建立的dictionary進行以下操作：增加一個新的水果和它的價格，修改一個已有的水果的價格，刪除一個已有的水果和它的價格。最後印出更新後的dictionary

# 增加一個新的水果和它的價格
fruits.update({"purple": 80})
print(fruits)
# 修改一個已有的水果的價格
fruits['STRAWBERRY'] = 180
print(fruits)
# 刪除一個已有的水果
del fruits['BANANA']
print(fruits)