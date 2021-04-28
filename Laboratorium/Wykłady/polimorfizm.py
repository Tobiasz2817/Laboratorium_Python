class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hejkato ja {self.name} twójkotelek. Mam {self.age} lat.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"wabie się {self.name}. I mam {self.age} lat.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Mruczuś", 2.5)
dog1 = Dog("Rex", 4)
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()