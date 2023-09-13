""" 
Напишите программу для печати всех уникальных значений в словаре. 

Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
         {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, 
         {"VIII":"S007"}] 

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
# Макарцев
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
        {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, 
         {"VIII":"S007"}]
result = set()
for i in data:
    print(list(i.values()))
    result.add(list(i.values())[0])
print(result)