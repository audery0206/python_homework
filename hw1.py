
N = int(input('please input how many number do you need :'))

P = input('please input all the numbers :')
numbers = list(map(int, P.split()))

numbers.sort()

numbers.reverse()

print(' '.join(map(str, numbers)))