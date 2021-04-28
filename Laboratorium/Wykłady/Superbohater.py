superbohater_list = []
import random


class superbohater():
    def __init__(self, rasa, predkosc, imie, sila):
        self.rasa = rasa
        self.predkosc = predkosc
        self.imie = imie
        self.sila = sila

    def atak(self):
        print("Superbohater {} uderz z sila {} niutiony".format(self.imie, self.sila))

    def biegnij(self):
        print(
            "Superbohater {} biegnie z predkoscia {} km/h".format(
                self.imie, self.predkosc
            )
        )


class Spiderman(superbohater):
    def __init__(self, rasa, predkosc, imie, sila):
        super().__init__(rasa, predkosc, imie, sila)

    def strzel_pajeczyna(self):
        print("Spiderman strzel pajeczyna")

    def walka_wrecz(self, przeciwnik):
        print("atakkk {}!".format(przeciwnik))
        wynik = random.randint(0, 100)
        if wynik > 50:
            print("Spierdman wygrał")
        elif wynik < 50:
            print("Spierdman przegral")
        else:
            print("Remis")
class IronMan(superbohater):
    def __init__(self,rasa,predkosc,imie,sila):
        super().__init__(rasa,predkosc,imie,sila)
   
    def super_zdolnosc(self):
        print("Kombinezon oraz Gadzety")
    def osobowosc(self):
        print("Narcyzm")
    def nemezis(self,przeciwnik):
        print("Przeciwnikiem {} jest {}".format(self.imie,przeciwnik))

class Thor(superbohater):

    def __init__(self, rasa, predkosc , imie, sila):

        super().__init__(rasa, predkosc , imie, sila)



    def piorunemgo(self):

        print("Piorun pier, pier... Nie będę mówił jak. Thor to zrobił. Tak się przestraszyłem, że hej!")



    def mjolnir(self):

        print("Thor uderza młotkiem w brata Lokiego")

        print("Wziął i go zabił no.")



    def Odyn(self):

        print("{} mówi ojcu, że nie jest gotowy objąć tron.".format(self.imie))

    

    def identyfikacja(self):

        print("Ja jestem {}, {} !".format(self.imie, self.rasa))

class Wolverine(superbohater):
    def __init__(self,rasa,predkosc,imie,sila):
        super().__init__(rasa,predkosc,imie,sila)

    def walka(self):
        tab_enemy = ["Sabertooth", "Deadpool", "Magneto"]
        return tab_enemy

    def atak_pazurami(self,tab_enemy):
        dmg = random.randint(30,60)
        rand_enemy = random.choice(tab_enemy)
        print(f"{self.imie} atakuje {rand_enemy}!")
        print(f"Zadał {dmg} obrażeń.")
        if dmg <= 40:
            print("Nie jest to super efektywne.")
        elif 40 <= dmg <= 50:
            print("Niezły atak!")
        else:
            print("Jest super efektywny!")

# spierdman = Spiderman("czlowiek", 32, "Spiderman", 23)
# spierdman.strzel_pajeczyna()
# spierdman.walka_wrecz("Venom")

# ironman=IronMan("Czlowiek","Wchuj szybka ","Tony Stark", 1500)
# ironman.super_zdolnosc()
# ironman.osobowosc()
# ironman.nemezis("Spierdman")

# thor = Thor("Bógpiorunów", 30, "Thor", 9000)
# thor.atak()

Wolverine = Wolverine("Człowiek", 30, "Logan", 50)
Wolverine.atak_pazurami(Wolverine.walka())