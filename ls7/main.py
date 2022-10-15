"""
a_list = [1, 2, 3, 4, 5, 6, 7, 8]
c_list = a_list
b_list = a_list.copy()
a_list[0] = 10
print(b_list, c_list)
"""
a_list = []

# ставит список в конец 
a_list.extend([15, 22, 14, 14, 14, 14, 765])

# ставит указаную позицию указанное значение
a_list.insert(0, 1)

# ставит значение в конец
a_list.append(12)

a_list[0] = 101

print(a_list)

# Удаление по индексу - пустой удаляет последний
a_list.pop()
a_list.pop(1)

# Удаление по по значению
a_list.remove(14)

print(a_list)

# индекс, номер порядковый елемента
print(a_list.index(765))
a_list.sort()
a_list.clear()
print(a_list)