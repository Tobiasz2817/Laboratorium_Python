class Citizen:
    def __init__(self, name, last_name, street, house_number, post_code, town):
        self.name = name
        self.last_name = last_name
        self.street = street
        self.house_number = house_number
        self.post_code = post_code
        self.town = town

    def Load(self):
        file_ = open("showcase.txt", "w")
        file_.write(
            f"---------------------\n{self.name} {self.last_name}\nul.{self.street} {self.house_number}\n{self.post_code} {self.town}\n---------------------"
        )
        file_.close()
    def Print(self):
        showcase = open("showcase.txt").read()
        print(showcase)\



citizen1 = Citizen("Tobiasz", "Mazurek", "3 Maja", 11, "63-440", "Raszków")
citizen1.Load()
citizen1.Print()
