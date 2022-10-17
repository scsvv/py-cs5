# Создайте список из случайных чисел. Найдите количество различных элементов в нем.
from random import randint


N = 10
list_of_numbers = []

for i in range(N):
    list_of_numbers.append( randint(1, 5))

print(list_of_numbers)

list_of_unique_numbers = []
for item in list_of_numbers:
    if list_of_numbers.count(item) == 1: 
        list_of_unique_numbers.append(item)


print(list_of_unique_numbers)
print(list_of_numbers)