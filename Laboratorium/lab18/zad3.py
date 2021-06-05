import random


def Main(pile,queue,how_much): 
    # How much = ilość elemntów dodawanych do talic za pomocą append w pętli for 
    # Zerowanie tablic przy każdej kolejnej pętli
    pile = []
    queue = []
    for i in range(how_much):
        pile.append(random.randint(0, 100))
    print("Stos: ", pile)
    for elements in pile:
        queue.insert(0, elements)
    print("Kolejka: ", queue)



pile = []
queue = []
how_much = 50
for i in range(3):
    Main(pile,queue,how_much)
    how_much+=50