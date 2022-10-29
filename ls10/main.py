"""
Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение. Например: 
"""
# None, null, undefined

while 1: 
    K = input("Enter number: ")
    

    try: 
        K = int(K)
        break
    except ValueError: 
        print("Введите число!!!")
    

goods_quantity = {}

for i in range(K):
    name = input("Fruit's name: ")
    count= int(input("Quantity: "))

    goods_quantity[name] = count

print(goods_quantity)