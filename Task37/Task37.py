""" 
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3 
"""
# Макс
def reverseN(n):
    if n > 0:
        num = int(input("Введите число: "))
        reverseN(n - 1)
        print(num, end = " ")

# Макарцев
def f(n):
    if n == 0:
        return ''
    k = int(input('Введите число: '))
    return f(n - 1) + f' {k}'


n = int(input('Введите кол-во чисел: '))
reverseN(n)
print(f(n))
print(*f(n).split())
#f(2) -> f(1) + " 3"
#          |
#        f(0) = "" + " 4"
#          |
#         ""