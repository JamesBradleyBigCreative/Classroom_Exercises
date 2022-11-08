content = input("Please enter a password")
result = False

while result == False:
    # Code within TRY is tested
    try:
        temporary = int(content)
    # Runs if test FAILS
    except:
        print("Cannot be converted to integer")
        break
    # Runs if test SUCCEEDS
    else:
        print("Successfully converted to integer")
        result = True
    # Runs irrelevant to the outcome of the test
    finally:
        print("Please try the program again")






