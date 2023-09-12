""" 
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32 
"""

classOne = 20
classTwo = 21
clasThree = 22

print((classOne + classOne % 2 + classTwo + classTwo % 2 + clasThree + clasThree % 2) // 2) # Моё

total_desks = 0

total_desks += classOne // 2 + classOne % 2
total_desks += classTwo // 2 + classTwo % 2
total_desks += clasThree // 2 + clasThree % 2

print(total_desks) # Макса
