""" 
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

Вывод:
2.5 10 
"""
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] # в списке находится кортеж

def find_farthest_orbit(list_of_orbits):
    max_index = 0
    max_value = 0
    for i in range(len(orbits)):
        if orbits[i][0] != orbits[i][1]:
            area = orbits[i][0] * orbits[i][1]
        if area > max_value:
            max_value = area
            max_index = i
    return list_of_orbits[max_index]

print(*find_farthest_orbit(orbits))

def find_farthest_orbit_1(list_of_orbits):
    return list_of_orbits[[(i[0] != i[1]) * i[0] * i[1] for i in
                list_of_orbits].index(max([(i[0] != i[1]) *
                    i[0] * i[1] for i in list_of_orbits]))]

print(*find_farthest_orbit_1(orbits))

def find_farthest_orbit_2(list_of_orbits):
    new_def = lambda x, y: (x != y) * x * y
    new_list = [new_def(i[0], i[1]) for i in
                    list_of_orbits]
    return list_of_orbits[new_list.index(max(new_list))]

print(*find_farthest_orbit_2(orbits))