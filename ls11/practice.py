def rome_numbers_convert(number):
    rome_number = ""
    if number > 4000 or number < 0:
        return "Invalid Data"
    
    if number >= 1000: 
        _tmp = number // 1000
        number -= 1000 * _tmp
        rome_number += "M" * _tmp

    if number >= 900 and number < 1000: 
        number -= 900
        rome_number += "CM"

    if number >= 500:
        _tmp = number // 100
        number -= 100 * _tmp
        rome_number += "D" + "C" * (_tmp - 5)

    if number >= 400 and number < 500: 
        number -= 400
        rome_number += "CD"

    if number >= 100: 
        _tmp = number // 100
        number -= 100 * _tmp
        rome_number += "C" * _tmp 

    if number >= 90 and number < 100: 
        number -= 90
        rome_number += "XC"
    
    if number >= 50: 
        _tmp = number // 10
        number -= 10 * _tmp
        rome_number += "L" + "X" * (_tmp - 5)

    if number >= 40 and number < 50: 
        number -= 40
        rome_number += "XL"
    
    if number >= 10: 
        _tmp = number // 10
        number -= 10 * _tmp
        rome_number += "X" * _tmp 

    if number == 9:
        number -= 9
        rome_number += "IX"
    
    if number >= 5: 
        rome_number += "V" + "I" * (number - 5)
        number = 0

    if number == 4: 
        rome_number += "IV"
        number = 0
    
    if number > 1: 
        rome_number += "I" * number
        number = 0 

    return rome_number

num = rome_numbers_convert(2022)

with open('text.txt', "w") as f:
    f.write(num)
    f.close() 