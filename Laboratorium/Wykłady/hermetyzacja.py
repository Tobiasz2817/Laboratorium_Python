class Ja:
    def __init__(self):
        self._age = 0
    def get_age(self):
        print("getter :")
        return self._age
    def set_age(self,a):
        print("Setter")
        self._age = a

    def del_age(self):
        del self._age
    
    age = property(get_age,set_age,del_age)

stan = Ja()
stan.age = 100

print(stan.age)