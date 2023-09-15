""" 
Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в 
порядке возрастания все те числа, которые встречаются в 
обоих наборах.

Пользователь вводит 2 числа. n - кол-во элементов первого 
множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12 
"""
numbers = input("\nВведите кол-во элементов первого и второго множества: ").split()
set_one = set(input (f"Введите {numbers[0]} элементов первого множества: ").split())
set_two = set(input(f"Введите {numbers[1]} элементов второго множества: ").split())
print(*sorted(int(i) for i in set_one.intersection(set_two)))

