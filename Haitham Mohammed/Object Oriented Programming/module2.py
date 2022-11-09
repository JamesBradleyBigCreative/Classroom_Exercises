class Film:
    def __int__ (self, title, director, age_rating,rotten_tomatoes):
        self.title = title
        self.director = director
        self.age_rating = age_rating
        self.rotten_tomatoes = rotten_tomatoes

p5 = Film("Cars2","John Lasseter","7+","39%")

print(p5.title)
