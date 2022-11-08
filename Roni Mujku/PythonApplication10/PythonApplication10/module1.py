class Movie():
    def __init__(self,title,director,age_rating,genre):
        self.__title = title
        self.__director = director
        self.__age_rating = age_rating
        self.__genre = genre

    def Description(self):
        print(f"The movie {self.__title} is the latest release from critically acclaimed director {self.__director} \n"
              f"With an age rating of {self.__age_rating} {self.__title} is best {self.__genre} flick coming out this summer")

    def GetTitle(self):
        print(self.__title)

    def GetRating(self):
        print(self.__age_rating)

    