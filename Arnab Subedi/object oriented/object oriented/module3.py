class movie:
    def __init__(self,title,director,age_rating,genre):
        self.title = title
        self.director = director
        self.age_rating = age_rating
        self.genre = genre
        

    def description(self):
        return f"The name of the film is {self.title}, and its director is {self.director}, it has a age rating of {self.age_rating}, and the genre is {self.genre}"
