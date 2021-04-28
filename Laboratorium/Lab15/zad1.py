import os


class Restaurant:
    def __init__(
        self,
        Name_resturant,
        size,
        number_of_tables,
        number_of_employees,
        name_owner,
        Last_name_owner,
        Pesel,
        Secret_code,
    ):
        self.Name_resturant = Name_resturant
        self.size = size
        self.number_of_tables = number_of_tables
        self.number_of_employees = number_of_employees
        self.name_owner = name_owner
        self.Last_name_owner = Last_name_owner
        self.Pesel = Pesel
        self.Secret_code = Secret_code

    def WeryfikacjaKlienta(self):
        Pass_Name = input("Podaj imie:")
        if Pass_Name == self.name_owner:
            Pass_last_name = input("Podaj Nazwisko:")
            if Pass_last_name == self.Last_name_owner:
                Pass_Pesel = int(input("Podaj Pesel :"))
                if Pass_Pesel == self.Pesel:
                    Pass_Secret_code = input("Podaj Tajny Kod :")
                    if Pass_Secret_code == self.Secret_code:
                        print("Udało ci się przejść weryfikację ! Witaj")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


class IceCreamStand(Restaurant):
    price_Type = [3.99, 3.00, 3.59]
    price_Flavorus = [0.60, 0.80, 0.60, 0.90, 1.00]

    def __init__(
        self,
        Name_resturant,
        size,
        number_of_tables,
        number_of_employees,
        name_owner,
        Last_name_owner,
        Pesel,
        Secret_code,
        flavor,
        type_flavorus,
    ):
        super().__init__(
            Name_resturant,
            size,
            number_of_tables,
            number_of_employees,
            name_owner,
            Last_name_owner,
            Pesel,
            Secret_code,
        )
        self.flavor = [
            "Truskawkowy",
            "Czekoladowy",
            "Waniliowy",
            "Wiśniowy",
            "Karmelowy",
        ]
        self.type_flavorus = ["Swiderek", "Zwykły", "Zawijaniec"]

    def Price(self, CHOFAT):

        Finally_Price = (
            self.price_Type[CHOFAT[0] - 1] + self.price_Flavorus[CHOFAT[1] - 1]
        )
        return round(Finally_Price, 2)

    def LetsBuy(self):
        choise = int(input(f"Wybierz Typ : 1-{len(self.type_flavorus)} ?:"))
        choise_2 = int(input(f"A Smak ?: 1-{len(self.flavor)} ?:"))
        print(f"Zakupiłes kozackie lody przejdzmy do płatności ")

        return choise, choise_2

    def Print_Type(self):
        iterrator = 1
        print("Dostępne Typy Lodów :")
        for i in self.type_flavorus:
            print(iterrator, ".", i)
            iterrator += 1
        print("Dostępne Smaki Lodów :")
        iterrator = 1
        for i in self.flavor:
            print(iterrator, ".", i)
            iterrator += 1

    def Add_Type_Or_Flavours(self):
        if self.WeryfikacjaKlienta():
            Add_Flavour = input("Podaj nowy smak loda :")
            self.flavor.append(Add_Flavour)
            Add_Price_flavour = float(input("Podaj cenę smaku :"))
            self.price_Flavorus.append(Add_Price_flavour)
            Add_Type = input("Podaj rodzaj loda :")
            self.type_flavorus.append(Add_Type)
            Add_Price_Type_flavours = float(input("Podaj cenę rodzaju loda :"))
            self.price_Type.append(Add_Price_Type_flavours)
            print("Wyświetle ci teraz liste lodów :")
            self.Print_Type()
        else:
            print("Nie udało się przejść weryfikacji !")


class CoffeShop(Restaurant):
    price_coffe = [3.99, 3.00, 3.59]
    price_Type = [0.60, 0.80, 0.60, 0.90, 1.00]

    def __init__(
        self,
        Name_resturant,
        size,
        number_of_tables,
        number_of_employees,
        name_owner,
        Last_name_owner,
        Pesel,
        Secret_code,
        coffe,
        coffe_Type,
    ):
        super().__init__(
            Name_resturant,
            size,
            number_of_tables,
            number_of_employees,
            name_owner,
            Last_name_owner,
            Pesel,
            Secret_code,
        )
        self.coffe = ["Czarna", "Biała", "Z mlekiem"]
        self.coffe_Type = ["Americano ", "Lungo", "Ristretto", "Espresso"]

    def Price(self, CHOFAT):

        Finally_Price = self.price_coffe[CHOFAT[0] - 1] + self.price_Type[CHOFAT[1] - 1]
        return round(Finally_Price, 2)

    def LetsBuy(self):
        choise = int(input(f"Wybierz Kawke  : 1-{len(self.coffe)} ?:"))
        choise_2 = int(input(f"A Rodzaj ?: 1-{len(self.coffe_Type)} ?:"))
        print(f"Zakupiłes kozacką kawkę przejdzmy do płatności ")

        return choise, choise_2

    def Print_Type(self):
        iterrator = 1
        print("Dostępne Kawy :")
        for i in self.coffe:
            print(iterrator, ".", i)
            iterrator += 1
        print("Dostępne Rodzaje Kaw:")
        iterrator = 1
        for i in self.coffe_Type:
            print(iterrator, ".", i)
            iterrator += 1

    def Add_Type_Or_Coffe(self):
        if self.WeryfikacjaKlienta():
            Add_Coffe = input("Podaj nową kawe (Białą , czarna ?itp.):")
            self.coffe.append(Add_Coffe)
            
            Add_Price_Coffe = float(input("Podaj cene kawy :"))
            self.price_coffe.append(Add_Price_Coffe)
            
            
            Add_Type = input("Podaj rodzaj kawy:")
            self.coffe_Type.append(Add_Type)
           
            Add_Price_Type = float(input("Podaj cenę rodzaju kawy :"))
            self.price_Type.append(Add_Price_Type)
            
            print("Wyświetle ci teraz liste Kaw i typów :")
            self.Print_Type()
        else:
            print("Nie udało się przejść weryfikacji !")


def Main():

    resturant = Restaurant("Jamnik", "1500m2", 50, 15, "Karol", "Nowak", 123456789, "54#@!")
    iceCream = IceCreamStand("Lodziarnia u Zbydszka ","15m2",15,3,"Tobiasz","Mazurek",123456789,"12#$%", [],[])
    coffeshop = CoffeShop("Kawirania u Janiny ","25m2",15,3,
        "Jadwiga",
        "Walczak",
        987654321,
        "98!@3",
        [],
        [],
    )

    while True:
        i = 0
        Save_choise = 0
        Price_flavorus = 0.0
        choise = 0
        Price_Coffe = 0
        choise_restaurant = int(
            input(
                "Wchodzisz do lodziarni (Wpisz 1) czy do kawiarni (Wpisz 2) lub wyjscie (Wpisz 3) :"
            )
        )
        if choise_restaurant == 1:
            while True:
                print("\tOto menu:")
                print("\t1. Pokaz Rodzaje lodów i ich smaki")
                print("\t2. Zakup lodów")
                print(
                    "\t3. Dodaj Dodatkowy Smak lodów (Oczywiście jeśli przejdziesz weryfikacje)"
                )
                print("\t4. Koniec zakupów i podliczenie Pieniędzy")
                print("\t5. Wyjście z lodziarni \n")
                choise_menu = int(input("Wybierz Opcje od 1-5 :"))
                print()
                if choise_menu == 1:
                    iceCream.Print_Type()
                    os.system("PAUSE")
                elif choise_menu == 2:
                    choise = iceCream.LetsBuy()
                    Save_choise = 2
                    os.system("PAUSE")
                elif choise_menu == 3:
                    Varriable = iceCream.Add_Type_Or_Flavours()
                    os.system("PAUSE")
                elif choise_menu == 4:
                    if Save_choise != 2:
                        print("Nic nie kupiłes !")
                    else:
                        Price_flavorus += iceCream.Price(choise)
                        print("Cena Do zapłaty : ", Price_flavorus)
                        i = 1
                        Price_flavorus = 0.0
                        os.system("PAUSE")
                elif choise_menu == 5:
                    if Save_choise == 2 and i != 1:
                        print("Hola Hola nie zapłaciłes !!!")
                    else:
                        print("Dziękujemy ze nas odwiedziłeś")
                        break

        elif choise_restaurant == 2:
            while True:
                print("\tOto menu:")
                print("\t1. Pokaz Rodzaje kaw i kawy")
                print("\t2. Zakup kawy")
                print(
                    "\t3. Dodaj Dodatkowy Smak Kawy i rodzaj (Oczywiście jeśli przejdziesz weryfikacje)"
                )
                print("\t4. Koniec zakupów i podliczenie Pieniędzy")
                print("\t5. Wyjście z Kawiarni \n")
                choise_menu = int(input("Wybierz Opcje od 1-5 :"))
                print()
                if choise_menu == 1:
                    coffeshop.pPrint_Type()
                    os.system("PAUSE")
                elif choise_menu == 2:
                    choise = coffeshop.LetsBuy()
                    Save_choise = 2
                    os.system("PAUSE")
                elif choise_menu == 3:
                    Varriable = coffeshop.Add_Type_Or_Coffe()
                    os.system("PAUSE")
                elif choise_menu == 4:
                    if Save_choise != 2:
                        print("Nic nie kupiłes !")
                    else:
                        Price_Coffe += coffeshop.Price(choise)
                        print("Cena Do zapłaty : ", Price_Coffe)
                        i = 1
                        os.system("PAUSE")
                        Price_Coffe = 0
                elif choise_menu == 5:
                    if Save_choise == 2 and i != 1:
                        print("Hola Hola nie zapłaciłes !!!")
                    else:
                        print("Dziękujemy ze nas odwiedziłeś")
                        break

        elif choise_restaurant == 3:
            print("Dziękujemy za wizytę")
            break


if __name__ == "__main__":
    Main()


