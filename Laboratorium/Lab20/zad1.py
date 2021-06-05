class is_palindrone_or_not:
    def __init__(self,pal):
       self.pal = pal 
    
    def Check(self):
        palindronic_string = "".join(reversed(list(self.pal)))
        if self.pal == palindronic_string:
            print(f"Word {self.pal} is palindrone")
        else:
            print(f"Word {self.pal} is not palindrone")

if __name__=='__main__':
    check1 = is_palindrone_or_not("grzebien ")
    check2 = is_palindrone_or_not("ala")
  
    for i in (check1,check2):
        i.Check()