import module1 as cinema
N1= str(input("Enter movie Name"))
D1 = str(input("Enter director name"))
A1 = int(input("Enter age rating"))
G1 = str(input("Enter movie genre"))
Des1 = str(input("Enter movie description")) 

print(cinema.Movie.TellADescription(cinema.Movie)(N1, D1, A1, G1, Des1)))