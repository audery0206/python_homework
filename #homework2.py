#homework2
#給定一個名為 numbers 的 list，其中包含一些整數。
def numbers = list()
def numbers_new = list()
    numbers = [11,5,13,14,5,16,5,24,22,100,5,90]
    print(numbers[0:13:2])
#使用切片取得這個 list 中索引值為奇數的元素，並將其儲存在一個新的 list 中。
    numbers_new = numbers[0:13:2]
    print(numbers_new[0:])
#將新的 list 反轉。
    numbers_new.reverse()
    print(numbers_new[0:])
#利用 list.count() 函數找出新的 list 中數字 5 出現的次數。
    numbers_new.count(5)

