class Hotel:
    def __init__(self, Numbers_of_Room, Numbers_Of_Floor):  
        self.Numbers_of_Room = Numbers_of_Room
        self.Numbers_Of_Floor = Numbers_Of_Floor
        self.Rooms = []
        Nr_room = 1
        for Nr_Floor in range(self.Numbers_Of_Floor): 
            for i in range(self.Numbers_of_Room): 
                self.Rooms.append(Room(Nr_room=Nr_room, Nr_Floor=Nr_Floor)) 
                Nr_room += 1
        print(f"Hotel posiada {Numbers_of_Room} pokoi na kazdym piętrze a jest ich {Numbers_Of_Floor}")        
 
    def Whether_The_Room_Is_Free(self):
        for Room in self.Rooms:
            if Room.Whether_Free():
                return True
        return False 
 
    def How_Much_Free_Rooms(self):
        How_Much = 0
        for Room in self.Rooms:
            if Room.Whether_Free():
                How_Much += 1 
        return How_Much
 
    def Take_Free_Rooms(self):
        for Room in self.Rooms: 
            if Room.Whether_Free(): 
                return Room
 
    def Rent_Room(self, person):
        Room = self.Take_Free_Rooms()
        if Room != None: 
            Room.Reserv(person)
            return Room.Nr_room
 
    def WhetherRent_2_Rooms(self):
        for i in range(len(self.Rooms) - 1): 
            if self.Rooms[i].Whether_Free() and self.Rooms[i+1].Whether_Free() and self.Rooms[i].Nr_Floor == self.Rooms[i+1].Nr_Floor:
                return True
 
    def Whether_person_Rent(self, lastname):
        for p in self.Rooms:
            if not p.Whether_Free() and p.person.lastname == lastname:
                return True
        return False
 
    def Release_Room(self, lastname):
        for p in self.Rooms:
            if not p.Whether_Free() and p.person.lastname == lastname: 
                p.Release()
 
 
class Room:
    def __init__(self, Nr_room, Nr_Floor, person = None):
        self.Nr_room = Nr_room
        self.Nr_Floor = Nr_Floor
        self.person = person
 
    def Whether_Free(self):
        return self.person is None 
    def Release(self):
        self.person = None
 
    def Reserv(self, person):
        self.person = person
 
 
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
 


 
h = Hotel(Numbers_of_Room=10, Numbers_Of_Floor=3)
person = Person(name="Agnieszka", lastname="Walczak")
h.Rent_Room(person)
h.Rent_Room(person)
h.Rent_Room(person)
print("Czy Pani Walczak wynajmuje hotel " ,h.Whether_person_Rent("Walczak"))
h.Release_Room("Walczak")
print("A czy teraz wynajmuje hotel bo słyszałem ze się wypisała (Flase - Nie wynajmuje ,True -przeciwnie) :",h.Whether_person_Rent("Kowalski"))
 
person2 = Person(name="Janek", lastname="Marynarka")
h.Rent_Room(person2)
print("Liczba wolnych pokoi :" ,h.How_Much_Free_Rooms())
print("Czy można wynająć 2 Rooms obok siebie :" ,h.WhetherRent_2_Rooms())


class Hotel:
    def __init__(self, rooms, floors, Room):
        self.rooms = rooms
        self.floors = floors
 
        rooms_per_floor = int(self.rooms/self.floors)
        last_floor_rooms = self.rooms % self.floors
 
        room_numbers = [int(room) for room in range(1, self.rooms+1)]
 
        self.List_Room = []
        self.Structure = []
        for floor in range(self.floors):
            floors_here = []
            for room in range(0, rooms_per_floor):
                # floors_here.append(room_numbers.pop(0))
                self.List_Room.append(Room(room_numbers.pop(0), floor))
            self.Structure.append(floors_here)
 
        last_floor = []
        for floor in range(0, last_floor_rooms):
            self.List_Room.append(Room(room_numbers.pop(0), self.floors-1))
        self.Structure[len(self.Structure)-1].extend(last_floor)
 
    def get_List_Room(self):
        return self.List_Room
 
class Room:
    def __init__(self, room_nr, floor):
        self.room_nr = room_nr
        self.floor = floor
        self.Guest = 0

        if self.floor == 0:
            self.floor = "Parter"

        print("Number pokoju :", self.room_nr, "  Piętro :", self.floor, "Gość:", self.Guest)
 
    def show_rooms(self):
 
        if self.Guest == 0:
            to_print = "-----"
        else:
            to_print = str(self.Guest)
 
        print("Number pokoju :", self.room_nr, "  Piętro :", self.floor, " Gość:", to_print)
 
    def leave_room(self):
        self.Guest = 0
        print("Pokój został zwolniony")
    
    def __str__(self):
        return f"Number pokoju : {self.room_nr} Piętro : {self.floor} Gość: {self.Guest}"
 
 
class Person(Hotel):
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return self.name
 
    def take_room(self, room, room_nr):
        self.room_nr = room_nr
 
        if room.Guest == 0:
            room.Guest = self.name
            print(self.name, "wynajął pokój", self.room_nr+1)
        else:
            print(self.name, "ten pokój jest zajęty")
 

def Menu():
    floors = int(input("Piętra: "))
    rooms = int(input("Pokoje: "))
    if floors > rooms:
        print("Piętro nie może być puste !")
        exit()
    else:
        h = Hotel(rooms, floors, Room)
        room_list = Hotel.get_List_Room(h)
        Guest_list = []
        while True:
            print("1. Dodaj gościa")
            print("2. Wynajmij pokój")
            print("3. Wymelduj się z pokóju")
            print("4. Wyjście z Hotelu")
            choice = int(input("Wybierz: "))
            if choice == 1:
                name = input("Podaj nazwę gościa: ")
                Guest_list.append(Person(name))
            elif choice == 2:
                i = 1
                for name in Guest_list:
                    print(i, name)
                    i += 1
                Guest = int(input("Komu chcesz wynająć pokój (id): "))
                for room in room_list:
                    room.show_rooms()
                room_to_give = int(input(f"Który pokój ma wziąć: "))-1
                Guest_list[Guest -1].take_room(room_list[room_to_give], room_to_give)
            elif choice == 3:
                for room in room_list:
                    room.show_rooms()
                room_to_leave = int(input("Który pokój chcesz zwolnić: "))
                room_list[room_to_leave-1].leave_room()
            elif choice == 4:
                print("Naraska ")
                break
            for i in (room_list):
                print(i)


Menu()