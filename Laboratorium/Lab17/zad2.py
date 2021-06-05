import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.util.langhelpers import string_or_unprintable

if os.path.exists("college2.db"):
    os.remove("college2.db")
# tworzymy instancję klasy Engine do obsługi bazy
base = create_engine("sqlite:///college2.db")  # ':memory:'
# klasa bazowa
Team = declarative_base()
# klasy do zadania
class Zawodnicy(Team):
    __tablename__ = "zawodnicy"
    number_player = Column(Integer, primary_key=True)
    name_player = Column(String(100), nullable=False)
    last_nameplayer = Column(String(100), nullable=False)
    relaction = relationship("Mecze", backref="zawodnicy")


class Mecze(Team):
    __tablename__ = "mecze"
    number_of_game = Column(Integer, primary_key=True)
    enemy = Column(String(100), nullable=False)
    the_best_player = Column(Integer, ForeignKey("zawodnicy.number_player"))


# tworzymy tabele
Team.metadata.create_all(base)

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=base)
sesja = BDSesja()


# Sprawdzamy czy jest pusta


def check_if_empty_zawodnicy():
    if not sesja.query(Zawodnicy).count():
        print(
            "Nie ma zawodników w Drużynie.\nCzy chcesz dodać nowych? Innaczej nie będzie na czym pracować.\n"
        )
        print("1 Tak\n2 Nie\n")

        choice = int(input("Wybór :"))
        if choice == 1:
            add_player()
        elif choice == 2:
            print("Nie mam na czym pracować, zakończę pracę programu.")
            exit()
        else:
            print("Nie ma takiej opcji... Kończę pracę programu...")
            exit()


# Dodajemy do tabelki bo nie możn apracować na pustej


def add_player():
    number_player_new = int(input("Podaj proszę numer zawodnika : "))
    name_player_new = str(input("Podaj prosze imię zawodnika : "))
    last_nameplayer_new = str(input("Podaj proszę nazwisko zawodnika : "))
    sesja.add(
        Zawodnicy(
            number_player=number_player_new,
            name_player=name_player_new,
            last_nameplayer=last_nameplayer_new,
        )
    )
    read_player()


# odczytujemy tabelkę zawodnicy


def read_player():
    for zawodnicy in sesja.query(Zawodnicy).all():
        print(zawodnicy.number_player, zawodnicy.name_player, zawodnicy.last_nameplayer)
    print()


# usuwamy z tabelki po imieniu i nazwisku zawodnika


def delete_player():
    imie = str(input("Podaj imię i nazwisko zawodnika do usunięcia (Osobno)\ Imie : "))
    nazwisko = str(input("Nazwisko : "))
    sesja.query(Zawodnicy).filter(
        Zawodnicy.name_player == imie and Zawodnicy.last_nameplayer == nazwisko
    ).delete(synchronize_session="evaluate")
    sesja.commit()
    read_player()


# zmienaimy wartości w tabelce na bazie numeru zawodnika filmu


def update_player():
    ajdi = str(input("Podaj proszę numer zawodnika, którego chcesz edytować: \n"))
    updating_criteria = str(
        input(
            "Podaj co chcesz zmienić?\nDla odpowiedznich pól wpisz:\n Numer zawodnika\n Imię\n Nazwisko\n"
        )
    )

    if updating_criteria == "Numer zawodnika":
        wartosc = int(input("Na wartość : "))
        sesja.query(Zawodnicy).filter(Zawodnicy.number_player == ajdi).update(
            {Zawodnicy.number_player: wartosc}, synchronize_session="evaluate"
        )

    elif updating_criteria == "Imię":
        wartosc = str(input("Na wartość : "))
        sesja.query(Zawodnicy).filter(Zawodnicy.name_player == ajdi).update(
            {Zawodnicy.name_player: wartosc}, synchronize_session="evaluate"
        )

    elif updating_criteria == "Nazwisko":
        wartosc = str(input("Na wartość :\n"))
        sesja.query(Zawodnicy).filter(Zawodnicy.last_nameplayer == ajdi).update(
            {Zawodnicy.last_nameplayer: wartosc}, synchronize_session="evaluate"
        )
    else:
        print("Nie ma takiego kryterium")
        pass
    read_player()


def check_if_empty_mecze():
    if not sesja.query(Mecze).count():
        print(
            "Nie ma meczów dla tej drużyny.\n Czy chcesz dodać nowe? Innaczej nie będzie na czym pracować.\n"
        )
        print("1 Tak\n2 Nie")
        choice = int(input("Wybór : "))
        if choice == 1:
            add_match()
        elif choice == 2:
            print("Nie mam na czym pracować, zakończę pracę programu.")
            exit()
        else:
            print("Nie ma takiej opcji... Kończę pracę programu...")
            exit()


# dodaj mecz


def add_match():
    number_of_game_new = int(input("Podaj proszę numer meczu: "))
    enemy_new = str(input("Podaj na kogo grali : "))
    the_best_player_new = str(input("Podaj proszę numer najlepszego zawodnika : "))
    sesja.add(
        Mecze(
            number_of_game=number_of_game_new,
            enemy=enemy_new,
            the_best_player=the_best_player_new,
        )
    )
    read_match()


def read_match():
    for mecze in sesja.query(Mecze).join(Zawodnicy).all():
        print(
            mecze.number_of_game,
            mecze.enemy,
            mecze.the_best_player,
            mecze.zawodnicy.name_player,
            mecze.zawodnicy.last_nameplayer,
        )
    print()


def delete_match():
    numer = str(input("Podaj numer meczu do usunięcia"))
    sesja.query(Mecze).filter(Mecze.number_of_game == numer).delete(
        synchronize_session="evaluate"
    )
    sesja.commit()
    read_match()


def update_match():
    ajdi = str(input("Podaj proszę numer meczu, którego chcesz edytować: \n"))
    updating_criteria = str(
        input(
            "Podaj co chcesz zmienić?\nDla odpowiedznich pól wpisz:\n Numer meczu\n Przeciwko\n Najlepszy zawodnik\n"
        )
    )

    if updating_criteria == "Numer meczu":
        wartosc = int(input("Na wartość :\n"))
        sesja.query(Mecze).filter(Mecze.number_of_game == ajdi).update(
            {Mecze.number_of_game: wartosc}, synchronize_session="evaluate"
        )

    elif updating_criteria == "Przeciwko":
        wartosc = str(input("Na wartość :\n"))
        sesja.query(Mecze).filter(Mecze.enemy == ajdi).update(
            {Mecze.enemy: wartosc}, synchronize_session="evaluate"
        )

    elif updating_criteria == "Najlepszy zawodnik":
        wartosc = str(input("Na wartość :\n"))
        sesja.query(Mecze).filter(Mecze.the_best_player == ajdi).update(
            {Mecze.the_best_player: wartosc}, synchronize_session="evaluate"
        )
    else:
        print("Nie ma takiego kryterium")
        pass
    read_match()


def how_the_best_player():
    print("Ile razy ten zawodnik był najlepszy? Sprawdź to")
    numer = int(input( "wpisz numer : "))
    print(sesja.query(Mecze).filter(Mecze.the_best_player == numer).count())


def how_match_on_enemy():
    i = str(input("Sprawdź ile razy drużyna grała enemy : "))
    print(sesja.query(Mecze).filter(Mecze.enemy == i).count())


def Main():
    while True:
        check_if_empty_zawodnicy()
        check_if_empty_mecze()
        print(
            "Menu:\n 1 Dodaj zawodnika \n 2 Edytuj zawodnika \n 3 Usuń zawodnika \n 4 Przejrzyj zawodników\n 5 Dodaj mecz\n 6 Edytuj mecz \n 7 Usuń mecz \n 8 Przejrzyj mecze \n 9 Sprawdź, ile razy zawodnik był najlepszy \n 10  Sprawdź ile razy grali mecz przeciwko jakieś drużynie \n 0 Wyjdź"
        )
        Z = int(input("Wybór: "))
        if Z == 1:
            add_player()
        elif Z == 2:
            update_player()
        elif Z == 3:
            delete_player()
        elif Z == 4:
            read_player()
        elif Z == 5:
            add_match()
        elif Z == 6:
            update_match()
        elif Z == 7:
            delete_match()
        elif Z == 8:
            read_match()
        elif Z == 9:
            how_the_best_player()
        elif Z == 10:
            how_match_on_enemy()
        elif Z == 0:
            exit()
        else:
            print("Nie ma takiej opcji")


Main()