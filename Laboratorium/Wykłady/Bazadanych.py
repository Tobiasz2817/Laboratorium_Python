class BazaDanych:
    def __init__(self):
        self.kontakty = []
    
    def Dodaj_Kontakt(self): 
        imie =  input("Podaj imie :")
        nazwisko = input("Podaj nazwisko :")
        nr_tel = int(input("Podaj nr_tel :"))
        kontakt = (imie,nazwisko,nr_tel)
        self.kontakty.append(kontakt)

    
    def Usun_Kontakt(self):
        x=1
        for i in self.kontakty:
            print(str(x),"." ,i)
            x+=1
        index = int(input("Podaj które kontakty chcesz usunąć :"))    
        del self.kontakty[index-1]
    
    def Wyswietl(self):
        print(self.kontakty)

baza = BazaDanych()
baza.Dodaj_Kontakt()
baza.Dodaj_Kontakt()
baza.Dodaj_Kontakt()
baza.Usun_Kontakt()
baza.Wyswietl()