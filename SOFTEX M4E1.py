class Album:
  def __init__(self, artist, title, genre, tracks):
    self.artist = artist
    self.title = title
    self.genre = genre
    self.tracks = tracks

  def exibir(self):
    print(self.artist, self.title, self.genre, self.tracks)

album = Album("Artist: Tayor Swift", "\nTitle: RED (taylor's version)", "\nGenre: Country-pop", "\nTracks: 30 tracks")
album.exibir()

class Book:
  def __init__(self, author, title, genre, pages):
    self.author = author
    self.title = title
    self.genre = genre
    self.pages = pages

  def exibir1(self):
    print(self.author, self.title, self.genre, self.pages)

book = Book("\nAuthor: Rick Riordan", "\nTitle: Percy Jackson and The Last Olympian", "\nGenre: Fantasy, YA", "\nPages: 381")
book.exibir1()

class Show:
  def __init__(self, name, director, seasons, episodes):
    self.name = name
    self.director = director
    self.seasons = seasons
    self.episodes = episodes

  def exibir0(self):
    print(self.name, self.director, self.seasons, self.episodes)

show = Show("\nName: Fleabag", "\nDirector: Phoebe Waller-Bridge", "\n Seasons: 2", "\nEpisodes: 12")
show.exibir0()
