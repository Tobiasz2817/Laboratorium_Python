import linecache
class Taduesz:
    def __init__(self,nazwa):
        self.nazwa = nazwa


    def LoadInwokacjePT(self):
        with open("pantadeusz.txt", "r", encoding="utf-8") as readfile:
            for lines in readfile:
                print(lines.rsplit("\n"))

    

tadeusz = Taduesz("Tadek")
tadeusz.LoadInwokacjePT()