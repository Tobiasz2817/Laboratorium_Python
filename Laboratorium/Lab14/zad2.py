class Animal:
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes


class Dog(Animal):
    def __init__(self, name, age, eyes):
        super().__init__(name, age, eyes)
        self.tail = "Medium"
        self.teeths = 42
        self.legs = 4

    def bark(self):
        print("Hau Hau")


class Cat(Animal):
    def __init__(self, name, age, eyes):
        super().__init__(name, age, eyes)
        self.tail = "Long"
        self.teeths = 30
        self.legs = 4

    def meow(self):
        print("Meow!")


class Bird(Animal):
    def __init__(self, name, age, eyes):
        super().__init__(name, age, eyes)
        self.tail = "Short"
        self.wings = 2
        self.legs = 2

    def fly(self):
        for _ in range(0, 10):
            print("\_/ /-\\ \n")


    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Eyes: {self.eyes}"


class Fish(Animal):
    def __init__(self, name, age, eyes):
        super().__init__(name, age, eyes)
        self.gills = "Exist"


bird1 = Bird("Skrzydlaty", "5", "2")

print(bird1.fly())
print(bird1)

