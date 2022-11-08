import module1 as mod

Title = input("Enter The Title: ")
Direct = input("Enter The Director: ")
AgeRate = int(input("Enter The Age Rating: "))
Genre = input("Enter The Genre: ")

Film = mod.Movie(Title,Direct,AgeRate,Genre)

Film.Description()
