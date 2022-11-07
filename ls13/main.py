"""
class Cat:

    def __init__(self, _name, _age, _gender, _color, _weight):
        self.name = _name 
        self.age = _age
        self.gender = _gender
        self.color = _color
        self.weight = _weight
        
    def __str__(self):
        return f"cat's name is {self.name}"

    def meow(self):
        print(f"{self.name} said meow")


murchik = Cat("Murchik", 1, "male", "black and white", 1.9)
kasper = Cat("Kasper", 4, "male", "red", 4)

print(murchik)

murchik.meow()
print(kasper)
kasper.meow() 
"""

class Triangle: 

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class IsoscelesTriangle(Triangle):
    
    def __init__(self, a, c):
        super().__init__(a, a, c)

class EqTriangle(Triangle):
    
    def __init__(self, a):
        super().__init__(a, a, a)


a = Triangle(1, 1, 1)
b = IsoscelesTriangle(1, 1)
c = EqTriangle(10)

print(c.a)
