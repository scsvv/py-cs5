list_of_cities = []
last_letter = ''
while True: 
    cities_name = input("Enter cities name: ")
    cities_name = cities_name.lower()
    if cities_name == "e": 
        break
    
    if list_of_cities.count(cities_name):
        print("Такая запись уже есть")
        continue
    
    if cities_name[len(cities_name)-1] == ' ': 
        print("Не использовать ПРОБЕЛ, НАЧИНАТЬ СЛОВО С БУКВЫ Ы")
        last_letter = "Ы"
        list_of_cities.append(cities_name.pop())
        continue    


    if cities_name[0] != last_letter and last_letter != '': 
        print(f"Название города должно начинатся с {last_letter}")
        continue
    
    
    list_of_cities.append(cities_name)
    last_letter = (cities_name[len(cities_name)-1])

print(list_of_cities)