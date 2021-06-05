import linecache
class Taduesz:
    def __init__(self,nazwa):
        self.nazwa = nazwa


    def PrintLinesFromPanTadeusz(self):
        with open("pantadeusz.txt", "r", encoding="utf-8") as readfile:
            count = -1
            for i, lines in enumerate(readfile):
                count += 1
                if i == 8 or i == 12 or i == 60 or i == 98 or i == 104:
                    print(lines)
                    count += 1
            print("Ilość wierszy w inwokacji: ", count-2)

tadeusz = Taduesz("Tadek")
tadeusz.PrintLinesFromPanTadeusz()


