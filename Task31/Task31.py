""" 
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где 
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

Input: 7
Output: 21
Задание необходимо решать через рекурсию 
"""
from datetime import datetime

def fib(k):
    if k in (1, 2):
        return 1
    return fib(k - 1) + fib(k - 2)

n = int(input("Введите номер числа Фибоначчи: "))
start_time = datetime.now()
print(fib(n)) # O(2^n) 1024 операции
end_time = datetime.now()
print(f"Время работы алгоритмя через рекурсию {end_time - start_time}")

start_time = datetime.now()
a0, a1 = 0, 1
for i in range(n):
    next_n = a0 + a1
    a0 = a1
    a1 = next_n
print(a0) # О(n)
end_time = datetime.now()
print(f"Время работы алгоритмя линеёной программы {end_time - start_time}")