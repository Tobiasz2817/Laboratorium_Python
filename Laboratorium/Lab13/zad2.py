class Book():
    def __init__(self, title, author, pages, actual_page, if_opened):
        self.title = title
        self.author = author
        self.pages = pages
        self.actual_page = actual_page
        self.if_opened = if_opened

    def __del__(self):
        print()
        if self.if_opened == True:
            print("Nie zamknąłeś książki", self.title,
                  ", pogniotła się i", self.author, "jest smutny/a")
        else:
            print("Dziękujemy że dbasz o książki",
                  self.author, "bardzo się cieszy :)")

    def __repr__(self):
        return str(self.title + " " + self.author)

    def open_book(self):
        self.if_opened = True

    def close_book(self):
        self.if_opened = False

    def czytaj(self):
        print()
        if self.if_opened == True:
            print("czytasz", self.title, "jesteś na",
                self.actual_page, "stronie")
            print("zostało Ci jeszcze", self.pages-self.actual_page, "stron")
            pages_to_read = int(input("Ile stron chcesz przeczytać: "))
            self.actual_page += pages_to_read
            while self.actual_page > self.pages:
                self.actual_page -= pages_to_read
                print("Ta książka nie ma tylu stron!")
                pages_to_read = int(input("Ile stron chcesz przeczytać: "))
                self.actual_page += pages_to_read
            if self.pages - self.actual_page > 0:
                print("zostało Ci jeszcze", self.pages -
                      self.actual_page, "stron")
            elif self.pages - self.actual_page == 0:
                print("Ukończyłeś książkę", self.title, "!!!")
        else:
            print("Zamkniętej książki się nie czyta...")

def Main():
    Book_list = []
    book1 = Book('Więzień Labiryntu', 'J.Dashner', 500, 230, False)
    book2 = Book('Władcy pierścieni', 'J.R.R. Tolkien', 500, 340, False)
    book3 = Book('Programista samouk', 'Cory Althoff', 251, 230, False)


    Book_list.append(book1)
    Book_list.append(book2)
    Book_list.append(book3)

    book1.open_book()
    book1.czytaj()
    book1.close_book()

    book2.czytaj()

    book3.open_book()
    book3.czytaj()

    print()
    print("LISTA KSIĄŻEK POSORTOWANA WEDŁUG TYTUŁÓW")
    Book_list.sort(key=lambda x: x.title)
    for book in Book_list:
        print(book)

if __name__ == "__main__":
    Main()