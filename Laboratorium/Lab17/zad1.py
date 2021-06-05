from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("sqlite:///college.db", echo=True)
meta = MetaData()

Movie = Table(
    "Movie",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("director", String),
    Column("cast", String),
    Column("vod", String)
)
# Movie = Table(
#     "Movie",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("director", string),
#     Column("cast", string),
#     Column("vod", string)
# )

# vod = Table(
#     "vod",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("movie_id", Integer),
# )
# cast = Table(
#     "vod",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
# )
# director = Table(
#     "director",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("name", String)
# )
meta.create_all(engine)

class Film:
    cast = []
    def __init__(self,name,director,cast,vod):
        self.name = name 
        self.director = director
        self.cast = cast
        self.vod = vod

    def AddActor(self):
        actor = input("Wprowadz imie i nazwisko aktora")
        self.cast.append(actor)
    
    def AddVod(self):
        vod = input("Wprowadz VOD")
        self.cast.append(vod)
    def Add_Movie(self):
        ins = Movie.insert()
        ins = Movie.insert().values(name = self.name, director = self.director,cast = self.cast, vod = self.vod )
        conn = engine.connect()
        result = conn.execute(ins)
        
        conn.execute(Movie.insert(), [
        {'name':'Bhaskar', 'director' : 'sdax','cast':'aaa','vod': 'Netflix'},
        {'name':'Avengers', 'director' : 'dsax','cast':'sss','vod': 'HBO'},
        {'name':'Harry Potter', 'director' : 'dsad','cast':'ddd','vod': 'Netflix'},
        {'name':'Więźień LAbiryntu', 'director' : 'dasdas','cast':'ccc','vod': 'Raukten'},
        ])

    def Delete(self):
        conn = engine.connect()
        stmt = Movie.delete().where(Movie.c.name == 'Bhaskar')
        conn.execute(stmt)
        s = Movie.select()
        conn.execute(s).fetchall()
    def Upgrade(self):
        conn = engine.connect()
        stmt=Movie.update().where(Movie.c.name=='Avengers').values(name='Avengers 2')
        conn.execute(stmt)
        s = Movie.select()
        conn.execute(s).fetchall()
    def Print(self):
        s = input("Podaj czego szukasz , musisz podać dokładną i pełną nazwe : ")
        conn = engine.connect()
        s = Movie.select().where(Movie.c.name==s)
        result = conn.execute(s)
        for row in result:
            print (row)

def Main():
    movie1 = Film("Avengers","KtosTam","xdd","Netflix")     
    while True:
        print("Witaj w menu ")
        print("1.Szukaj Film  ") 
        print("2.Dodaj Filmy")        
        print("3.Usun Film ")        
        print("4.Upgrade Filmów ")   
        print("5.Wyjście ")  
        choise = int(input("Wybierz :"))
        if choise == 1:
            movie1.Print()
        elif choise == 2:
            movie1.Add_Movie()
        elif choise == 3:
            movie1.Delete()
        elif choise == 4:
            movie1.Upgrade()
        elif choise == 5:
            break




Main()
