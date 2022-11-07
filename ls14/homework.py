class Student: 

    def __init__(self, name, surname, age):
        self.name = name 
        self.surname = surname
        self.age = age
        self.subjects = {"math": [12, 10, 12, 8], "english": [12, 10, 11, 9]}


    def add_marks(self, subject, mark): 
        
        for item in self.subjects: 
            if subject == item:
                self.subjects[subject].append(mark)
                return 0    
        
        self.subjects[subject] = [mark]

    
    def eq_mark(self, subject):
        for item in self.subjects: 
            if subject == item:
                _mark = 0
                _length = len(self.subjects[subject])
                for el in self.subjects[subject]: 
                    _mark += el 
                return _mark / _length
            else:
                return 'Impossible'

    def __str__(self):

        return f"{self.subjects}"

student1 = Student("Igor", "Groch", 13)

student1.add_marks("math", 10)
student1.add_marks("french", 8)
student1.add_marks("french", 9)
print(student1)
print(student1.eq_mark('math'))

        