class Animal:
    def __init__(self, age, name=""):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return "<" + self.name + ":" + str(self.age) + ">"


class Cat(Animal):
    def speak(self):
        print("Meow")

    def __str__(self):
        return "<" + self.name + ":" + str(self.age) + ":Cat>"


class Person(Animal):
    def speak(self):
        print("hello")

    def __str__(self):
        return "<" + self.name + ":" + str(self.age) + ":Person>"


class Student(Person):
    def __init__(self, age, name, grade):
        super().__init__(age, name)
        self.grade = grade

    def speak(self):
        print("haha.. I'm so tired.")

    def study(self):
        self.grade += 1

    def __str__(self):
        return "<" + self.name + ":" + str(self.age) + ":Person:Student:" + str(self.grade) + ">"


ani = Animal(13, "mimi")
print(ani)

cat1 = Cat(12, "nami")
print(cat1)
cat1.speak()
cat1.set_name("hani")
print(cat1.get_name())

student1 = Student(17, "mac", 6)
student1.speak()
print(student1)