class Album:
  def __init__(self, artist, title, genre):
    self.artist = artist
    self.title = title
    self.genre = genre

  def exibir(self):
    print(self.artist, self.title, self.genre)

album = Album("Artist: Tayor Swift", "\nTitle: RED (taylor's version)", "\nGenre: Country-pop")
album.exibir()

class Book:
  def __init__(self, author, title, genre):
    self.author = author
    self.title = title
    self.genre = genre

  def exibir1(self):
    print(self.author, self.title, self.genre)

book = Book("\nAuthor: Rick Riordan", "\nTitle: Percy Jackson and The Last Olympian", "\nGenre: Fantasy, YA")
book.exibir1()

class Show:
  def __init__(self, name, director, seasons):
    self.name = name
    self.director = director
    self.seasons = seasons

  def exibir0(self):
    print(self.name, self.director, self.seasons)

show = Show("\nName: Fleabag", "\nDirector: Phoebe Waller-Bridge", "\n Seasons: 2")
show.exibir0()
