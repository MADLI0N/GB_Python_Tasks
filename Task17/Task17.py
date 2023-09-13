""" 
Дан список чисел. Определите, 
сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

numbers = [1, 1, 2, 0, -1, 3, 4, 4]
unicNumbers = set(numbers)
print(numbers)
print(len(unicNumbers))

# Макарцев
#1
print(len(set(numbers)))

#2
help_list = []
for i in range(len(numbers)):
    if numbers[i] not in help_list:
        help_list.append(numbers[i])
print(len(help_list)) 

    
