class Parking:
    miejsca = { }#{miejsce parkingowe}: {blachy samochodu}
    tablice = {}#{blachy}: {czy na parkingu}
    def zarejestruj(self, blachy, miejsce):
        if miejsce not in range(1, 10):
            print("Nie ma takiego miejsca")
        else:
            if blachy not in self.tablice:
                self.tablice[blachy] = False
                self.miejsca[miejsce] = blachy
            else:
                print("Samochód jest już w bazie.")

    def wjazd(self, blachy):
        if blachy not in self.tablice:
            print("Samochodu nie ma w bazie")
        else:
            self.tablice[blachy] = True
    def wyjazd(self, blachy):
        if blachy not in self.tablice:
            print("Samochodu nie ma w bazie")
        else:
            self.tablice[blachy] = False
    def sprawdz_blache(self, blachy):
        for x in self.miejsca:
            if self.miejsca[x] == blachy:
                nr = x

        if blachy not in self.tablice:
            print("Samochodu nie ma w bazie")
        else:
            if self.tablice[blachy]:
                print("Samochód znajduje się na parkingu, na miejscu {}".format(nr))
            else:
                print("Samochód nie znajduje się na parkingu.")

    def usun_pojazd(self, blachy):
        if blachy not in self.tablice:
            print("Samochodu nie ma w bazie")
        else:
            for x in self.miejsca:
                if self.miejsca[x] == blachy:
                    nr = x
            del self.tablice[blachy]
            del self.miejsca[nr]


parking1 = Parking()

parking1.zarejestruj("DW1234", 8)
parking1.zarejestruj("DW9999", 12)

parking1.wjazd("DW1234")
parking1.sprawdz_blache("DW1234")

print(parking1.tablice, parking1.miejsca)