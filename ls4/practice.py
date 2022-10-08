"""
1. Меньшее из двух

Пользователь вводит два целых числа. Выведите меньшее из них.
2. Четырехзначное?

Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b: 
    print("A > B")
elif a == b: 
     print("A = B")
else: 
    print("A < B")

c = int(input())

if c > 999 and c < 10000: 
    print("XXXX")
else: 
    print("NO 4")