def save_in_file(postcode):
    try:
        with open("postcodey.txt", "a") as f: 
            f.write(f"{postcode}\n")
    except FileNotFoundError:
        print("Niepoprawny plik")
 
 
def add_to_file(postcode):
    if len(postcode) != 6 and postcode[2] != '-':
        raise Exception("Zle wczytany kod pocztowy")
    for i, num in enumerate(postcode):
        if i == 2:
            continue 
        if not num.isnumeric():
            raise Exception("Zły kod pocztowy")
    save_in_file(postcode)

def Main():
    postcode = input("Podaj kod pocztowy przykład  XX-XXX : ")
    try:
        add_to_file(postcode)
        print("Dodano kod pocztowy do pliku")
    except Exception as add:
        print(add)


Main()