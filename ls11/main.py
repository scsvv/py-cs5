"""
def printf(*args):
    print(*args)
 
def sum(a, b=-3, *args): 
    print(args)
    printf(a+b)

printf("asd", "asdf", "asd")
printf("fff")
sum(3, 7)
sum(3, 10)
sum(3, 15)
sum(3)
sum(1, 2)
"""

def sum(a, b): 
    return a + b

c = sum(12, 12)
print(sum(10, 2)) 
print(c)