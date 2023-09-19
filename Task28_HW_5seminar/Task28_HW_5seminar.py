""" 
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

2 2
4 
"""

a = 3
b = 5

# Мое
def sum(a, b):    
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)   

# Робот
# def sum(a, b):
#     if b == 0:
#         print("b == 0 -> ", a, b)
#         return a
#     elif a == 0:
#         print("a == 0 -> ", a, b)
#         return b
#     else:
#         print(a, b)
#         return sum(a + 1, b - 1)
    
print(sum(a, b))