#recursive and iterative
#2 number add
#n, x = map(int, input().split())
#print(n + x)

#1+~100
total=0
for number in range(1,101):
    total = total + number
print(total)
#1+~100
total = sum(range(1,101))
print(total)
#1+~100
def add(start, end):
    if start >= end:
        return 0
    return start + add(start+1, end)
total = add(1, 101)
print(total)
#-------------------
#費氏數列 前面兩個數加起來等於第三個數字
#1,1,2,3,5,8,...
def fin(n):
    if n is 1 :
        return 1
    if n is 2 :
        return 1 
    return fin(n-1)+fin(n-2)
print(fin(20))
# will stack overflow.
#如何用一般的寫法去處理遞迴的問題 避免overflow

# iterative(dynamic program)用記憶體換時間 <-> recursive 用時間換取空間（記憶體）
n=20
f={
    1:1,
    2:1,
}
for i in range(3, n+1):
    f[i]=f[i-1]+f[i-2]
#for key, value in f.items():
print(f)
#----------------------
