""" 
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо,  K – положительное число.

Input:   [1, 2, 3, 4, 5] k = 3
Output:  [3, 4, 5, 1, 2]   
"""
n = [1, 2, 3, 4, 5]
print(n)
k = 3
print(n[-k:] + n[:-k])

#Народное
n = [1, 2, 3, 4, 5]
k = 12
k %= len(n) # Макарцев
d = (n[-k:] + n[:-k])
print(d)

# Макарцев(через циклы)
list_1 = [1, 2, 3, 4, 5]
k = 3
k %= len(list_1)
output_list = []
for i in range(k):
    output_list.append(list_1[len(list_1) - k + i])
for i in range(len(list_1) - k):
    output_list.append(list_1[i])
print(output_list)

