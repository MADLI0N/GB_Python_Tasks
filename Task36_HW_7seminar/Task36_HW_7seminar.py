""" 
Напишите функцию 
print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и 
столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы 
(подумайте,почему не с нуля). 
Примечание: бинарной операцией называется любая операция, 
у которойровно два аргумента, как, 
например, у операции умножения.

Ввод: 
print_operation_table(lambda x, y: x * y) 

Вывод:
1 2  3  4  5  6
2 4  6  8  10 12
3 6  9  12 15 18
4 8  12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36  
"""
def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        list_n = [str(i + 1) for i in range(num_rows)]
        print(*list_n)        
        for i in range(1, num_rows):            
            result = []
            result.append(str(i + 1))
            for j in range(1, num_columns):                
                result.append(str(operation(i + 1, j + 1)))               
            print(*result," ")       
 
print_operation_table(lambda x, y: x + y, 4, 4)

# Автотест
def print_operation_table(operation, num_rows , num_columns ):
 if num_rows < 2 or num_columns < 2:
  print('ОШИБКА! Размерности таблицы должны быть больше 2!')
 else:
  print(' '.join([str(i) for i in range(1, num_columns + 1)]))
  for i in range(2, num_rows + 1):
   print(i, end = ' ')
   for j in range(2, num_columns + 1):
    print(operation(i, j), end = ' ')
   print()
