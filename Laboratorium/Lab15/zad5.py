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