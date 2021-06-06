
class File_Opp:
    def __init__(self) -> None:
        pass

    def save_in_file(self,postcode):
        try:
            with open("postcodey.txt", "a") as f: 
                f.write(f"{postcode}\n")
        except FileNotFoundError:
            print("Niepoprawny plik")
    
    
    def add_to_file(self,postcode):
        if len(postcode) != 6 and postcode[2] != '-':
            raise Exception("Zle wczytany kod pocztowy")
        for i, num in enumerate(postcode):
            if i == 2:
                continue 
            if not num.isnumeric():
                raise Exception("Zły kod pocztowy")
        self.save_in_file(postcode)

    def Main(self):
        postcode = input("Podaj kod pocztowy przykład  XX-XXX : ")
        try:
            self.add_to_file(postcode)
            print("Dodano kod pocztowy do pliku")
        except Exception as add:
            print(add)

m = File_Opp()
m.Main()