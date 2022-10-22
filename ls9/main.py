# tuple1 = ('Kiev', 3000000, 540, 'Ukraine')
# [], (), {}
# list[1]
'''
dict1 = {
    "orange": 13, 
    "banana": 14,
    "blackberry": 15,    
}
print(dict1["orange"])
'''

good1 = {
    'name': 'Cola', 
    'price': 18, 
    'decription': 'olololo', 
    'img': 'img'
}

good2 = {
    'name': 'Pepsi', 
    'price': 18, 
    'decription': 'olololo', 
    'img': 'img'
}

good3 = {
    'name': 'Sprite', 
    'price': 18, 
    'decription': 'olololo', 
    'img': 'img', 
    'quantity': 34
}

goods = [good1, good2, good3]

for value in good1.items(): 
    print(f'{value[0]}: {value[1]}')