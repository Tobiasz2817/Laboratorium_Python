import random
import os

class Car:
    def __init__(self, mark, model, course, type_, colour, power, value,id_number_vehicle):
        self.mark = mark
        self.model = model
        self.course = course
        self.type_ = type_
        self.colour = colour
        self.power = power
        self.value = value
        self.id_number_vehicle = id_number_vehicle

    def Max_Speed(self):
        max_predkosc_proporcja = 1.4
        return f"{self.mark} jedzie najwięcej z prędkością {max_predkosc_proporcja * self.power} km/h "

    def Drive_Straight(self):
        drive = random.randint(1, 70)
        if drive < 20:
            return "\nKurde cos znosi na prawo .... pora na mechanika"
        elif drive < 50:
            return "\nDobra elegancko jedzie prosto !"
        elif drive < 70:
            return "\nKurde cos znosi na lewo .... pora na mechanika .."

    def Show_Speed(self):
        speed = 0
        while self.power * 1.4 > speed:
            speed += 25
            if speed < self.power * 1.4:
                print("Taka oto przyspiesza", self.model, speed)

    def Oil_Change_ITP(self):
        distance = int(input("\nKiedy Ostatnio wymieniałes olej , Podaj w przejechanych km ? "))
        if distance >= 10000:
            return f"\tNależy Zrobić przebieg !"
        elif distance >= 9000:
            return f"\tMożesz jeszcze jeździć ale zaniedługo bedzię trzeba wymienić !! "
        else:
            return f"\tMożesz jeszcze spokojnie jeźdznić "
    
    def Open_Car(self):
        if self.id_number_vehicle == None:
            print("Sory niemasz takiej funkcji ;/")
        else:
            pass_number = input("\nSprawdzmy czy masz dobry kluczyk lub czy to nie złodziej chce sprawdzić czy samochód jest otwarty (Podaj ID): ")
            for i in range(1,3):
                if pass_number == self.id_number_vehicle:
                    print("\tWeryfikacja Powiodła się ")
                    break
                else:
                    if i == 1:
                        print("\tWeryfikacja Nie Powiodła się ")
                        pass_number = input("Masz Ostatnia szanse , jeśli sie nie uda odpala sie alarm ! :")
                    else: 
                        print("\tŁiŁuŁiŁuŁiŁu")

    def __str__(self):
        return f"\nTwój samochód to {self.mark} o przebiegu {self.course} w kolorze {self.colour} no i oczywiście z mocą {self.power} kuni"


car1 = Car("Ferrari", "F3", 144000, "Kabriolet", "Czerwony", 270, 60000,"1FASD")
car2 = Car("Proshe", "G7", 1200, "Sedan", "Fioletowy", 250, 100000,"3FGDS")
car3 = Car("Skoda", "Fabia", 270000, "Sedan", "Niebieski", 130, 15000,None)
car4 = Car("Audi", "A3", 165000, "Hatchback", "Jasny Niebieski", 200, 25000,"2QWER")
car5 = Car("Audi", "RS7", 12000, "Hatchback", "Mocny Czerwony", 370, 500000,"QZDSA")

car1.Show_Speed()
print(car1)
print(car1.Drive_Straight())
car1.Open_Car()
print(car1.Oil_Change_ITP())
print(car1.Max_Speed())

print()
print()
os.system("PAUSE")

car3.Show_Speed()
print(car3)
print(car3.Drive_Straight())
car3.Open_Car()
print(car3.Oil_Change_ITP())
print(car3.Max_Speed())
