import module3 as cinema

N1= input("Enter movie Name: ")
D1 = input("Enter director name: ")
A1 = int(input("Enter age rating: "))
G1 = input("Enter movie genre: ")

myMovie = cinema.Movie(N1, D1, A1, G1)

print(myMovie.TellADescription())



