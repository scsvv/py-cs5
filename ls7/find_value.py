from random import randint


N = 10
numbers_list = []

for i in range(N):
    numbers_list.append(randint(1, 3))

print(numbers_list)
max_value = numbers_list[0]
second_max_value = numbers_list[1]
counts = numbers_list.count(numbers_list[0])
count_number = numbers_list[0]
min_value = numbers_list[0]
 
for i in numbers_list: 
    if max_value < i:  
        second_max_value = max_value
        max_value = i
    elif i > second_max_value and i < max_value: 
        second_max_value = i
    elif i < min_value: 
        min_value = i
    
    if numbers_list.count(i) > counts: 
        counts = numbers_list.count(i)
        count_number = i


print(max_value, second_max_value,  min_value, "counts: ", counts, count_number)


