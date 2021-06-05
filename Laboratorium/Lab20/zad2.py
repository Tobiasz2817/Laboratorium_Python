import pytest 

def Men_ppm(mass,heigh,age):
    return (66 + (13.7 * mass) + (5 * heigh) + (6.76 *age))
def Women_ppm(mass,heigh,age):
    return (655 + (9.6 * mass) + (1.8 * heigh) + (4.7 *age))
def Load_Information():
    mass = input("Podaj swoją mase :")
    heigh = input("Podaj swój wzrost :")
    age = input("Podaj swój wiek :")
    return mass,heigh,age

def Menu():
    List = []
    whoam = input("Siema kim jestes :")
    if whoam == "Panda":
        print("Coś jest z tobą nie tak")
    elif whoam == "Mezczyzna":
        List = Load_Information()
        print(Men_ppm(float(List[0]),float(List[1]),float(List[2])))            
    elif whoam == "Kobieta":
        List = Load_Information()
        print(Women_ppm(float(List[0]),float(List[1]),float(List[2])))


Menu()