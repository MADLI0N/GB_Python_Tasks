""" 
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)

Input: 5
Output: yes 
"""
from math import sqrt

num = int(input("Введите число: "))

def prime_number(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print(prime_number(num))

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(num))

def prime(num):
    for i in range(2, int(num // 2)):
        if num % i == 0:
            return False
    return True

print(prime(num))
    