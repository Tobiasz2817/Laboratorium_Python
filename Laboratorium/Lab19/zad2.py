import sys
 
def LoadFile(plik):
    row = [] 
    try:
        with open(plik, "r") as f:
            row = f.readlines()
    except FileNotFoundError: 
        print(f"Brak pliku {plik}")
    return row
 

def Main():
    if len(sys.argv) == 3:
        File1 = sys.argv[1]
        File2 = sys.argv[2] 
    else:
        File1 = input("Podaj nazwe pliku :")
        File2 = input("Podaj nazwe kolejnego pliku :")

    row1 = LoadFile(File1)
    row2 = LoadFile(File2)
    
    dl = len(row1) if len(row1) > len(row2) else len(row2)
    
    for i in range(dl):
        if i < len(row1):
            print(row1[i], end="")
        if i < len(row2):
            print(row2[i], end="")

Main()