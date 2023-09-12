""" 
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 
"""
a = int(input("\nВведите число: "))

fib = 10
numOne = 0
numTwo = 1
temp = 1

for i in range(3, fib + 1):    
    temp = numOne + numTwo
    if i == fib:
        print(-1)
    elif temp == a:
        print(i)
        break
    numOne = numTwo
    numTwo = temp

# Макарцев
n0 = 0
n1 = 0
n2 = 1
i = 2 # Так как 2 первых числа уже известны это 0 и 1
while n0 < a:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > a:
        i = 0
if i != 0:
    print(i)
else:
    print(-1)



