password = input("Please enter a password: ")
valid = False
# Password has to be between 12 and 15 characters long
while valid == False:
    if len(password) > 12 & len(password) < 15:
        print("Password too short")
        break
    else:
        print("Password accepted")

    # STRENGTHS
    # Check for correct password length
    # Restricts password from being too long or too short
    # Notifies the user of this issue why it was not accepted
    
    # WEAKNWSSES
    # It doesnt LOOP:
    # It doesnt restrict you to specific data types: They can enter numbers, int, string, float... as long as its length is correct it doesnt matter
    # Code is inefficient - too long can be made shorter

    # CONCLUSION
    # Although code was functional and operational
    # It was too long, didn't account for anything other than lenght
    # Not very secure system
    # Would be inproved by requiring special charaters and numbers