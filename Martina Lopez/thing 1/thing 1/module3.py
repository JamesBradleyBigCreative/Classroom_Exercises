class Movie:
    def __init__(self, Title, Director, Age_Rating, Genre ):
        self.Title = Title
        self.Director = Director
        self.Age_Rating = Age_Rating
        self.Genre = Genre
       
    def TellADescription(self):
         return f"The movie name is {self.Title}. The director is {self.Director} and the age rating is {self.Age_Rating}. The movie genre is {self.Genre}"
