class movie:
    def __init__(self,name,director,rating,age_rating):
        self.name = name
        self.age_rating = age_rating
        self.director = director
        self.rating = rating
    def details(self):
        return  f"The name of the movie is {self.name}, with the director {self.director}, the movie has an age rating of {self.age_rating}, and has an overall rating of {self.rating}"