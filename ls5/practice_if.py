# A + B > C 
"""
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A+B>C and B+C>A and C+A>B:
    print("Triangle is real")
else: 
    print("Triangle isn`t real")
"""

"""
День недели

Пользователь вводит номер дня недели. Выведите строку 'Выходные', если введенное число равно 6 или 7. В случае, если число лежит в диапазоне от 1 до 5 включительно, выведите строку 'Будни'.
"""
day = int(input("Enter day's number (1-7): "))

if day == 1: 
    print("Monday")
elif day == 2: 
    print("Tuesday")
elif day == 3: 
    print("Wednesday")
elif day == 4: 
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6: 
    print("Saturday")
elif day == 7:
    print("Sunday")
else: 
    print("Invalid value")