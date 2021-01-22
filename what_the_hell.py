import sys

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{} is on creation".format(self.name))
    def speak(self):
        print("Hi, my name is {} and I am {}years old".format(self.name, self.age))

a = Person("강호건", 37)
a.speak()

class Student(Person):
    def __init__(self, name, age, ID_Nr):
        Person.__init__(self, name, age)
        self.ID_Nr = ID_Nr
        print("Student '{}' is on creation".format(self.name))
    def speak(self):
        print("Hi, mine is {:d}".format(self.ID_Nr))
b = Student("홍창현", 25, 20041956)
b.speak()
class Professor(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary
        print("Professor '{}' is on creation". format(self.name))
    def speak(self):
        print("Hi, my salary is {:d}".format(self.salary))


c = Professor("a", 23, 30000)

print(__name__)
print(sys.prefix)
print(sys.version)
