import module3 as mod

t = input("what is the title of your film: ")
d = input("what is the name of the director: ")
a = input("enter the age rating: ")
g = input("enter the genre of the film: ")

print(mod.movie.description(mod.movie(t,d,a,g)))
