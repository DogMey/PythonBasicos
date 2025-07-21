class EmptyPerson:
    pass # This is a class definition for EmptyPerson

print(EmptyPerson())  # Output: <class '__main__.EmptyPerson'>

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"    # This is a public attribute
        self.__name = name # This is a private attribute
        self.__surname = surname

    def getName (self):
        return self.__name
    
    def walk (self):
        print(f"{self.full_name} is walking")

my_person = Person("Kevin", "Ramirez")
# print(my_person.__name)  # Output: Kevin
print(my_person.getName())  # Output: Kevin
my_person.walk()  # Output: Kevin is walking

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")